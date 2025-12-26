# Spanish Vocabulary Lists

This directory contains Spanish vocabulary lists organized by CEFR levels and topics.

## Directories

### basic_a1_a2/
Basic Spanish vocabulary suitable for A1 and A2 level learners (Common European Framework of Reference).

- **Source**: [CodingFriends/basic-vocabulary-word-lists](https://github.com/CodingFriends/basic-vocabulary-word-lists)
- **License**: Check original repository for license information
- **Format**: CSV files with structure: `Spanish;English;;tags`

## Files in basic_a1_a2/

| File | Description | Word Count (approx) |
|------|-------------|---------------------|
| adjective.csv | Common adjectives | 20+ |
| color.csv | Color names | 10+ |
| communication.csv | Communication-related words | 15+ |
| food.csv | Food and dining vocabulary | 30+ |
| health.csv | Health and body-related terms | 20+ |
| numbers.csv | Numbers and counting | 20+ |
| orientation.csv | Direction and orientation | 15+ |
| personal-information.csv | Personal information vocabulary | 20+ |
| sentences.csv | Common phrases and sentences | 20+ |
| shopping.csv | Shopping-related vocabulary | 15+ |
| surrounding.csv | Environment and surroundings | 20+ |
| technology.csv | Technology terms | 10+ |
| time.csv | Time-related vocabulary | 25+ |
| transport.csv | Transportation vocabulary | 15+ |
| verb.csv | Common verbs | 30+ |

## Usage Examples

### Loading a CSV file in Python
```python
import csv

with open('basic_a1_a2/food.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        spanish, english, _, tags = row
        print(f"{english}: {spanish}")
```

### Using pandas
```python
import pandas as pd

# Read with custom delimiter
df = pd.read_csv('basic_a1_a2/verb.csv', sep=';', names=['Spanish', 'English', 'Extra', 'Tags'])
print(df[['Spanish', 'English']].head(10))
```

## CEFR Levels

**A1 (Beginner)**: Can understand and use familiar everyday expressions and very basic phrases.

**A2 (Elementary)**: Can understand sentences and frequently used expressions related to areas of most immediate relevance.

These word lists are suitable for learners at both A1 and A2 levels.

## Attribution

Please cite the original source when using these word lists:
- CodingFriends/basic-vocabulary-word-lists on GitHub
