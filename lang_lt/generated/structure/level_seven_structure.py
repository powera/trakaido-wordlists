"""
Nouns Seven - Category Structure

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

from ..dictionary.building_structure_dictionary import *
from ..dictionary.food_drink_dictionary import *
from ..dictionary.nationality_dictionary import *
from ..dictionary.personal_name_dictionary import *
from ..dictionary.place_name_dictionary import *

level_seven_structure = {
  'Food Drink': {
    "display_name": 'Food Drink',
    "words": [N06_008, N06_011, N06_009, N06_039, N06_022, N06_010, N06_017, N06_038, N06_066, N06_030, N06_076, N06_028, N06_042, N06_023, N06_019, N06_040, N06_077, N06_074, N06_073, N06_068, N06_036, N06_033, N06_078, N06_060, N06_062, N06_031, N06_041, N06_061, N06_079, N06_048, N06_049, N06_026, N06_058, N06_027, N06_063, N06_045, N06_053, N06_083, N06_065, N06_035, N06_082, N06_044, N06_057, N06_067, N06_056, N06_047, N06_081, N06_032, N06_080, N06_072, N06_025, N06_034]
  },
  'Building Structure': {
    "display_name": 'Building Structure',
    "words": [N07_004]
  },
  'Place Name': {
    "display_name": 'Place Name',
    "words": [N30_001, N30_002, N30_003, N30_028, N30_030, N30_033, N30_034, N30_035]
  },
  'Nationality': {
    "display_name": 'Nationality',
    "words": [N33_001, N33_002, N33_003, N33_017]
  },
  'Personal Name': {
    "display_name": 'Personal Name',
    "words": [N29_004, N29_005, N29_006, N29_007, N29_008, N29_009, N29_012, N29_013]
  },
}
