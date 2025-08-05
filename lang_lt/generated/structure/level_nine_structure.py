"""
Nouns Nine - Category Structure

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
from ..dictionary.quality_dictionary import *

level_nine_structure = {
  'Concept Idea': {
    "display_name": 'Concept Idea',
    "words": [N17_021, N17_049, N17_062, N17_019, N17_022, N17_054, N17_020, N17_024, N17_046, N17_037, N17_058, N17_044, N17_030, N17_027, N17_036, N17_023, N17_031, N17_025, N17_039, N17_045, N17_029, N17_026, N17_034, N17_028, N17_057, N17_040, N17_052, N17_032, N17_038, N17_033, N17_051, N17_047, N17_041, N17_035, N17_050, N17_061, N17_063, N17_043, N17_048, N17_056, N17_055, N17_042, N17_059, N17_060, N17_053]
  },
  'Quality': {
    "display_name": 'Quality',
    "words": [A05_015, A05_021, A05_018, A05_019, A05_030, A05_031, A05_032, A05_017, A05_020, A05_024, A05_022, A05_016, A05_025, A05_034, A05_029, A05_023, A05_026, A05_028, A05_027, A05_033]
  },
}
