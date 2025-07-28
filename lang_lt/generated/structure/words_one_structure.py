"""
Nouns One - Category Structure

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
from ..dictionary.building_structure_dictionary import *
from ..dictionary.clothing_accessory_dictionary import *
from ..dictionary.color_dictionary import *
from ..dictionary.food_drink_dictionary import *
from ..dictionary.plant_dictionary import *
from ..dictionary.small_movable_object_dictionary import *
from ..dictionary.tool_machine_dictionary import *

words_one_structure = {
  'Food Drink': {
    "display_name": 'Food Drink',
    "words": [N06_002, N06_001, N06_008, N06_012, N06_013, N06_007, N06_003, N06_006, N06_004, N06_011, N06_009, N06_005, N06_022, N06_010, N06_017, N06_015, N06_020, N06_021, N06_014, N06_023, N06_019, N06_018, N06_016]
  },
  'Animal': {
    "display_name": 'Animal',
    "words": [N02_004, N02_001, N02_009, N02_003, N02_002, N02_007, N02_008, N02_005, N02_010, N02_006]
  },
  'Plant': {
    "display_name": 'Plant',
    "words": [N05_001, N05_005, N05_003, N05_006, N05_002, N05_004]
  },
  'Clothing Accessory': {
    "display_name": 'Clothing Accessory',
    "words": [N09_003, N09_008, N09_004, N09_006, N09_001, N09_010, N09_005, N09_002, N09_009, N09_012, N09_007, N09_011]
  },
  'Small Movable Object': {
    "display_name": 'Small Movable Object',
    "words": [N08_005, N08_003, N08_014, N08_008, N08_013, N08_006, N08_018, N08_007, N08_009, N08_004, N08_012, N08_016, N08_002, N08_001, N08_017, N08_010, N08_015, N08_011]
  },
  'Building Structure': {
    "display_name": 'Building Structure',
    "words": [N07_001, N07_002, N07_004, N07_008, N07_003, N07_009, N07_005, N07_007, N07_010, N07_006, N07_011]
  },
  'Tool Machine': {
    "display_name": 'Tool Machine',
    "words": [N12_007, N12_001, N12_006, N12_003, N12_002, N12_009, N12_005, N12_008, N12_004, N12_010]
  },
  'Color': {
    "display_name": 'Color',
    "words": [A02_002, A02_001, A02_003, A02_005, A02_007, A02_004, A02_006, A02_008]
  },
}
