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
from ..dictionary.human_dictionary import *
from ..dictionary.natural_feature_dictionary import *
from ..dictionary.quality_dictionary import *
from ..dictionary.tool_machine_dictionary import *

level_six_structure = {
  'Tool Machine': {
    "display_name": 'Tool Machine',
    "words": [N12_012, N12_014, N12_016, N12_018, N12_023, N12_024, N12_027, N12_029, N12_030, N12_032, N12_035]
  },
  'Human': {
    "display_name": 'Human',
    "words": [N01_051, N01_052]
  },
  'Natural Feature': {
    "display_name": 'Natural Feature',
    "words": [N11_032]
  },
  'Concept Idea': {
    "display_name": 'Concept Idea',
    "words": [N17_009, N17_011]
  },
  'Quality': {
    "display_name": 'Quality',
    "words": [A05_008, A05_012]
  },
}
