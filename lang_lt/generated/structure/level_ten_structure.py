"""
Nouns Ten - Category Structure

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

from ..dictionary.animal_dictionary import *
from ..dictionary.location_dictionary import *
from ..dictionary.style_dictionary import *

level_ten_structure = {
  'Animal': {
    "display_name": 'Animal',
    "words": [N02_011, N02_012, N02_013, N02_014, N02_015, N02_016]
  },
  'Location': {
    "display_name": 'Location',
    "words": [D07_007, D07_001, D07_006, D07_003, D07_002, D07_004, D07_011, D07_010, D07_005, D07_008, D07_012, D07_009]
  },
  'Style': {
    "display_name": 'Style',
    "words": [D01_003, D01_009, D01_008, D01_010, D01_002, D01_001, D01_007, D01_006, D01_004, D01_005]
  },
}
