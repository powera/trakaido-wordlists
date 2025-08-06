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

from ..dictionary.food_drink_dictionary import *
from ..dictionary.human_dictionary import *
from ..dictionary.plant_dictionary import *

level_five_structure = {
  'Food Drink': {
    "display_name": 'Food Drink',
    "words": [N06_024, N06_029, N06_037, N06_043, N06_046, N06_050, N06_051, N06_052, N06_054, N06_055, N06_059, N06_064, N06_069, N06_070, N06_071, N06_075]
  },
  'Plant': {
    "display_name": 'Plant',
    "words": [N05_001, N05_005, N05_003, N05_006, N05_002, N05_004]
  },
  'Human': {
    "display_name": 'Human',
    "words": [N01_055, N01_056, N01_060, N01_059, N01_057, N01_058, N01_061, N01_062, N01_063, N01_002, N01_064, N01_030, N01_001, N01_025, N01_003, N01_018, N01_011, N01_005, N01_009, N01_010, N01_019, N01_004, N01_026, N01_016, N01_008, N01_022, N01_021, N01_029, N01_017, N01_024, N01_020, N01_012, N01_028, N01_014, N01_006, N01_007, N01_013, N01_015, N01_023, N01_027]
  },
}
