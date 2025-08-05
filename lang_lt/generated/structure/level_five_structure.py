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

from ..dictionary.human_dictionary import *
from ..dictionary.material_substance_dictionary import *
from ..dictionary.pronoun_other_dictionary import *
from ..dictionary.unit_of_measurement_dictionary import *

level_five_structure = {
  'Human': {
    "display_name": 'Human',
    "words": [N01_055, N01_056, N01_060, N01_059, N01_057, N01_058, N01_061, N01_062, N01_063, N01_064]
  },
  'Unit Of Measurement': {
    "display_name": 'Unit Of Measurement',
    "words": [N34_009, N34_004, N34_001]
  },
  'Material Substance': {
    "display_name": 'Material Substance',
    "words": [N14_018, N14_011, N14_007, N14_003, N14_008, N14_001, N14_024, N14_002, N14_004, N14_013, N14_016, N14_009, N14_006, N14_017, N14_010, N14_014, N14_021, N14_019, N14_023, N14_020, N14_022]
  },
  'Pronoun Other': {
    "display_name": 'Pronoun Other',
    "words": [P99_009]
  },
}
