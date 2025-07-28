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

from ..dictionary.noun_other_dictionary import *
from ..dictionary.quality_dictionary import *

words_three_structure = {
  'Quality': {
    "display_name": 'Quality',
    "words": [A05_015, A05_021, A05_018, A05_019, A05_030, A05_031, A05_032, A05_017, A05_020, A05_024, A05_022, A05_016, A05_025, A05_034, A05_029, A05_023, A05_026, A05_028, A05_027, A05_033]
  },
  'Noun Other': {
    "display_name": 'Noun Other',
    "words": [N99_045, N99_026, N99_063, N99_042, N99_075, N99_025, N99_027, N99_046, N99_103, N99_048, N99_031, N99_073, N99_038, N99_037, N99_076, N99_041, N99_050, N99_043, N99_049, N99_039, N99_034, N99_062, N99_028, N99_064, N99_036, N99_074, N99_057, N99_052, N99_047, N99_068, N99_078, N99_100, N99_056, N99_067, N99_091, N99_061, N99_040, N99_053, N99_098, N99_084, N99_081, N99_044, N99_090, N99_077, N99_085, N99_065, N99_058, N99_066, N99_079, N99_093, N99_055, N99_099, N99_060, N99_059, N99_083, N99_035, N99_080, N99_088, N99_082, N99_094, N99_106, N99_086, N99_069, N99_029, N99_092, N99_087, N99_105, N99_101, N99_070, N99_095, N99_089, N99_051, N99_054, N99_104, N99_033, N99_071, N99_097, N99_102, N99_072, N99_032, N99_096, N99_107, N99_030]
  },
}
