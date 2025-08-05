"""
Nouns Twelve - Category Structure

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

from ..dictionary.time_period_dictionary import *

level_twelve_structure = {
  'Time Period': {
    "display_name": 'Time Period',
    "words": [N25_002, N25_018, N25_001, N25_003, N25_007, N25_014, N25_013, N25_017, N25_019, N25_015, N25_010, N25_004, N25_012, N25_016, N25_020, N25_011, N25_005, N25_009, N25_008, N25_006]
  },
}
