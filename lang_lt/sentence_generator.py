#!/usr/bin/python3

"""
Final Sentence Generator for Level 20 Lithuanian Learning

This script generates simple sentences using pattern-based generation
with proper dictionary integration and Lithuanian grammar.
Focus on simple patterns for level 20, saving complex ones for later levels.
"""

import json
import logging
import random
import sys
import os
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path

# Configure logging
# To see debug logs for sentence generation rejections, change level to logging.DEBUG
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add the src directory to the path to import LLM clients and sentence generation library
sys.path.append(str(Path(__file__).parent.parent.parent.parent / "src"))

try:
    from clients.unified_client import UnifiedLLMClient
    from clients.types import Schema, SchemaProperty
    LLM_AVAILABLE = True
except ImportError:
    print("LLM client not available. Running without LLM integration.")
    LLM_AVAILABLE = False

try:
    from lib.sentence_generation import SentenceGenerator
    SENTENCE_LIB_AVAILABLE = True
except ImportError:
    print("Sentence generation library not available.")
    SENTENCE_LIB_AVAILABLE = False

# Import verb conjugations from verbs.py
from verbs import verbs_new

class SimpleSentenceGenerator:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.dictionary_path = self.base_path / "generated" / "dictionary"
        
        # Load dictionaries
        self.animals = self._load_dictionary("animal_dictionary.py")
        self.foods = self._load_dictionary("food_drink_dictionary.py")
        self.buildings = self._load_dictionary("building_structure_dictionary.py")
        self.colors = self._load_dictionary("color_dictionary.py")
        self.objects = self._load_dictionary("small_movable_object_dictionary.py")
        self.humans = self._load_dictionary("human_dictionary.py")
        
        # Debug log dictionary sizes
        logger.debug(f"Loaded dictionaries: animals={len(self.animals)}, foods={len(self.foods)}, buildings={len(self.buildings)}, colors={len(self.colors)}, objects={len(self.objects)}, humans={len(self.humans)}")
        
        # Load adjective dictionaries
        self.quality_raw = self._load_dictionary("quality_dictionary.py")
        self.numbers_raw = self._load_dictionary("definite_quantity_dictionary.py")
        
        # Filter quality adjectives for level 20 (basic descriptive adjectives)
        quality_whitelist = ["big", "small", "good", "bad", "hot", "cold", "new", "long", "short", "high", "low", "dark"]
        self.quality = {k: v for k, v in self.quality_raw.items() if k in quality_whitelist}
        
        # Filter numbers 1-8 only
        numbers_whitelist = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
        self.numbers = {k: v for k, v in self.numbers_raw.items() if k in numbers_whitelist}
        
        # Debug log filtered dictionary sizes
        logger.debug(f"Filtered dictionaries: quality={len(self.quality)} (from {len(self.quality_raw)}), numbers={len(self.numbers)} (from {len(self.numbers_raw)})")
        
        # Add hard-coded GUIDs for numbers (in case they're missing from the dictionary)
        number_guids = {
            "one": "A11_002",
            "two": "A11_003", 
            "three": "A11_004",
            "four": "A11_005",
            "five": "A11_006",
            "six": "A11_007",
            "seven": "A11_008",
            "eight": "A11_009"
        }
        
        # Ensure all numbers have GUIDs
        for num_en, guid in number_guids.items():
            if num_en in self.numbers and 'guid' not in self.numbers[num_en]:
                self.numbers[num_en]['guid'] = guid
        
        # Subjects with cases and GUIDs
        self.pronouns = {
            "I": {"nom": "aš", "acc": "mane", "gen": "manęs", "guid": "PRON_001"},
            "you": {"nom": "tu", "acc": "tave", "gen": "tavęs", "guid": "PRON_002"},
            "he": {"nom": "jis", "acc": "jį", "gen": "jo", "guid": "PRON_003"},
            "she": {"nom": "ji", "acc": "ją", "gen": "jos", "guid": "PRON_004"},
            "we": {"nom": "mes", "acc": "mus", "gen": "mūsų", "guid": "PRON_005"},
            "they": {"nom": "jie", "acc": "juos", "gen": "jų", "guid": "PRON_006"},
        }
        
        # Load verbs from verbs.py or use fallback
        self.verbs = self._load_verbs_from_file()
        
        # Gender mapping for common words (simplified)
        self.word_genders = {
            # Foods - mostly feminine
            "bread": "f", "coffee": "f", "milk": "m", "water": "m", "apple": "m",
            "cheese": "m", "fish": "f", "meat": "f", "soup": "f", "cake": "m",
            "beer": "m", "tea": "f", "juice": "m", "wine": "m", "egg": "m",
            
            # Objects - mixed
            "book": "f", "paper": "m", "pen": "m", "table": "m", "chair": "f",
            "car": "m", "house": "m", "phone": "m", "computer": "m", "bag": "m",
            
            # Animals - based on Lithuanian gender
            "dog": "m", "cat": "f", "horse": "m", "bird": "m", "cow": "f",
            "pig": "f", "rabbit": "m", "mouse": "f",
            
            # Quality adjectives - Lithuanian gender
            "big": "m", "small": "m", "good": "m", "bad": "m", "hot": "m", "cold": "m",
            "new": "m", "long": "m", "short": "m", "high": "m", "low": "m", "dark": "m",
            
            # Numbers - Lithuanian gender (masculine forms)
            "one": "m", "two": "m", "three": "m", "four": "m", 
            "five": "m", "six": "m", "seven": "m", "eight": "m"
        }

        # Initialize LLM client if available
        self.llm_client = None
        if LLM_AVAILABLE:
            try:
                self.llm_client = UnifiedLLMClient()
            except Exception as e:
                print(f"Warning: Could not initialize LLM client: {e}")
        
        # Initialize sentence generation library if available
        self.sentence_generator = None
        if SENTENCE_LIB_AVAILABLE and self.llm_client:
            try:
                # Prepare word matrices for the sentence generation library
                word_matrices = {
                    "verbs": self.verbs,
                    "pronouns": self.pronouns,
                    "animals": self.animals,
                    "foods": self.foods,
                    "objects": self.objects,
                    "humans": self.humans,
                    "colors": self.colors,
                    "quality": self.quality,
                    "numbers": self.numbers
                }
                
                # Prepare Lithuanian grammar rules
                grammar_rules = {
                    "lt": {
                        "cases": {
                            "accusative": {
                                "endings": {"default": "ą"}  # Simplified
                            }
                        },
                        "verb_conjugation": {
                            "present": {"default": ""},
                            "past": {"default": ""},
                            "future": {"default": ""}
                        }
                    }
                }
                
                self.sentence_generator = SentenceGenerator(
                    word_matrices=word_matrices,
                    grammar_rules=grammar_rules,
                    llm_client=self.llm_client
                )
                logger.debug("Sentence generation library initialized successfully")
            except Exception as e:
                print(f"Warning: Could not initialize sentence generation library: {e}")
                logger.debug(f"Sentence generation library initialization failed: {e}")

    def _load_dictionary(self, filename: str) -> Dict[str, Dict]:
        """Load a dictionary file and extract word entries"""
        file_path = self.dictionary_path / filename
        if not file_path.exists():
            logger.debug(f"Dictionary loading rejected: file {filename} not found at {file_path}")
            print(f"Warning: Dictionary file {filename} not found")
            return {}
        
        words = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            namespace = {}
            exec(content, namespace)
            
            for name, value in namespace.items():
                if (isinstance(value, dict) and 
                    (name.startswith('N') or name.startswith('A') or name.startswith('D')) and 
                    'english' in value and 
                    'lithuanian' in value):
                    words[value['english']] = value
                    
        except Exception as e:
            logger.debug(f"Dictionary loading rejected: error loading {filename}: {e}")
            print(f"Error loading {filename}: {e}")
            
        logger.debug(f"Dictionary loaded: {filename} contains {len(words)} words")
        return words

    def _load_verbs_from_file(self) -> Dict[str, Dict]:
        """Load verb conjugations from verbs.py"""
        # Define which verbs to use for level 20 and their compatibility
        verb_config = {
            "buy": {
                "infinitive": "pirkti",
                "compatible_objects": ["foods", "objects"],
                "compatible_subjects": ["pronouns", "humans"]
            },
            "eat": {
                "infinitive": "valgyti", 
                "compatible_objects": ["foods"],
                "compatible_subjects": ["pronouns", "humans"]
            },
            "drink": {
                "infinitive": "gerti",
                "compatible_objects": ["drinks"],
                "compatible_subjects": ["pronouns", "humans"]
            },
            "see": {
                "infinitive": "matyti",
                "compatible_objects": ["foods", "objects", "animals"],
                "compatible_subjects": ["pronouns", "humans", "animals"]
            },
            "have": {
                "infinitive": "turėti",
                "compatible_objects": ["foods", "objects"],
                "compatible_subjects": ["pronouns", "humans", "animals"]
            }
        }
        
        verbs = {}
        
        for english_verb, config in verb_config.items():
            infinitive = config["infinitive"]
            
            if infinitive in verbs_new:
                verb_data = verbs_new[infinitive]
                
                # Convert from verbs.py format to sentence generator format
                verbs[english_verb] = {
                    "infinitive": infinitive,
                    "present": self._convert_tense_conjugations(verb_data.get("present_tense", {})),
                    "past": self._convert_tense_conjugations(verb_data.get("past_tense", {})),
                    "future": self._convert_tense_conjugations(verb_data.get("future", {})),
                    "compatible_objects": config["compatible_objects"],
                    "compatible_subjects": config["compatible_subjects"]
                }
            else:
                logger.debug(f"Verb {infinitive} not found in verbs.py, skipping")
        
        logger.debug(f"Loaded {len(verbs)} verbs from verbs.py")
        return verbs
    
    def _convert_tense_conjugations(self, tense_data: Dict[str, Dict]) -> Dict[str, str]:
        """Convert verbs.py tense format to sentence generator format"""
        # Map from verbs.py person codes to sentence generator keys
        person_mapping = {
            "1s": "I",
            "2s": "you", 
            "3s-m": "he",
            "3s-f": "she",
            "1p": "we",
            "3p-m": "they",
            "3p-f": "they"  # Use same as 3p-m for simplicity
        }
        
        conjugations = {}
        
        for person_code, conjugation_data in tense_data.items():
            if person_code in person_mapping:
                key = person_mapping[person_code]
                lithuanian_form = conjugation_data.get("lithuanian", "").replace("aš ", "").replace("tu ", "").replace("jis ", "").replace("ji ", "").replace("mes ", "").replace("jie ", "").replace("jos ", "")
                conjugations[key] = lithuanian_form
        
        # Add animal and person forms (use 3rd person singular)
        if "he" in conjugations:
            conjugations["animal"] = conjugations["he"]
            conjugations["person"] = conjugations["he"]
        
        return conjugations
    


    def _get_accusative_form(self, word: str, lithuanian: str) -> str:
        """Get accusative form of Lithuanian word"""
        # Special cases for numbers (irregular accusative forms)
        number_accusatives = {
            "vienas": "vieną",
            "du": "du",  # "du" stays the same in accusative
            "trys": "tris",
            "keturi": "keturis",
            "penki": "penkis",
            "šeši": "šešis",
            "septyni": "septynis",
            "aštuoni": "aštuonis"
        }
        
        if lithuanian in number_accusatives:
            return number_accusatives[lithuanian]
        
        gender = self.word_genders.get(word, "m")
        
        if gender == "m":
            if lithuanian.endswith("as"):
                return lithuanian[:-2] + "ą"
            elif lithuanian.endswith("is") or lithuanian.endswith("ys"):
                return lithuanian[:-2] + "į"
            elif lithuanian.endswith("us"):
                return lithuanian[:-2] + "ų"
            else:
                return lithuanian + "ą"
        else:
            if lithuanian.endswith("a"):
                return lithuanian[:-1] + "ą"
            elif lithuanian.endswith("ė"):
                return lithuanian[:-1] + "ę"
            elif lithuanian.endswith("is"):
                return lithuanian[:-2] + "į"
            else:
                return lithuanian + "ą"

    def _get_compatible_objects(self, verb: str) -> List[Tuple[str, Dict]]:
        """Get objects compatible with a given verb"""
        compatible_objects = []
        verb_info = self.verbs.get(verb, {})
        compatible_types = verb_info.get("compatible_objects", ["foods", "objects"])
        
        for obj_type in compatible_types:
            if obj_type == "foods":
                compatible_objects.extend(list(self.foods.items()))
            elif obj_type == "drinks":
                drinks = ["water", "coffee", "milk", "beer", "tea", "juice", "wine"]
                for drink in drinks:
                    if drink in self.foods:
                        compatible_objects.append((drink, self.foods[drink]))
            elif obj_type == "objects":
                compatible_objects.extend(list(self.objects.items()))
            elif obj_type == "animals":
                compatible_objects.extend(list(self.animals.items()))
        
        return compatible_objects

    def _get_compatible_subjects(self, verb: str) -> List[Tuple[str, Dict]]:
        """Get subjects compatible with a given verb"""
        compatible_subjects = []
        verb_info = self.verbs.get(verb, {})
        compatible_types = verb_info.get("compatible_subjects", ["pronouns", "humans", "animals"])
        
        for subj_type in compatible_types:
            if subj_type == "pronouns":
                for pronoun, data in self.pronouns.items():
                    compatible_subjects.append((pronoun, {"lithuanian": data["nom"], "guid": data["guid"]}))
            elif subj_type == "humans":
                # Use all available humans from the loaded dictionary
                for human_en, human_data in self.humans.items():
                    compatible_subjects.append((human_en, human_data))
            elif subj_type == "animals":
                # Use all available animals from the loaded dictionary
                for animal_en, animal_data in self.animals.items():
                    compatible_subjects.append((animal_en, animal_data))
        
        return compatible_subjects

    def _get_subject_type(self, subject_en: str) -> str:
        """Determine subject type for verb conjugation"""
        if subject_en in ["I", "you", "he", "she", "we", "they"]:
            return subject_en
        elif subject_en in self.animals:
            return "animal"
        else:
            return "person"

    def _get_english_verb_form(self, verb: str, subject: str, tense: str) -> str:
        """Get correct English verb form"""
        if tense == "present":
            if subject in ["I", "you", "we", "they"]:
                return verb
            else:
                if verb == "buy": return "buys"
                elif verb == "have": return "has"
                elif verb == "drink": return "drinks"
                elif verb.endswith(('s', 'sh', 'ch', 'x', 'z')):
                    return verb + "es"
                else: 
                    return verb + "s"
        elif tense == "past":
            if verb == "buy": return "bought"
            elif verb == "eat": return "ate"
            elif verb == "drink": return "drank"
            elif verb == "see": return "saw"
            elif verb == "have": return "had"
            elif verb == "find": return "found"
            else: return verb + "ed"
        else:  # future
            return f"will {verb}"

    def _create_simple_sentence_pattern(self) -> Optional[Dict[str, Any]]:
        """Create a simple sentence pattern (SVO or SVAO only)"""
        verb = random.choice(list(self.verbs.keys()))
        
        compatible_subjects = self._get_compatible_subjects(verb)
        compatible_objects = self._get_compatible_objects(verb)
        
        if not compatible_subjects or not compatible_objects:
            logger.debug(f"Sentence generation rejected: verb '{verb}' has no compatible subjects ({len(compatible_subjects)}) or objects ({len(compatible_objects)})")
            return None
            
        subject_en, subject_data = random.choice(compatible_subjects)
        obj_en, obj_data = random.choice(compatible_objects)
        tense = random.choice(["present", "past", "future"])
        
        pattern = {
            "subject": {"english": subject_en, "data": subject_data},
            "verb": {"english": verb, "data": self.verbs[verb]},
            "object": {"english": obj_en, "data": obj_data},
            "tense": tense
        }
        
        # Add adjective sometimes (30% chance for level 20)
        if random.random() < 0.3:
            # Choose from colors, quality adjectives, or numbers
            adjective_sources = []
            if self.colors:
                adjective_sources.append(("colors", self.colors))
            if self.quality:
                adjective_sources.append(("quality", self.quality))
            if self.numbers:
                adjective_sources.append(("numbers", self.numbers))
            
            if adjective_sources:
                source_name, source_dict = random.choice(adjective_sources)
                adjective_en = random.choice(list(source_dict.keys()))
                pattern["adjective"] = {
                    "english": adjective_en, 
                    "data": source_dict[adjective_en],
                    "type": source_name
                }
        
        return pattern

    def _pattern_to_sentence(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        """Convert a pattern to English and Lithuanian sentences"""
        subject_en = pattern["subject"]["english"]
        verb_en = pattern["verb"]["english"]
        obj_en = pattern["object"]["english"]
        tense = pattern["tense"]
        
        # Build English sentence
        verb_form = self._get_english_verb_form(verb_en, subject_en, tense)
        
        parts = []
        
        # Handle "the" prefix for subjects
        if subject_en in self.animals or subject_en in self.humans:
            parts.append(f"The {subject_en}")
        else:
            parts.append(subject_en.capitalize())
        
        parts.append(verb_form)
        
        # Handle adjectives and objects
        if "adjective" in pattern:
            adj_type = pattern["adjective"].get("type", "colors")
            adj_en = pattern["adjective"]["english"]
            
            if adj_type == "numbers":
                # Numbers come before the noun, no "the" article
                parts.append(adj_en)
                # Make noun plural for numbers > 1
                if adj_en in ["two", "three", "four", "five", "six", "seven", "eight"]:
                    # Simple pluralization (this could be improved)
                    if obj_en.endswith('y'):
                        obj_plural = obj_en[:-1] + "ies"
                    elif obj_en.endswith(('s', 'sh', 'ch', 'x', 'z')):
                        obj_plural = obj_en + "es"
                    else:
                        obj_plural = obj_en + "s"
                    parts.append(obj_plural)
                else:
                    parts.append(obj_en)
            else:
                # Regular adjectives (colors, quality)
                parts.append(adj_en)
                # Handle "the" prefix for objects when needed
                if obj_en in self.animals:
                    parts.append(f"the {obj_en}")
                else:
                    parts.append(obj_en)
        else:
            # No adjective
            if obj_en in self.animals:
                parts.append(f"the {obj_en}")
            else:
                parts.append(obj_en)
        
        english = " ".join(parts) + "."
        
        # Build Lithuanian sentence
        subject_type = self._get_subject_type(subject_en)
        
        # Get Lithuanian forms
        if subject_en in self.pronouns:
            subject_lt = self.pronouns[subject_en]["nom"]
        else:
            subject_lt = pattern["subject"]["data"]["lithuanian"]
        
        verb_lt = pattern["verb"]["data"][tense][subject_type]
        obj_lt_nom = pattern["object"]["data"]["lithuanian"]
        obj_lt_acc = self._get_accusative_form(obj_en, obj_lt_nom)
        
        lt_parts = []
        lt_parts.append(subject_lt.capitalize())
        lt_parts.append(verb_lt)
        
        if "adjective" in pattern:
            adj_lt = pattern["adjective"]["data"]["lithuanian"]
            adj_acc = self._get_accusative_form(pattern["adjective"]["english"], adj_lt)
            lt_parts.append(adj_acc)
        
        lt_parts.append(obj_lt_acc)
        
        lithuanian = " ".join(lt_parts) + "."
        
        # Track words used
        words_used = []
        
        words_used.extend([
            {"english": subject_en, "lithuanian": subject_lt, "type": "subject", "guid": pattern["subject"]["data"].get("guid", "")},
            {"english": verb_en, "lithuanian": pattern["verb"]["data"]["infinitive"], "type": "verb"},
        ])
        
        if "adjective" in pattern:
            words_used.append({
                "english": pattern["adjective"]["english"],
                "lithuanian": pattern["adjective"]["data"]["lithuanian"],
                "type": "adjective",
                "guid": pattern["adjective"]["data"]["guid"]
            })
        
        words_used.append({
            "english": obj_en,
            "lithuanian": obj_lt_nom,
            "type": "object",
            "guid": pattern["object"]["data"]["guid"]
        })
        
        return {
            "english": english,
            "lithuanian": lithuanian,
            "words_used": words_used,
            "pattern": "SVAO" if "adjective" in pattern else "SVO",
            "tense": tense
        }

    def _generate_sentence_with_llm(self, pattern: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Use LLM to generate a complete sentence from the pattern"""
        if not self.llm_client:
            logger.debug("Sentence generation rejected: LLM client not available")
            return None
        
        # Get available colors for LLM to choose from
        available_colors = list(self.colors.keys()) if self.colors else []
        color_list = ", ".join(available_colors)
        
        # Get some context about the words to help LLM
        subject_info = pattern['subject']['data'] if 'data' in pattern['subject'] else {}
        verb_info = pattern['verb']
        object_info = pattern['object']['data'] if 'data' in pattern['object'] else {}
        
        prompt = f"""
        Create a natural Lithuanian sentence for language learning (Level 20 - beginner) using these components:
        
        Subject: {pattern['subject']['english']} (Lithuanian: {subject_info.get('lithuanian', 'unknown')})
        Verb: {pattern['verb']['english']} in {pattern['tense']} tense
        Object: {pattern['object']['english']} (Lithuanian: {object_info.get('lithuanian', 'unknown')})
        
        Available colors to optionally include: {color_list}
        
        Requirements:
        1. Create a grammatically correct Lithuanian sentence using proper cases (nominative for subject, accusative for object)
        2. Use the correct verb conjugation for the tense and subject
        3. Optionally include ONE appropriate color from the list if it makes sense contextually
        4. Make sure the sentence is logical and natural
        5. Provide both English and Lithuanian versions
        
        If the combination doesn't make logical sense, explain why.
        """
        
        # Define the schema for the expected response
        sentence_generation_schema = Schema(
            "SentenceGeneration",
            "Generated Lithuanian sentence with proper grammar",
            {
                "makes_sense": SchemaProperty("boolean", "Whether the sentence combination makes logical sense"),
                "reason": SchemaProperty("string", "Explanation if the sentence doesn't make sense", required=False),
                "english": SchemaProperty("string", "Natural English sentence", required=False),
                "lithuanian": SchemaProperty("string", "Grammatically correct Lithuanian sentence", required=False),
                "color_used": SchemaProperty("string", "Color that was included in the sentence, or null", required=False)
            }
        )
        
        # Debug log the sentence pattern being generated
        logger.debug(f"Requesting sentence generation from LLM: {pattern['subject']['english']} / {pattern['verb']['english']} / {pattern['tense']} / {pattern['object']['english']}")
        
        try:
            logger.debug(f"Calling LLM generate_chat with model=gpt-5-nano, schema=SentenceGeneration")
            response = self.llm_client.generate_chat(
                prompt=prompt,
                model="gpt-5-nano",
                json_schema=sentence_generation_schema
            )
            
            # Get structured data from the response
            result = response.structured_data
            logger.debug(f"LLM response result: {result}")
            
            if result.get("makes_sense", False):
                return {
                    "english": result.get("english", ""),
                    "lithuanian": result.get("lithuanian", ""),
                    "color_used": result.get("color_used"),
                    "llm_generated": True
                }
            else:
                logger.debug(f"Sentence generation rejected by LLM: {result.get('reason', 'Unknown reason')} (Pattern: {pattern['subject']['english']} {pattern['verb']['english']} {pattern['object']['english']})")
                return None
                
        except Exception as e:
            logger.debug(f"Sentence generation rejected due to LLM error: {e} (Pattern: {pattern['subject']['english']} {pattern['verb']['english']} {pattern['object']['english']})")
            print(f"LLM sentence generation failed: {e}")
            return None

    def generate_with_sentence_library(self, count: int = 10, model: str = "gpt-4o-mini") -> List[Dict[str, Any]]:
        """Generate sentences using the sentence generation library"""
        if not self.sentence_generator:
            print("Sentence generation library not available. Falling back to simple generation.")
            return self.generate_simple_sentences(count=count, use_llm=True)
        
        sentences = []
        attempts = 0
        max_attempts = count * 3
        
        print(f"Generating {count} sentences using sentence generation library...")
        logger.debug(f"Starting library-based sentence generation: target={count}, max_attempts={max_attempts}")
        
        while len(sentences) < count and attempts < max_attempts:
            attempts += 1
            
            # Create pattern using the library
            pattern = self.sentence_generator.create_sentence_pattern("SVO")
            if not pattern:
                logger.debug(f"Library sentence generation attempt {attempts}: Pattern creation failed")
                continue
            
            # Generate sentence using the library's LLM method
            result = self.sentence_generator.generate_with_llm(pattern, "lt", model)
            if result:
                # Convert library result to our format
                sentence = {
                    "english": result["english"],
                    "lithuanian": result["target_sentence"],
                    "subject": pattern["subject"]["key"],
                    "verb": pattern["verb"]["key"],
                    "object": pattern["object"]["key"],
                    "tense": pattern["tense"],
                    "pattern": pattern["pattern_type"],
                    "llm_generated": True,
                    "library_generated": True
                }
                
                # Build words_used array
                words_used = []
                
                # Add subject
                subject_data = pattern["subject"]["data"]
                words_used.append({
                    "english": pattern["subject"]["key"],
                    "lithuanian": subject_data.get("lithuanian", subject_data.get("nom", "")),
                    "type": "subject",
                    "guid": subject_data.get("guid", "")
                })
                
                # Add verb
                verb_data = pattern["verb"]["data"]
                words_used.append({
                    "english": pattern["verb"]["key"],
                    "lithuanian": verb_data.get("infinitive", verb_data.get("lithuanian", "")),
                    "type": "verb"
                })
                
                # Add adjective if used
                if result.get("adjective_used"):
                    adj_key = result["adjective_used"]
                    if "adjective" in pattern:
                        adj_data = pattern["adjective"]["data"]
                        words_used.append({
                            "english": adj_key,
                            "lithuanian": adj_data.get("lithuanian", ""),
                            "type": "adjective",
                            "guid": adj_data.get("guid", "")
                        })
                        sentence["adjective"] = adj_key
                        sentence["adjective_guid"] = adj_data.get("guid", "")
                
                # Add object
                object_data = pattern["object"]["data"]
                words_used.append({
                    "english": pattern["object"]["key"],
                    "lithuanian": object_data.get("lithuanian", ""),
                    "type": "object",
                    "guid": object_data.get("guid", "")
                })
                
                sentence["words_used"] = words_used
                sentences.append(sentence)
                logger.debug(f"Library sentence generation attempt {attempts}: Successfully generated sentence")
            else:
                logger.debug(f"Library sentence generation attempt {attempts}: Library rejected pattern")
                continue
            
            if len(sentences) % 10 == 0:
                print(f"  Generated {len(sentences)}/{count} sentences...")
        
        print(f"Generated {len(sentences)} sentences in {attempts} attempts using library")
        logger.debug(f"Library sentence generation completed: generated={len(sentences)}, target={count}, attempts={attempts}")
        return sentences

    def generate_simple_sentences(self, count: int = 10, use_llm: bool = False, use_library: bool = False) -> List[Dict[str, Any]]:
        """Generate simple sentences for level 20"""
        # Use sentence generation library if requested and available
        if use_library and self.sentence_generator:
            return self.generate_with_sentence_library(count)
        
        sentences = []
        attempts = 0
        max_attempts = count * 2
        
        print(f"Generating {count} simple sentences for level 20...")
        if use_llm:
            print("Using LLM for quality control and color selection...")
        
        logger.debug(f"Starting sentence generation: target={count}, use_llm={use_llm}, max_attempts={max_attempts}")
        
        while len(sentences) < count and attempts < max_attempts:
            attempts += 1
            
            pattern = self._create_simple_sentence_pattern()
            if not pattern:
                logger.debug(f"Sentence generation attempt {attempts}: Pattern creation failed")
                continue
            
            # Generate sentence with LLM or pattern-based approach
            if use_llm:
                # Use LLM to generate the complete sentence
                llm_sentence = self._generate_sentence_with_llm(pattern)
                if llm_sentence:
                    # Add pattern information for reference
                    llm_sentence.update({
                        "subject": pattern["subject"]["english"],
                        "verb": pattern["verb"]["english"],
                        "object": pattern["object"]["english"],
                        "tense": pattern["tense"],
                        "pattern": "SVAO" if llm_sentence.get("color_used") else "SVO"
                    })
                    
                    # Build words_used array with GUIDs for LLM sentences
                    words_used = []
                    
                    # Add subject with GUID
                    subject_lt = pattern["subject"]["data"]["lithuanian"] if pattern["subject"]["english"] not in self.pronouns else self.pronouns[pattern["subject"]["english"]]["nom"]
                    words_used.append({
                        "english": pattern["subject"]["english"],
                        "lithuanian": subject_lt,
                        "type": "subject",
                        "guid": pattern["subject"]["data"].get("guid", "")
                    })
                    
                    # Add verb (no GUID for verbs)
                    words_used.append({
                        "english": pattern["verb"]["english"],
                        "lithuanian": pattern["verb"]["data"]["infinitive"],
                        "type": "verb"
                    })
                    
                    # Add color/adjective if used
                    if llm_sentence.get("color_used") and llm_sentence["color_used"] in self.colors:
                        color_data = self.colors[llm_sentence["color_used"]]
                        llm_sentence["adjective"] = llm_sentence["color_used"]
                        llm_sentence["adjective_guid"] = color_data.get("guid", "")
                        words_used.append({
                            "english": llm_sentence["color_used"],
                            "lithuanian": color_data["lithuanian"],
                            "type": "adjective",
                            "guid": color_data.get("guid", "")
                        })
                    
                    # Add object with GUID
                    words_used.append({
                        "english": pattern["object"]["english"],
                        "lithuanian": pattern["object"]["data"]["lithuanian"],
                        "type": "object",
                        "guid": pattern["object"]["data"].get("guid", "")
                    })
                    
                    llm_sentence["words_used"] = words_used
                    sentence = llm_sentence
                else:
                    # LLM rejected the pattern, skip this attempt
                    logger.debug(f"Sentence generation attempt {attempts}: LLM rejected pattern ({pattern['subject']['english']} {pattern['verb']['english']} {pattern['object']['english']})")
                    if attempts % 50 == 0:
                        print(f"  LLM rejected pattern, trying another...")
                    continue
            else:
                # Use pattern-based generation
                sentence = self._pattern_to_sentence(pattern)
            
            sentences.append(sentence)
            logger.debug(f"Sentence generation attempt {attempts}: Successfully generated sentence ({pattern['subject']['english']} {pattern['verb']['english']} {pattern['object']['english']})")
            
            if len(sentences) % 10 == 0:
                print(f"  Generated {len(sentences)}/{count} sentences...")
        
        print(f"Generated {len(sentences)} sentences in {attempts} attempts")
        logger.debug(f"Sentence generation completed: generated={len(sentences)}, target={count}, attempts={attempts}, success_rate={len(sentences)/attempts*100:.1f}%")
        return sentences

def main():
    """Main function with user interaction"""
    generator = SimpleSentenceGenerator()
    
    print("Simple Lithuanian Sentence Generator for Level 20")
    print("================================================")
    print(f"Loaded dictionaries:")
    print(f"  Animals: {len(generator.animals)} words")
    print(f"  Foods: {len(generator.foods)} words") 
    print(f"  Buildings: {len(generator.buildings)} words")
    print(f"  Colors: {len(generator.colors)} words")
    print(f"  Objects: {len(generator.objects)} words")
    print(f"  Humans: {len(generator.humans)} words")
    print()
    
    # Ask about debug logging
    debug_response = input("Enable debug logging to see rejection reasons? (y/n): ").lower()
    if debug_response.startswith('y'):
        logging.getLogger().setLevel(logging.DEBUG)
        print("Debug logging enabled - you will see detailed rejection reasons.")
        print()
    
    # Ask about sentence generation method
    use_llm = False
    use_library = False
    
    if SENTENCE_LIB_AVAILABLE and generator.sentence_generator:
        print("Sentence generation options:")
        print("1. Simple pattern-based generation (no API calls)")
        print("2. LLM-enhanced generation with GPT-5-nano (API calls)")
        print("3. Use sentence generation library with GPT-4o-mini (API calls)")
        
        choice = input("Choose generation method (1/2/3): ").strip()
        
        if choice == "2":
            use_llm = True
            print("Warning: This will make API calls to GPT-5-nano for each sentence.")
            confirm = input("Continue? (y/n): ").lower()
            if not confirm.startswith('y'):
                use_llm = False
                print("Proceeding with simple pattern-based generation.")
        elif choice == "3":
            use_library = True
            print("Warning: This will make API calls to GPT-4o-mini for each sentence.")
            confirm = input("Continue? (y/n): ").lower()
            if not confirm.startswith('y'):
                use_library = False
                print("Proceeding with simple pattern-based generation.")
        else:
            print("Using simple pattern-based generation.")
            
    elif LLM_AVAILABLE and generator.llm_client:
        response = input("Use LLM (GPT-5-nano) for quality control and color selection? This will make API calls. (y/n): ").lower()
        use_llm = response.startswith('y')
        
        if use_llm:
            print("Warning: This will make API calls to GPT-5-nano for each sentence.")
            confirm = input("Continue? (y/n): ").lower()
            if not confirm.startswith('y'):
                use_llm = False
                print("Proceeding without LLM quality control.")
    else:
        print("LLM not available. Proceeding with simple pattern-based generation only.")
    
    # Generate sentences
    sentences = generator.generate_simple_sentences(count=10, use_llm=use_llm, use_library=use_library)
    
    # Create output
    output = {
        "metadata": {
            "level": "level_20",
            "total_sentences": len(sentences),
            "generated_date": "2025-08-01",
            "description": "Simple sentences for Lithuanian learning level 20 - SVO and SVAO patterns only",
            "version": "final",
            "patterns_used": ["SVO", "SVAO"],
            "llm_quality_control": use_llm,
            "sentence_library_used": use_library,
            "generation_method": "library" if use_library else ("llm" if use_llm else "pattern"),
            "dictionaries_used": {
                "animals": len(generator.animals),
                "foods": len(generator.foods),
                "buildings": len(generator.buildings),
                "colors": len(generator.colors),
                "objects": len(generator.objects),
                "humans": len(generator.humans)
            }
        },
        "sentences": sentences
    }
    
    # Save to JSON file
    output_path = generator.base_path / "level_20_sentences_final.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\nGenerated {len(sentences)} sentences and saved to {output_path}")
    
    # Print some examples
    print("\nExample sentences:")
    for i, sentence in enumerate(sentences[:10]):
        print(f"{i+1}. EN: {sentence['english']}")
        print(f"   LT: {sentence['lithuanian']}")
        print(f"   Pattern: {sentence['pattern']}, Tense: {sentence['tense']}")
        if sentence.get('library_generated'):
            print("   (Generated using sentence library)")
        elif sentence.get('llm_generated'):
            print("   (LLM generated)")
        elif sentence.get('llm_improved'):
            print("   (LLM improved)")
        print()

if __name__ == "__main__":
    main()