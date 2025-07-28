"""
Nouns Two - Category Structure

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

from ..dictionary.definite_quantity_dictionary import *
from ..dictionary.emotion_feeling_dictionary import *
from ..dictionary.human_dictionary import *
from ..dictionary.shape_dictionary import *

words_two_structure = {
  'Human': {
    "display_name": 'Human',
    "words": [N01_002, N01_030, N01_001, N01_025, N01_003, N01_018, N01_011, N01_005, N01_009, N01_010, N01_019, N01_004, N01_026, N01_016, N01_008, N01_022, N01_021, N01_029, N01_017, N01_024, N01_020, N01_012, N01_028, N01_014, N01_006, N01_007, N01_013, N01_015, N01_023, N01_027]
  },
  'Definite Quantity': {
    "display_name": 'Definite Quantity',
    "words": [A11_002, A11_003, A11_004, A11_005, A11_006, A11_007, A11_011, A11_021, A11_009, A11_008, A11_010, A11_022, A11_013, A11_023, A11_016, A11_024, A11_001, A11_012, A11_025, A11_015, A11_019, A11_017, A11_026, A11_027, A11_014, A11_028, A11_018, A11_020, A11_029, A11_030]
  },
  'Shape': {
    "display_name": 'Shape',
    "words": [A03_002, A03_001, A03_007, A03_004, A03_008, A03_010, A03_009, A03_006, A03_012, A03_003, A03_005, A03_011, A03_013]
  },
  'Emotion Feeling': {
    "display_name": 'Emotion Feeling',
    "words": [N23_001, N23_005, N23_003, N23_007, N23_013, N23_010, N23_002, N23_009, N23_008, N23_006, N23_004, N23_020, N23_015, N23_011, N23_024, N23_016, N23_023, N23_014, N23_019, N23_022, N23_012, N23_021, N23_017, N23_018]
  },
}
