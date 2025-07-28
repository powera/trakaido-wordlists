#!/usr/bin/python3

"""Wordlists for Trakaido, a language learning app for Lithuanian."""

from .nouns_enhanced import *
from .verbs import *
from .phrases import *
from .levels import levels

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

