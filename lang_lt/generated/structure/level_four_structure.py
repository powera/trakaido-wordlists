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
from ..dictionary.emotion_feeling_dictionary import *
from ..dictionary.food_drink_dictionary import *
from ..dictionary.human_dictionary import *
from ..dictionary.material_substance_dictionary import *
from ..dictionary.natural_feature_dictionary import *
from ..dictionary.unit_of_measurement_dictionary import *

level_four_structure = {
  'Food Drink': {
    "display_name": 'Food Drink',
    "words": [N06_024, N06_029, N06_037, N06_043, N06_046, N06_050, N06_051, N06_052, N06_054, N06_055, N06_059, N06_064, N06_069, N06_070, N06_071, N06_075]
  },
  'Human': {
    "display_name": 'Human',
    "words": [N01_002, N01_030, N01_001, N01_025, N01_003, N01_018, N01_011, N01_005, N01_009, N01_010, N01_019, N01_004, N01_026, N01_016, N01_008, N01_022, N01_021, N01_029, N01_017, N01_024, N01_020, N01_012, N01_028, N01_014]
  },
  'Emotion Feeling': {
    "display_name": 'Emotion Feeling',
    "words": [N23_001, N23_005, N23_003, N23_007, N23_013, N23_010, N23_002, N23_009, N23_008, N23_006, N23_004, N23_020, N23_015, N23_011, N23_024, N23_016, N23_023, N23_014, N23_019, N23_022, N23_012, N23_021, N23_017]
  },
  'Unit Of Measurement': {
    "display_name": 'Unit Of Measurement',
    "words": [N34_002, N34_003, N34_005, N34_006, N34_007, N34_008, N34_010, N34_011]
  },
  'Natural Feature': {
    "display_name": 'Natural Feature',
    "words": [N11_017, N11_019]
  },
  'Body Part': {
    "display_name": 'Body Part',
    "words": [N03_018, N03_014, N03_001, N03_002, N03_030, N03_003, N03_027, N03_005, N03_011, N03_024, N03_026, N03_009, N03_004, N03_006, N03_010, N03_020, N03_008, N03_015, N03_028, N03_017, N03_019, N03_022, N03_029, N03_012, N03_016, N03_007, N03_013, N03_025, N03_023, N03_021]
  },
  'Material Substance': {
    "display_name": 'Material Substance',
    "words": [N14_005, N14_012, N14_015]
  },
}
