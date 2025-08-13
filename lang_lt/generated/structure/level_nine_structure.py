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

from ..dictionary.emotion_feeling_dictionary import *
from ..dictionary.quality_dictionary import *
from ..dictionary.sequence_dictionary import *
from ..dictionary.small_movable_object_dictionary import *

level_nine_structure = {
  'Small Movable Object': {
    "display_name": 'Small Movable Object',
    "words": [N08_014, N08_008, N08_013, N08_019, N08_020, N08_021, N08_022, N08_023, N08_024, N08_025, N08_026]
  },
  'Emotion Feeling': {
    "display_name": 'Emotion Feeling',
    "words": [N23_013, N23_010, N23_009, N23_008, N23_015, N23_024, N23_016, N23_023, N23_014, N23_019, N23_012, N23_017, N23_018]
  },
  'Quality': {
    "display_name": 'Quality',
    "words": [A05_015, A05_021, A05_018, A05_019, A05_030, A05_031, A05_032, A05_017, A05_020, A05_024, A05_022, A05_016, A05_025, A05_034, A05_029, A05_023, A05_026, A05_028, A05_027, A05_033, A05_008, A05_012]
  },
  'Sequence': {
    "display_name": 'Sequence',
    "words": [A15_001, A15_002, A15_003, A15_004, A15_005, A15_006, A15_007, A15_008, A15_009, A15_010]
  },
}
