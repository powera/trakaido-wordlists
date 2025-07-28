#!/usr/bin/python3

"""Wordlists for Trakaido, a language learning app for Lithuanian."""

import os
import importlib.util
from typing import Dict, List, Any, Optional
from .levels import levels

class WordListManager:
    """
    Manages word lists using the enhanced directory structure.
    
    This class lazily loads dictionary files from enhanced/dictionary/ and
    structure files from enhanced/structure/, then compiles word lists by
    matching GUIDs to dictionary entries.
    """
    
    def __init__(self):
        self._dictionary_cache: Dict[str, Dict[str, Any]] = {}
        self._structure_cache: Dict[str, Dict[str, List[str]]] = {}
        self._compiled_cache: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        
        # Get the directory path for enhanced files
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.enhanced_dir = os.path.join(current_dir, 'enhanced')
        self.dictionary_dir = os.path.join(self.enhanced_dir, 'dictionary')
        self.structure_dir = os.path.join(self.enhanced_dir, 'structure')
    
    def _load_dictionary_file(self, filename: str) -> Dict[str, Any]:
        """Load a dictionary file and return all GUID entries."""
        if filename in self._dictionary_cache:
            return self._dictionary_cache[filename]
        
        file_path = os.path.join(self.dictionary_dir, filename)
        if not os.path.exists(file_path):
            return {}
        
        # Load the module dynamically
        spec = importlib.util.spec_from_file_location(f"dict_{filename[:-3]}", file_path)
        if spec is None or spec.loader is None:
            return {}
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Extract all GUID entries (variables that start with N, V, P, etc.)
        guid_entries = {}
        for attr_name in dir(module):
            if attr_name.startswith(('N', 'V', 'P')) and not attr_name.startswith('_'):
                attr_value = getattr(module, attr_name)
                if isinstance(attr_value, dict) and 'guid' in attr_value:
                    guid_entries[attr_name] = attr_value
        
        self._dictionary_cache[filename] = guid_entries
        return guid_entries
    
    def _load_structure_file(self, filename: str) -> Dict[str, List[str]]:
        """Load a structure file and return the structure mapping."""
        if filename in self._structure_cache:
            return self._structure_cache[filename]
        
        file_path = os.path.join(self.structure_dir, filename)
        if not os.path.exists(file_path):
            return {}
        
        # Load the module dynamically
        spec = importlib.util.spec_from_file_location(f"struct_{filename[:-3]}", file_path)
        if spec is None or spec.loader is None:
            return {}
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Find the structure variable (should be named like "nouns_one_structure")
        structure_data = {}
        for attr_name in dir(module):
            if attr_name.endswith('_structure') and not attr_name.startswith('_'):
                structure_data = getattr(module, attr_name, {})
                break
        
        self._structure_cache[filename] = structure_data
        return structure_data
    
    def _get_all_dictionary_entries(self) -> Dict[str, Any]:
        """Load all dictionary entries from all dictionary files."""
        all_entries = {}
        
        if not os.path.exists(self.dictionary_dir):
            return all_entries
        
        # Load all dictionary files
        for filename in os.listdir(self.dictionary_dir):
            if filename.endswith('_dictionary.py'):
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

# Legacy compatibility - load from enhanced structure for nouns
def _get_enhanced_nouns():
    """Get noun corpora from enhanced structure."""
    enhanced_nouns = {}
    for corpus_name in ["nouns_one", "nouns_two", "nouns_three", "nouns_four", "nouns_five"]:
        enhanced_nouns[corpus_name] = _word_manager.get_corpus(corpus_name)
    return enhanced_nouns

# Load enhanced nouns
_enhanced_nouns = _get_enhanced_nouns()

# Import legacy data for non-noun corpora (until they're migrated)
from .verbs import *
from .phrases import *

# Try to get common_words from enhanced structure, fall back to legacy
try:
    common_words = _word_manager.get_corpus("common_words")
    common_words_two = _word_manager.get_corpus("common_words_two")
except:
    # Fall back to legacy imports if enhanced structure doesn't exist yet
    try:
        from .nouns_enhanced import common_words, common_words_two
    except ImportError:
        common_words = {}
        common_words_two = {}

all_words = {
  "nouns_one": _enhanced_nouns.get("nouns_one", {}),
  "nouns_two": _enhanced_nouns.get("nouns_two", {}),
  "nouns_three": _enhanced_nouns.get("nouns_three", {}),
  "nouns_four": _enhanced_nouns.get("nouns_four", {}),
  "nouns_five": _enhanced_nouns.get("nouns_five", {}),
  "common_words": common_words,
  "common_words_two": common_words_two,
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

