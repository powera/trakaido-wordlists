#!/usr/bin/python3

"""Wordlists for Trakaido, a language learning app for Lithuanian."""

from .nouns import *
from .verbs import *
from .phrases import *

all_words = {
  "nouns_one": nouns_one,
  "nouns_two": nouns_two,
  "nouns_three": nouns_three,
  "nouns_four": nouns_four,
  "nouns_five": nouns_five,
  "common_words": common_words,
  "common_words_two": common_words_two,
  "verbs_present": verbs_present,
  "verbs_past": verbs_past,
  "verbs_future": verbs_future,
  "phrases_one": phrases_one,
}

levels = {
    "level_1": [
        {"corpus": "nouns_one", "group": "Food + Drink"},
        {"corpus": "nouns_one", "group": "Clothing"},
        {"corpus": "nouns_one", "group": "Buildings"},
    ],
    "level_2": [
        {"corpus": "nouns_one", "group": "Transportation"},
        {"corpus": "nouns_one", "group": "Plants + Animals"},
        {"corpus": "nouns_one", "group": "Small Physical Objects"},
    ],
    "level_3": [
        {"corpus": "nouns_one", "group": "Colors"},
        {"corpus": "nouns_two", "group": "Numbers"},
        {"corpus": "nouns_two", "group": "Shapes"},
    ],
    "level_4": [
        {"corpus": "nouns_two", "group": "Occupations"},
        {"corpus": "nouns_two", "group": "Emotions"},
        {"corpus": "nouns_three", "group": "Body Parts"},
        {"corpus": "verbs_present", "group": "Mental & Emotional"},
    ],
    "level_5": [
        {"corpus": "nouns_three", "group": "Units of Measurement"},
        {"corpus": "nouns_three", "group": "Materials"},
        {"corpus": "verbs_present", "group": "Actions & Transactions"},
    ],
    "level_6": [
        {"corpus": "verbs_present", "group": "Basic Needs & Daily Life"},
        {"corpus": "verbs_present", "group": "Sensory Perception"},
        {"corpus": "nouns_four", "group": "Days of the Week"},
        {"corpus": "nouns_four", "group": "Months of the Year"},
    ],
    "level_7": [
        {"corpus": "nouns_three", "group": "Additional Foods"},
        {"corpus": "verbs_past", "group": "Mental & Emotional"},
        {"corpus": "verbs_past", "group": "Actions & Transactions"},
        {"corpus": "verbs_past", "group": "Basic Needs & Daily Life"},
    ],
    "level_8": [
        {"corpus": "nouns_five", "group": "Weather"},
        {"corpus": "nouns_five", "group": "Hobbies"},
        {"corpus": "verbs_present", "group": "Movement & Travel"},
        {"corpus": "verbs_past", "group": "Movement & Travel"},
        {"corpus": "verbs_past", "group": "Sensory Perception"},
        {"corpus": "common_words_two", "group": "Question Words"},
    ],
    "level_9": [
        {"corpus": "nouns_five", "group": "Personality"},
        {"corpus": "nouns_five", "group": "Family & Relationships"},
        {"corpus": "nouns_five", "group": "Technology"},
        {"corpus": "verbs_present", "group": "Learning & Knowledge"},
        {"corpus": "verbs_past", "group": "Learning & Knowledge"},
    ],
    "level_10": [
        {"corpus": "phrases_one", "group": "Greetings"},
        {"corpus": "common_words", "group": "Time & Life"},
        {"corpus": "common_words", "group": "Places & Direction"},
        {"corpus": "common_words", "group": "People & Relationships"},
    ],
    "level_11": [
        {"corpus": "common_words", "group": "Thinking & Communication"},
        {"corpus": "common_words", "group": "Descriptive Words"},
        {"corpus": "common_words", "group": "Social & Political"},
        {"corpus": "common_words_two", "group": "Abstract Concepts"},
    ],
    "level_12": [
        {"corpus": "verbs_future", "group": "Basic Needs & Daily Life"},
        {"corpus": "verbs_future", "group": "Movement & Travel"},
        {"corpus": "verbs_future", "group": "Mental & Emotional"},
        {"corpus": "verbs_future", "group": "Sensory Perception"},
        {"corpus": "verbs_future", "group": "Learning & Knowledge"},
        {"corpus": "verbs_future", "group": "Actions & Transactions"},
    ],
    "level_13": [
        {"corpus": "common_words_two", "group": "Grammar - Connectors"},
        {"corpus": "common_words_two", "group": "Grammar - Adverbs of Time and Place"},
        {"corpus": "common_words_two", "group": "Grammar - Adverbs of Manner"},
        {"corpus": "common_words_two", "group": "Qualitative Adjectives"},
    ],
    "level_14": [
        {"corpus": "nouns_four", "group": "Countries"},
        {"corpus": "nouns_four", "group": "Nationalities"},
        {"corpus": "nouns_four", "group": "Cities"},
        {"corpus": "nouns_four", "group": "Common Proper Nouns"},
        {"corpus": "nouns_three", "group": "Geographic Features"},
    ],
    "level_15": [
        {"corpus": "phrases_one", "group": "Asking for Directions"},
        {"corpus": "phrases_one", "group": "Transportation"},
        {"corpus": "phrases_one", "group": "Restaurant"},
        {"corpus": "phrases_one", "group": "Personal Comfort"},
    ],
}

