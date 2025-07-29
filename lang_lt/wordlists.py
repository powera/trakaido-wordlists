#!/usr/bin/python3

"""Wordlists for Trakaido, a language learning app for Lithuanian."""

import os
import importlib.util
from typing import Dict, List, Any, Optional
from .levels import levels

class WordListManager:
    """
    Manages word lists using the generated directory structure.
    
    This class lazily loads dictionary files from generated/dictionary/ and
    structure files from generated/structure/, then compiles word lists by
    matching GUIDs to dictionary entries.
    """
    
    def __init__(self):
        self._dictionary_cache: Dict[str, Dict[str, Any]] = {}
        self._structure_cache: Dict[str, Dict[str, List[str]]] = {}
        self._compiled_cache: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        
        # Get the directory path for generated files
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.generated_dir = os.path.join(current_dir, 'generated')
        self.dictionary_dir = os.path.join(self.generated_dir, 'dictionary')
        self.structure_dir = os.path.join(self.generated_dir, 'structure')
    
    def _load_dictionary_file(self, filename: str) -> Dict[str, Any]:
        """Load a dictionary file and return all GUID entries."""
        if filename in self._dictionary_cache:
            return self._dictionary_cache[filename]
        
        file_path = os.path.join(self.dictionary_dir, filename)
        if not os.path.exists(file_path):
            return {}
        
        try:
            # Import the dictionary module using the package path
            dict_name = filename[:-3]  # Remove '.py'
            module_path = f"data.trakaido_wordlists.lang_lt.generated.dictionary.{dict_name}"
            module = importlib.import_module(module_path)
            
            # Extract all GUID entries (variables that start with N, V, P, A, C, D, etc.)
            guid_entries = {}
            for attr_name in dir(module):
                if attr_name.startswith(('N', 'V', 'P', 'A', 'C', 'D')) and not attr_name.startswith('_'):
                    attr_value = getattr(module, attr_name)
                    if isinstance(attr_value, dict) and 'guid' in attr_value:
                        guid_entries[attr_name] = attr_value
            
            self._dictionary_cache[filename] = guid_entries
            return guid_entries
            
        except ImportError as e:
            print(f"Failed to import dictionary module {module_path}: {e}")
            return {}
    
    def _load_structure_file(self, filename: str) -> Dict[str, List[str]]:
        """Load a structure file and return the structure mapping."""
        if filename in self._structure_cache:
            return self._structure_cache[filename]
        
        file_path = os.path.join(self.structure_dir, filename)
        if not os.path.exists(file_path):
            return {}
        
        try:
            # Import the structure module using the package path
            corpus_name = filename[:-13]  # Remove '_structure.py'
            module_path = f"data.trakaido_wordlists.lang_lt.generated.structure.{corpus_name}_structure"
            module = importlib.import_module(module_path)
            
            # Find the structure variable (should be named like "words_one_structure")
            raw_structure_data = {}
            for attr_name in dir(module):
                if attr_name.endswith('_structure') and not attr_name.startswith('_'):
                    raw_structure_data = getattr(module, attr_name, {})
                    break
            
            # Convert the new format to the old format expected by compile_corpus
            # New format: {"Category": {"display_name": "...", "words": [word_objects]}}
            # Old format: {"Category": [guid_strings]}
            structure_data = {}
            for category_name, category_data in raw_structure_data.items():
                if isinstance(category_data, dict) and 'words' in category_data:
                    # Extract GUIDs from word objects
                    guid_list = []
                    for word_obj in category_data['words']:
                        if hasattr(word_obj, 'get') and 'guid' in word_obj:
                            guid_list.append(word_obj['guid'])
                        elif hasattr(word_obj, '__name__'):
                            # If it's a variable reference, use the variable name as GUID
                            guid_list.append(word_obj.__name__)
                    structure_data[category_name] = guid_list
            
            self._structure_cache[filename] = structure_data
            return structure_data
            
        except ImportError as e:
            print(f"Failed to import structure module {module_path}: {e}")
            return {}
    
    def _get_all_dictionary_entries(self) -> Dict[str, Any]:
        """Load all dictionary entries from all dictionary files."""
        all_entries = {}
        
        if not os.path.exists(self.dictionary_dir):
            return all_entries
        
        # Load all dictionary files
        for filename in os.listdir(self.dictionary_dir):
            if filename.endswith('_dictionary.py') and not filename.startswith('__'):
                entries = self._load_dictionary_file(filename)
                all_entries.update(entries)
        
        return all_entries
    
    def compile_corpus(self, corpus_name: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Compile a corpus by loading its structure and matching GUIDs to dictionary entries.
        
        Args:
            corpus_name: Name of the corpus (e.g., "nouns_one")
            
        Returns:
            Dictionary mapping group names to lists of word entries
        """
        if corpus_name in self._compiled_cache:
            return self._compiled_cache[corpus_name]
        
        # Load structure file
        structure_filename = f"{corpus_name}_structure.py"
        structure = self._load_structure_file(structure_filename)
        
        if not structure:
            self._compiled_cache[corpus_name] = {}
            return {}
        
        # Load all dictionary entries
        all_entries = self._get_all_dictionary_entries()
        
        # Compile the corpus
        compiled_corpus = {}
        for group_name, guid_list in structure.items():
            compiled_group = []
            for guid in guid_list:
                if guid in all_entries:
                    compiled_group.append(all_entries[guid])
                else:
                    # Log missing GUID but continue
                    print(f"Warning: GUID {guid} not found in dictionary files")
            compiled_corpus[group_name] = compiled_group
        
        self._compiled_cache[corpus_name] = compiled_corpus
        return compiled_corpus
    
    def get_corpus(self, corpus_name: str) -> Dict[str, List[Dict[str, Any]]]:
        """Get a compiled corpus."""
        return self.compile_corpus(corpus_name)

# Create global instance
_word_manager = WordListManager()

# Load from generated structure for words (non-verbs)
def _get_generated_words():
    """Get word corpora from generated structure."""
    generated_words = {}
    for corpus_name in ["words_one", "words_two", "words_three", "words_four", "words_five", "words_six", "words_seven"]:
        generated_words[corpus_name] = _word_manager.get_corpus(corpus_name)
    return generated_words

# Load generated words
_generated_words = _get_generated_words()

# Import legacy data for non-noun corpora (until they're migrated)
from .verbs import *
from .phrases import *

all_words = {
  # New generated word corpora (replacing nouns_* and common_words*)
  "words_one": _generated_words.get("words_one", {}),
  "words_two": _generated_words.get("words_two", {}),
  "words_three": _generated_words.get("words_three", {}),
  "words_four": _generated_words.get("words_four", {}),
  "words_five": _generated_words.get("words_five", {}),
  "words_six": _generated_words.get("words_six", {}),
  "words_seven": _generated_words.get("words_seven", {}),
  # Keep verbs and phrases as they are for now
  "verbs_present": verbs_present,
  "verbs_past": verbs_past,
  "verbs_future": verbs_future,
  "phrases_one": phrases_one,
}

# Utility functions for backward compatibility
def get_all_word_pairs_flat():
    """
    Get all word pairs from all corpora as a flat list.
    
    Returns:
        list: A list of dictionaries, each containing:
            - english: English word
            - lithuanian: Lithuanian word
            - corpus: Name of the corpus
            - group: Name of the group within the corpus
            - metadata: Metadata dictionary (if available)
    """
    flat_words = []
    
    for corpus_name, corpus_data in all_words.items():
        if isinstance(corpus_data, dict):
            for group_name, word_list in corpus_data.items():
                if isinstance(word_list, list):
                    for word_entry in word_list:
                        if isinstance(word_entry, dict):
                            flat_word = {
                                'english': word_entry.get('english', ''),
                                'lithuanian': word_entry.get('lithuanian', ''),
                                'alternatives': word_entry.get('alternatives', {'english': [], 'lithuanian': []}),
                                'corpus': corpus_name,
                                'group': group_name,
                                'metadata': word_entry.get('metadata', {})
                            }
                            flat_words.append(flat_word)
    
    return flat_words

def get_all_word_pairs_flat_basic():
    """
    Creates a flat list of all word pairs from all corpora with only basic fields.
    
    This function provides backward compatibility for existing API endpoints
    that expect only the basic english/lithuanian format.
    
    Returns:
        list: A list of dictionaries, each containing only 'english', 'lithuanian', 
              'corpus', and 'group' keys.
    """
    flat_words = []
    
    # Iterate through all corpora
    for corpus_name, corpus_data in all_words.items():
        # Iterate through all groups
        for group_name, word_pairs in corpus_data.items():
            # Add each word pair to the flat list with corpus information
            for word_pair in word_pairs:
                # Extract only basic fields for backward compatibility
                flat_word = {
                    'english': word_pair['english'],
                    'lithuanian': word_pair['lithuanian'],
                    'corpus': corpus_name,
                    'group': group_name
                }
                flat_words.append(flat_word)
    
    return flat_words

def get_words_by_corpus_basic(corpus_name, group_name=None):
    """
    Get words for a specific corpus and optional group with only basic fields.
    
    This function provides backward compatibility for existing API endpoints
    that expect only the basic english/lithuanian format.
    
    Args:
        corpus_name: The corpus name
        group_name: Optional group name
    
    Returns:
        list: A list of dictionaries with only basic fields
    """
    if corpus_name not in all_words:
        return []
    
    if group_name:
        if group_name not in all_words[corpus_name]:
            return []
        # Return only basic fields for the specific group
        return [
            {
                'english': word_pair['english'],
                'lithuanian': word_pair['lithuanian']
            }
            for word_pair in all_words[corpus_name][group_name]
        ]
    
    # If no group specified, return all words from all groups in this corpus
    result = []
    for grp, words in all_words[corpus_name].items():
        for word_pair in words:
            result.append({
                'english': word_pair['english'],
                'lithuanian': word_pair['lithuanian']
            })
    return result

def get_words_by_level_enhanced(level_name):
    """
    Get all words for a specific level with full enhanced format.
    
    Args:
        level_name: The level name (e.g., "level_1")
    
    Returns:
        list: List of word objects with all enhanced fields
    """
    if level_name not in levels:
        return []
    
    level_words = []
    for level_item in levels[level_name]:
        corpus = level_item["corpus"]
        group = level_item["group"]
        
        if corpus in all_words and group in all_words[corpus]:
            # Add corpus and group info to each word
            for word_pair in all_words[corpus][group]:
                enhanced_word = word_pair.copy()
                enhanced_word['corpus'] = corpus
                enhanced_word['group'] = group
                level_words.append(enhanced_word)
    
    return level_words

