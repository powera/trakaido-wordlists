"""
Nouns Eleven - Category Structure

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

from ..dictionary.conjunction_other_dictionary import *
from ..dictionary.quality_dictionary import *
from ..dictionary.temporal_name_dictionary import *

level_eleven_structure = {
  'Temporal Name': {
    "display_name": 'Temporal Name',
    "words": [N32_012, N32_010, N32_015, N32_013, N32_014, N32_011, N32_017, N32_016, N32_019, N32_008, N32_018, N32_009, N32_006, N32_005, N32_007, N32_001, N32_004, N32_002, N32_003]
  },
  'Quality': {
    "display_name": 'Quality',
    "words": [A05_035, A05_046, A05_001, A05_045, A05_040, A05_036, A05_038, A05_041, A05_044, A05_042, A05_037, A05_003, A05_039, A05_047, A05_006, A05_002, A05_043, A05_011, A05_009, A05_005, A05_014, A05_013, A05_004, A05_007, A05_010]
  },
  'Conjunction Other': {
    "display_name": 'Conjunction Other',
    "words": [C99_001, C99_011, C99_008, C99_006, C99_017, C99_004, C99_009, C99_010, C99_003, C99_002, C99_007, C99_016, C99_015, C99_014, C99_012, C99_013, C99_005]
  },
}
