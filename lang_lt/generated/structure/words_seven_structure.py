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

from ..dictionary.nationality_dictionary import *
from ..dictionary.personal_name_dictionary import *
from ..dictionary.place_name_dictionary import *
from ..dictionary.temporal_name_dictionary import *

words_seven_structure = {
  'Temporal Name': {
    "display_name": 'Temporal Name',
    "words": [N32_012, N32_010, N32_015, N32_013, N32_014, N32_011, N32_017, N32_016, N32_019, N32_008, N32_018, N32_009, N32_006, N32_005, N32_007, N32_001, N32_004, N32_002, N32_003]
  },
  'Place Name': {
    "display_name": 'Place Name',
    "words": [N30_014, N30_011, N30_006, N30_024, N30_023, N30_005, N30_015, N30_010, N30_009, N30_013, N30_025, N30_007, N30_008, N30_017, N30_012, N30_027, N30_029, N30_016, N30_004, N30_022, N30_031, N30_032, N30_018, N30_020, N30_019, N30_021, N30_026, N30_001, N30_002, N30_003, N30_028, N30_030, N30_033, N30_034, N30_035]
  },
  'Nationality': {
    "display_name": 'Nationality',
    "words": [N33_011, N33_010, N33_006, N33_014, N33_005, N33_009, N33_007, N33_013, N33_008, N33_004, N33_012, N33_015, N33_016, N33_001, N33_002, N33_003, N33_017]
  },
  'Personal Name': {
    "display_name": 'Personal Name',
    "words": [N29_001, N29_003, N29_002, N29_010, N29_011, N29_004, N29_005, N29_006, N29_007, N29_008, N29_009, N29_012, N29_013]
  },
}
