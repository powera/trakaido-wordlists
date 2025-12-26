# HSK (汉语水平考试) Chinese Vocabulary Lists

This directory contains comprehensive HSK (Hanyu Shuiping Kaoshi) vocabulary lists for Chinese language learning.

## Files

### hsk_complete.json
- **Source**: [drkameleon/complete-hsk-vocabulary](https://github.com/drkameleon/complete-hsk-vocabulary)
- **License**: MIT
- **Description**: Complete HSK 2.0 and HSK 3.0 vocabulary in JSON format
- **Size**: ~9.3 MB
- **Content**:
  - Simplified and traditional Chinese characters
  - Multiple transcription systems (Pinyin, Wade-Giles, Bopomofo, etc.)
  - English meanings
  - HSK levels (both old 1-6 and new 1-7+)
  - Part of speech tags
  - Frequency data
  - Classifiers

### hsk30.csv
- **Source**: [ivankra/hsk30](https://github.com/ivankra/hsk30)
- **License**: MIT (code), data from government sources
- **Description**: HSK 3.0 vocabulary list with 11,092 terms
- **Content**:
  - Simplified and traditional Chinese
  - Pinyin with diacritics
  - Part of speech tags
  - HSK 3.0 levels
  - Cross-references to CEDICT

## HSK Levels

### HSK 2.0 (Old System)
- Level 1: ~150 words
- Level 2: ~300 words total
- Level 3: ~600 words total
- Level 4: ~1,200 words total
- Level 5: ~2,500 words total
- Level 6: ~5,000 words total

### HSK 3.0 (New System)
- Levels 1-9 with 11,092 total vocabulary words
- More comprehensive and aligned with international standards

## Usage Examples

### Loading the JSON file
```python
import json

with open('hsk_complete.json', 'r', encoding='utf-8') as f:
    hsk_words = json.load(f)

# Find all HSK 1 words (old system)
hsk1_words = [w for w in hsk_words if 'old-1' in w['level']]
print(f"HSK 1 has {len(hsk1_words)} words")
```

### Loading the CSV file
```python
import pandas as pd

hsk30 = pd.read_csv('hsk30.csv')
level1_words = hsk30[hsk30['Level'] == 1]
print(f"HSK 3.0 Level 1 has {len(level1_words)} words")
```

## Attribution

Please cite the original sources when using these word lists:
- Complete HSK Vocabulary by drkameleon (MIT License)
- HSK 3.0 by ivankra (MIT License)
