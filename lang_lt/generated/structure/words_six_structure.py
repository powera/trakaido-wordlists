"""
Nouns Six - Category Structure

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
from ..dictionary.natural_feature_dictionary import *
from ..dictionary.noun_other_dictionary import *
from ..dictionary.quality_dictionary import *
from ..dictionary.tool_machine_dictionary import *

words_six_structure = {
  'Tool Machine': {
    "display_name": 'Tool Machine',
    "words": [N12_011, N12_021, N12_033, N12_020, N12_019, N12_034, N12_026, N12_015, N12_025, N12_017, N12_028, N12_022, N12_031, N12_013, N12_012, N12_014, N12_016, N12_018, N12_023, N12_024, N12_027, N12_029, N12_030, N12_032, N12_035]
  },
  'Natural Feature': {
    "display_name": 'Natural Feature',
    "words": [N11_021, N11_027, N11_030, N11_022, N11_020, N11_023, N11_025, N11_031, N11_026, N11_028, N11_024, N11_029, N11_032]
  },
  'Concept Idea': {
    "display_name": 'Concept Idea',
    "words": [N17_016, N17_001, N17_002, N17_003, N17_018, N17_005, N17_007, N17_004, N17_006, N17_008, N17_015, N17_010, N17_017, N17_013, N17_014, N17_012, N17_009, N17_011]
  },
  'Quality': {
    "display_name": 'Quality',
    "words": [A05_001, A05_003, A05_006, A05_002, A05_011, A05_009, A05_005, A05_014, A05_013, A05_004, A05_007, A05_010, A05_008, A05_012]
  },
  'Noun Other': {
    "display_name": 'Noun Other',
    "words": [N99_003, N99_001, N99_002, N99_006, N99_010, N99_004, N99_007, N99_005, N99_008, N99_009, N99_017, N99_018, N99_011, N99_013, N99_019, N99_024, N99_014, N99_023, N99_020, N99_015, N99_012, N99_016, N99_021, N99_022]
  },
}
