# German Vocabulary Lists

This directory contains German vocabulary lists organized by CEFR levels and topics.

## Directories

### basic_a1_a2/
Basic German vocabulary suitable for A1 and A2 level learners (Common European Framework of Reference).

- **Source**: [CodingFriends/basic-vocabulary-word-lists](https://github.com/CodingFriends/basic-vocabulary-word-lists)
- **Format**: CSV files with structure: `German;English;;tags`
- **Level**: A1-A2 (Beginner to Elementary)

### goethe_a1_b1/
Official Goethe-Institut vocabulary stems for A1, A2, and B1 levels.

- **Source**: [technologiestiftung/sprach-o-mat](https://github.com/technologiestiftung/sprach-o-mat)
- **Format**: CSV with columns: ID, Level, Stem
- **Levels**: A1, A2, B1
- **Content**: Word stems from official Goethe-Institut certification materials

### frequency_lists/
Frequency-based German vocabulary lists.

- **Source**: [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords)
- **Format**: TXT files with format: `word frequency_count`
- **Content**: Top 50,000 most common German words from OpenSubtitles corpus

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

### Loading basic vocabulary (CSV)
```python
import csv

with open('basic_a1_a2/food.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        german, english, _, tags = row
        print(f"{english}: {german}")
```

### Loading Goethe stems
```python
import pandas as pd

df = pd.read_csv('goethe_a1_b1/dictionary_stems.csv')
a1_words = df[df['level'] == 'A1']
print(f"A1 level has {len(a1_words)} word stems")
```

### Loading frequency list
```python
with open('frequency_lists/hermitdave_50k.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i >= 100:  # Top 100 words
            break
        word, freq = line.strip().split()
        print(f"{i+1}. {word} ({freq} occurrences)")
```

## CEFR Levels

**A1 (Beginner)**: Can understand and use familiar everyday expressions and very basic phrases.

**A2 (Elementary)**: Can understand sentences and frequently used expressions related to areas of most immediate relevance.

**B1 (Intermediate)**: Can understand the main points of clear standard input on familiar matters regularly encountered.

**B2 (Upper Intermediate)**: Can understand the main ideas of complex text on both concrete and abstract topics.

**C1 (Advanced)**: Can understand a wide range of demanding, longer texts, and recognize implicit meaning.

**C2 (Proficiency)**: Can understand with ease virtually everything heard or read.

## Attribution

Please cite the original sources when using these word lists:
- CodingFriends/basic-vocabulary-word-lists on GitHub
- technologiestiftung/sprach-o-mat (Goethe-Institut materials)
- hermitdave/FrequencyWords (OpenSubtitles corpus)