def get_all_word_pairs_flat():
    """
    Creates a flat list of all word pairs from all corpora.
    
    Returns:
        list: A list of dictionaries, each containing 'english', 'lithuanian', 
              'corpus', and 'group' keys.
    """
    flat_words = []
    
    # Iterate through all corpora
    for corpus_name, corpus_data in all_words.items():
        # Iterate through all groups
        for group_name, word_pairs in corpus_data.items():
            # Add each word pair to the flat list with corpus information
            for word_pair in word_pairs:
                flat_word = word_pair.copy()  # Create a copy to avoid modifying the original
                flat_word['corpus'] = corpus_name
                flat_word['group'] = group_name
                flat_words.append(flat_word)
    
    return flat_words

def check_for_duplicates():
    """
    Checks for duplicate words in the wordlists.
    
    This function identifies four types of duplicates:
    1. Exact English duplicates - the same English word appears multiple times
    2. Semantic English duplicates - the same English word with different Lithuanian translations
       (potentially different meanings)
    3. Exact Lithuanian duplicates - the same Lithuanian word appears multiple times
    4. Semantic Lithuanian duplicates - the same Lithuanian word with different English translations
       (potentially different meanings)
    
    Returns:
        tuple: (english_exact_duplicates, english_semantic_duplicates, 
                lithuanian_exact_duplicates, lithuanian_semantic_duplicates)
            - english_exact_duplicates: A list of English words that appear multiple times
            - english_semantic_duplicates: A dictionary where keys are English words and values
              are lists of different Lithuanian translations
            - lithuanian_exact_duplicates: A list of Lithuanian words that appear multiple times
            - lithuanian_semantic_duplicates: A dictionary where keys are Lithuanian words and values
              are lists of different English translations
    """
    flat_words = get_all_word_pairs_flat()
    
    # Track English word occurrences and translations
    english_word_count = {}
    english_word_translations = {}
    
    # Track Lithuanian word occurrences and translations
    lithuanian_word_count = {}
    lithuanian_word_translations = {}
    
    # Find duplicates
    english_exact_duplicates = []
    english_semantic_duplicates = {}
    lithuanian_exact_duplicates = []
    lithuanian_semantic_duplicates = {}
    
    for word_pair in flat_words:
        english = word_pair['english']
        lithuanian = word_pair['lithuanian']
        
        # Track English word count
        if english in english_word_count:
            english_word_count[english] += 1
            if english_word_count[english] == 2:  # Only add to duplicates list once
                english_exact_duplicates.append(english)
        else:
            english_word_count[english] = 1
        
        # Track different Lithuanian translations for English words
        if english in english_word_translations:
            if lithuanian not in english_word_translations[english]:
                english_word_translations[english].append(lithuanian)
                # If we find a new translation, it's a semantic duplicate
                if len(english_word_translations[english]) == 2:  # Only add to semantic duplicates once
                    english_semantic_duplicates[english] = english_word_translations[english]
        else:
            english_word_translations[english] = [lithuanian]
        
        # Track Lithuanian word count
        if lithuanian in lithuanian_word_count:
            lithuanian_word_count[lithuanian] += 1
            if lithuanian_word_count[lithuanian] == 2:  # Only add to duplicates list once
                lithuanian_exact_duplicates.append(lithuanian)
        else:
            lithuanian_word_count[lithuanian] = 1
        
        # Track different English translations for Lithuanian words
        if lithuanian in lithuanian_word_translations:
            if english not in lithuanian_word_translations[lithuanian]:
                lithuanian_word_translations[lithuanian].append(english)
                # If we find a new translation, it's a semantic duplicate
                if len(lithuanian_word_translations[lithuanian]) == 2:  # Only add to semantic duplicates once
                    lithuanian_semantic_duplicates[lithuanian] = lithuanian_word_translations[lithuanian]
        else:
            lithuanian_word_translations[lithuanian] = [english]
    
    return english_exact_duplicates, english_semantic_duplicates, lithuanian_exact_duplicates, lithuanian_semantic_duplicates


