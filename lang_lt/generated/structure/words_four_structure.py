"""
Nouns Four - Category Structure

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

from ..dictionary.body_part_dictionary import *
from ..dictionary.food_drink_dictionary import *
from ..dictionary.material_substance_dictionary import *
from ..dictionary.natural_feature_dictionary import *
from ..dictionary.unit_of_measurement_dictionary import *

words_four_structure = {
  'Food Drink': {
    "display_name": 'Food Drink',
    "words": [N06_039, N06_038, N06_066, N06_030, N06_076, N06_028, N06_042, N06_040, N06_077, N06_074, N06_073, N06_068, N06_036, N06_033, N06_078, N06_060, N06_062, N06_031, N06_041, N06_061, N06_079, N06_048, N06_049, N06_026, N06_058, N06_027, N06_063, N06_045, N06_053, N06_083, N06_065, N06_035, N06_082, N06_044, N06_057, N06_067, N06_056, N06_047, N06_081, N06_032, N06_080, N06_072, N06_025, N06_034, N06_024, N06_029, N06_037, N06_043, N06_046, N06_050, N06_051, N06_052, N06_054, N06_055, N06_059, N06_064, N06_069, N06_070, N06_071, N06_075]
  },
  'Unit Of Measurement': {
    "display_name": 'Unit Of Measurement',
    "words": [N34_009, N34_004, N34_001, N34_002, N34_003, N34_005, N34_006, N34_007, N34_008, N34_010, N34_011]
  },
  'Natural Feature': {
    "display_name": 'Natural Feature',
    "words": [N11_007, N11_004, N11_010, N11_006, N11_002, N11_001, N11_012, N11_005, N11_003, N11_009, N11_016, N11_008, N11_015, N11_011, N11_014, N11_018, N11_013, N11_017, N11_019]
  },
  'Body Part': {
    "display_name": 'Body Part',
    "words": [N03_018, N03_014, N03_001, N03_002, N03_030, N03_003, N03_027, N03_005, N03_011, N03_024, N03_026, N03_009, N03_004, N03_006, N03_010, N03_020, N03_008, N03_015, N03_028, N03_017, N03_019, N03_022, N03_029, N03_012, N03_016, N03_007, N03_013, N03_025, N03_023, N03_021]
  },
  'Material Substance': {
    "display_name": 'Material Substance',
    "words": [N14_018, N14_011, N14_007, N14_003, N14_008, N14_001, N14_024, N14_002, N14_004, N14_013, N14_016, N14_009, N14_006, N14_017, N14_010, N14_014, N14_021, N14_019, N14_023, N14_020, N14_022, N14_005, N14_012, N14_015]
  },
}
