"""
Nouns Three - Category Structure

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

from ..dictionary.color_dictionary import *
from ..dictionary.definite_quantity_dictionary import *
from ..dictionary.shape_dictionary import *

level_three_structure = {
  'Color': {
    "display_name": 'Color',
    "words": [A02_002, A02_001, A02_003, A02_005, A02_007, A02_004, A02_006, A02_008]
  },
  'Definite Quantity': {
    "display_name": 'Definite Quantity',
    "words": [A11_002, A11_003, A11_004, A11_005, A11_006, A11_007, A11_011, A11_021, A11_009, A11_008, A11_010, A11_022, A11_013, A11_023, A11_016, A11_024, A11_001, A11_012, A11_025, A11_015, A11_019, A11_017, A11_026, A11_027, A11_014, A11_028, A11_018]
  },
  'Shape': {
    "display_name": 'Shape',
    "words": [A03_002, A03_001, A03_007, A03_004, A03_008, A03_010, A03_009, A03_006, A03_012]
  },
}
