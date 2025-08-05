"""
Nouns Thirteen - Category Structure

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

from ..dictionary.concept_idea_dictionary import *
from ..dictionary.place_name_dictionary import *

level_thirteen_structure = {
  'Place Name': {
    "display_name": 'Place Name',
    "words": [N30_036, N30_037, N30_039, N30_041, N30_040, N30_053, N30_048, N30_043, N30_038, N30_047, N30_052, N30_044, N30_049, N30_046, N30_051, N30_050, N30_042, N30_045]
  },
  'Concept Idea': {
    "display_name": 'Concept Idea',
    "words": [N17_016, N17_001, N17_002, N17_003, N17_018, N17_005, N17_007, N17_004, N17_006, N17_008, N17_015, N17_010, N17_017, N17_013, N17_014, N17_012]
  },
}
