# Spanish Vocabulary Lists

This directory contains Spanish vocabulary lists organized by CEFR levels, topics, and frequency.

## Directories

### basic_a1_a2/
Basic Spanish vocabulary suitable for A1 and A2 level learners (Common European Framework of Reference).

- **Source**: [CodingFriends/basic-vocabulary-word-lists](https://github.com/CodingFriends/basic-vocabulary-word-lists)
- **Format**: CSV files with structure: `Spanish;English;;tags`
- **Level**: A1-A2 (Beginner to Elementary)

### frequency_lists/
Frequency-based Spanish vocabulary lists covering all proficiency levels.

- **Sources**:
  - [doozan/spanish_data](https://github.com/doozan/spanish_data) - Detailed frequency with POS tags
  - [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) - OpenSubtitles corpus
- **Format**: CSV and TXT files
- **Content**: Top 50,000 most common Spanish words with detailed linguistic information

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

## Files in frequency_lists/

| File | Description | Source | Format |
|------|-------------|--------|--------|
| frequency_detailed.csv | 50k+ words with POS tags, lemmas, usage counts | doozan/spanish_data | CSV with columns: count, spanish, pos, flags, usage |
| top_50k_words.txt | Top 50,000 Spanish words by frequency | doozan/spanish_data | TXT: word + tab + count |
| hermitdave_50k.txt | Top 50,000 from OpenSubtitles corpus | hermitdave/FrequencyWords | TXT: word + space + count |

The frequency lists cover vocabulary from A1 (beginner) through C2 (mastery) levels based on word frequency.

**Frequency to CEFR level (approximate):**
- A1: Top 500-1,000 words
- A2: Top 1,000-2,000 words
- B1: Top 2,000-4,000 words
- B2: Top 4,000-8,000 words
- C1: Top 8,000-16,000 words
- C2: 16,000+ words

## Usage Examples

### Loading frequency data
```python
import pandas as pd

# Load detailed frequency data with POS tags
df = pd.read_csv('frequency_lists/frequency_detailed.csv')
print(df.head(20))  # Top 20 most common words

# Get A1 level vocabulary (top 1000)
a1_vocab = df.head(1000)
verbs_a1 = a1_vocab[a1_vocab['pos'] == 'v']
```

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
