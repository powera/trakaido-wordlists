"""
Nouns Five - Category Structure

This file contains the organizational structure mapping categories to word objects.
Each category contains a list of word objects imported from the dictionary files.

Structure:
- Each category has a "display_name" for pretty printing
- Each category has a "words" list containing the actual word objects
- Word objects are imported from their respective dictionary files

Format: "Category": {
  "display_name": "Pretty Category Name",
  "words": [word_object1, word_object2, ...]
}
"""

from ..dictionary.concept_idea_dictionary import *
from ..dictionary.conjunction_other_dictionary import *
from ..dictionary.location_dictionary import *
from ..dictionary.pronoun_other_dictionary import *
from ..dictionary.quality_dictionary import *
from ..dictionary.style_dictionary import *

words_five_structure = {
  'Concept Idea': {
    "display_name": 'Concept Idea',
    "words": [N17_027, N17_019, N17_023, N17_022, N17_026, N17_028, N17_021, N17_020, N17_024, N17_025]
  },
  'Quality': {
    "display_name": 'Quality',
    "words": [A05_035, A05_046, A05_045, A05_040, A05_036, A05_038, A05_041, A05_044, A05_042, A05_037, A05_039, A05_047, A05_043]
  },
  'Conjunction Other': {
    "display_name": 'Conjunction Other',
    "words": [C99_001, C99_011, C99_008, C99_006, C99_017, C99_004, C99_009, C99_010, C99_003, C99_002, C99_007, C99_016, C99_015, C99_014, C99_012, C99_013, C99_005]
  },
  'Location': {
    "display_name": 'Location',
    "words": [D07_007, D07_001, D07_006, D07_003, D07_002, D07_004, D07_011, D07_010, D07_005, D07_008, D07_012, D07_009]
  },
  'Style': {
    "display_name": 'Style',
    "words": [D01_003, D01_009, D01_008, D01_010, D01_002, D01_001, D01_007, D01_006, D01_004, D01_005]
  },
  'Pronoun Other': {
    "display_name": 'Pronoun Other',
    "words": [P99_002, P99_004, P99_007, P99_001, P99_006, P99_003, P99_005, P99_008, P99_010, P99_009]
  },
}