def find_missing_words(input_words):
    """
    Find English words that are not already in the app's wordlists.
    
    Args:
        input_words: Either a list of words ["word1", "word2"] or a file path 
                    containing one word per line.
    
    Returns:
        list: A list of English words (in order) that are not found in any 
              of the app's wordlists.
    """
    # Get all existing English words from the app
    existing_words = set()
    flat_words = get_all_word_pairs_flat()
    for word_pair in flat_words:
        existing_words.add(word_pair['english'].lower())
    
    # Determine if input_words is a file path or a list
    if isinstance(input_words, str):
        # It's a file path
        try:
            with open(input_words, 'r', encoding='utf-8') as file:
                words_to_check = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {input_words}")
        except Exception as e:
            raise Exception(f"Error reading file {input_words}: {e}")
    elif isinstance(input_words, list):
        # It's a list of words
        words_to_check = input_words
    else:
        raise TypeError("input_words must be either a list of words or a file path string")
    
    # Find missing words (preserve order)
    missing_words = []
    for word in words_to_check:
        if word.lower() not in existing_words:
            missing_words.append(word)
    
    return missing_words


def find_lithuanian_words_not_in_audiobatches():
    """
    Find Lithuanian words from the app's wordlists that are NOT present in any 
    of the audiobatches text files.
    
    This function reads all .txt files in the audiobatches subdirectory and 
    compares them against all Lithuanian words in the app's wordlists to find
    which words from the app are missing from the audiobatches.
    
    Returns:
        list: A list of Lithuanian words from the app that are not found in any 
              audiobatches file.
    """
    import os
    import glob
    
    # Get all Lithuanian words from the app
    app_lithuanian_words = set()
    flat_words = get_all_word_pairs_flat()
    for word_pair in flat_words:
        app_lithuanian_words.add(word_pair['lithuanian'].lower())
    
    # Get the path to the audiobatches directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    audiobatches_dir = os.path.join(current_dir, 'audiobatches')
    
    # Read all words from all .txt files in audiobatches directory
    audiobatch_words = set()
    txt_files = glob.glob(os.path.join(audiobatches_dir, '*.txt'))
    
    for txt_file in txt_files:
        try:
            with open(txt_file, 'r', encoding='utf-8') as file:
                for line in file:
                    word = line.strip()
                    if word:  # Skip empty lines
                        audiobatch_words.add(word.lower())
        except Exception as e:
            print(f"Warning: Error reading file {txt_file}: {e}")
            continue
    
    # Find Lithuanian words from app that are NOT in any audiobatch file
    missing_from_audiobatches = []
    for lithuanian_word in sorted(app_lithuanian_words):
        if lithuanian_word not in audiobatch_words:
            missing_from_audiobatches.append(lithuanian_word)
    
    return missing_from_audiobatches
