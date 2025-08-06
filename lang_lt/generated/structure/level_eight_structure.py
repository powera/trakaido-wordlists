"""
Nouns Eight - Category Structure

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
from ..dictionary.clothing_accessory_dictionary import *
from ..dictionary.human_dictionary import *
from ..dictionary.material_substance_dictionary import *
from ..dictionary.natural_feature_dictionary import *
from ..dictionary.pronoun_other_dictionary import *
from ..dictionary.tool_machine_dictionary import *

level_eight_structure = {
  'Clothing Accessory': {
    "display_name": 'Clothing Accessory',
    "words": [N09_004, N09_010]
  },
  'Tool Machine': {
    "display_name": 'Tool Machine',
    "words": [N12_011, N12_021, N12_033, N12_020, N12_019, N12_034, N12_026, N12_015, N12_025, N12_017, N12_028, N12_022, N12_031, N12_013, N12_012, N12_014, N12_016, N12_018, N12_023, N12_024, N12_027, N12_029, N12_030, N12_032, N12_035]
  },
  'Human': {
    "display_name": 'Human',
    "words": [N01_033, N01_031, N01_032, N01_036, N01_040, N01_034, N01_037, N01_035, N01_038, N01_039, N01_047, N01_048, N01_041, N01_043, N01_049, N01_054, N01_044, N01_053, N01_050, N01_045, N01_042, N01_046, N01_051, N01_052]
  },
  'Natural Feature': {
    "display_name": 'Natural Feature',
    "words": [N11_007, N11_004, N11_010, N11_006, N11_002, N11_001, N11_012, N11_005, N11_003, N11_009, N11_016, N11_008, N11_015, N11_011, N11_014, N11_018, N11_013, N11_017, N11_019, N11_032]
  },
  'Body Part': {
    "display_name": 'Body Part',
    "words": [N03_018, N03_001, N03_002, N03_026, N03_009, N03_010, N03_008, N03_017, N03_019, N03_012, N03_007, N03_013, N03_025, N03_023, N03_021]
  },
  'Material Substance': {
    "display_name": 'Material Substance',
    "words": [N14_018, N14_011, N14_007, N14_003, N14_008, N14_001, N14_024, N14_002, N14_004, N14_013, N14_016, N14_009, N14_006, N14_017, N14_010, N14_014, N14_021, N14_019, N14_023, N14_020, N14_022, N14_005, N14_012, N14_015]
  },
  'Pronoun Other': {
    "display_name": 'Pronoun Other',
    "words": [P99_002, P99_004, P99_007, P99_001, P99_006, P99_003, P99_005, P99_008, P99_010, P99_009]
  },
}
