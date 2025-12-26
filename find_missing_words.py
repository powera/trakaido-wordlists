#!/usr/bin/env python3
"""Find common missing words from the word frequency list."""

import json
import os
from pathlib import Path
from collections import defaultdict

# Load frequency list
with open('20th_books.json') as f:
    freq_data = json.load(f)
    word_freq = freq_data['global_word_frequency']

# Load all existing words from jsonl files
existing_words = set()
jsonl_dir = Path('jsonl')

for jsonl_file in jsonl_dir.rglob('base.jsonl'):
    with open(jsonl_file) as f:
        for line in f:
            if line.strip():
                entry = json.loads(line)
                existing_words.add(entry['concept_label'].lower())

# Words to exclude (declined forms, contractions, etc.)
exclude_patterns = {
    # Contractions
    "don't", "didn't", "doesn't", "won't", "wouldn't", "can't", "couldn't", "isn't", "wasn't", "weren't",
    "aren't", "haven't", "hasn't", "hadn't", "it's", "that's", "what's", "there's", "he's", "she's",
    "we're", "they're", "you're", "i'm", "we'll", "you'll", "they'll", "he'll", "she'll",
    "you've", "we've", "they've", "he'd", "she'd", "we'd", "you'd", "i've", "let's",
    # Possessives
    "his", "her", "their", "its", "my", "your", "our",
    # Declined verb forms (keep only if base form missing)
    "was", "were", "been", "had", "has", "did", "does",
    # Pronouns (basic ones)
    "i", "me", "he", "him", "she", "we", "us", "they", "them", "you", "it",
    # Articles
    "the", "a", "an",
    # Comparatives/superlatives (when base exists)
    "better", "best", "worse", "worst", "larger", "largest", "smaller", "smallest",
    # Common plurals when singular exists
    "men", "women", "children", "people", "eyes", "hands", "feet", "days", "years", "times",
    "things", "words", "trees", "animals", "horses", "books", "friends", "walls", "places",
    "fields", "hills", "mountains", "ships", "boys", "houses", "lights", "ways", "doors",
    "stones", "clouds", "guards", "creatures", "wings", "voices", "heads", "faces", "teeth",
    "ears", "fingers", "lives", "rabbits", "shadows", "leaves", "miles", "stars", "names",
    "arms", "legs", "sounds", "questions", "steps", "lands", "horses", "rocks", "orders",
    # Past tense when base exists
    "went", "came", "said", "made", "took", "gave", "saw", "knew", "thought", "felt",
    "looked", "turned", "stood", "began", "told", "asked", "seemed", "passed", "fell",
    "spoke", "held", "answered", "cried", "moved", "brought", "called", "ran", "stopped",
    "walked", "tried", "reached", "followed", "caught", "started", "opened", "kept",
    "sent", "grew", "watched", "appeared", "returned", "killed", "learned", "laughed",
    "carried", "filled", "decided", "remembered", "waited", "showed", "met", "died",
    "broke", "changed", "smiled", "lifted", "whispered", "dropped", "continued", "pulled",
    "touched", "picked", "noticed", "stepped", "finished", "shouted", "raised", "lived",
    "rode", "added", "pointed", "worked", "climbed", "crossed", "laid", "fallen", "pushed",
    "struck", "covered", "entered", "hung", "ended", "rolled", "slipped", "spent", "destroyed",
    "vanished", "talked", "pressed", "wore", "built",
    # Present participles when base exists
    "going", "looking", "coming", "doing", "trying", "standing", "running", "moving",
    "thinking", "waiting", "making", "talking", "sitting", "lying", "turning", "fighting",
    "leaving", "walking", "listening", "holding", "seeing", "speaking", "passing", "rising",
    "telling", "knowing", "using", "living", "having", "being", "getting", "taking",
    "saying", "watching", "working", "falling", "growing", "following", "staring",
    # Adverbs when adjective exists
    "slowly", "quickly", "quietly", "certainly", "exactly", "immediately", "completely",
    "carefully", "surely", "obviously", "especially", "gently", "swiftly",
    # Special cases
    "himself", "herself", "themselves", "itself", "myself", "yourself",
    "someone", "anyone", "everyone", "nobody", "nothing", "something", "anything", "everything",
    "somewhere", "anywhere", "everywhere", "nowhere",
    "merry", "warren", "al",  # Proper names that slipped in
}

# Find missing common words
missing = []
for word, freq in word_freq.items():
    word_lower = word.lower()
    if (word_lower not in existing_words and
        word_lower not in exclude_patterns and
        "'" not in word and  # Skip contractions
        len(word) > 1):  # Skip single letters
        missing.append((word_lower, freq))

# Sort by frequency
missing_sorted = sorted(missing, key=lambda x: x[1], reverse=True)

# Take top 1000
top_missing = missing_sorted[:1000]

# Print results
print("Top missing common words by frequency:")
print("=" * 60)
for i, (word, freq) in enumerate(top_missing[:100], 1):
    print(f"{i:3d}. {word:20s} (freq: {freq})")
