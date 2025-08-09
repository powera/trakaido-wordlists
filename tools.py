from lang_lt.wordlists import get_all_word_pairs_flat


def find_missing_words(input_words):
    """
    Find English words that are not already in the app's wordlists.
    
    Args:
        input_words: Either a list of words ["word1", "word2"] or a file path 
                    containing one word per line.
    
    Returns:
        list: A list of English words (in order) that are not found in any 
              of the app's wordlists.
    """
    # Get all existing English words from the app
    existing_words = set()
    flat_words = get_all_word_pairs_flat()
    for word_pair in flat_words:
        existing_words.add(word_pair['english'].lower())
    
    # Determine if input_words is a file path or a list
    if isinstance(input_words, str):
        # It's a file path
        try:
            with open(input_words, 'r', encoding='utf-8') as file:
                words_to_check = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {input_words}")
        except Exception as e:
            raise Exception(f"Error reading file {input_words}: {e}")
    elif isinstance(input_words, list):
        # It's a list of words
        words_to_check = input_words
    else:
        raise TypeError("input_words must be either a list of words or a file path string")
    
    # Find missing words (preserve order)
    missing_words = []
    for word in words_to_check:
        if word.lower() not in existing_words:
            missing_words.append(word)
    
    return missing_words


def check_for_duplicates():
    """
    Checks for duplicate words in the wordlists.
    
    This function identifies four types of duplicates:
    1. Exact English duplicates - the same English word appears multiple times
    2. Semantic English duplicates - the same English word with different Lithuanian translations
       (potentially different meanings)
    3. Exact Lithuanian duplicates - the same Lithuanian word appears multiple times
    4. Semantic Lithuanian duplicates - the same Lithuanian word with different English translations
       (potentially different meanings)
    
    Returns:
        tuple: (english_exact_duplicates, english_semantic_duplicates, 
                lithuanian_exact_duplicates, lithuanian_semantic_duplicates)
            - english_exact_duplicates: A list of English words that appear multiple times
            - english_semantic_duplicates: A dictionary where keys are English words and values
              are lists of different Lithuanian translations
            - lithuanian_exact_duplicates: A list of Lithuanian words that appear multiple times
            - lithuanian_semantic_duplicates: A dictionary where keys are Lithuanian words and values
              are lists of different English translations
    """
    flat_words = get_all_word_pairs_flat()
    
    # Track English word occurrences and translations
    english_word_count = {}
    english_word_translations = {}
    
    # Track Lithuanian word occurrences and translations
    lithuanian_word_count = {}
    lithuanian_word_translations = {}
    
    # Find duplicates
    english_exact_duplicates = []
    english_semantic_duplicates = {}
    lithuanian_exact_duplicates = []
    lithuanian_semantic_duplicates = {}
    
    for word_pair in flat_words:
        english = word_pair['english']
        lithuanian = word_pair['lithuanian']
        
        # Track English word count
        if english in english_word_count:
            english_word_count[english] += 1
            if english_word_count[english] == 2:  # Only add to duplicates list once
                english_exact_duplicates.append(english)
        else:
            english_word_count[english] = 1
        
        # Track different Lithuanian translations for English words
        if english in english_word_translations:
            if lithuanian not in english_word_translations[english]:
                english_word_translations[english].append(lithuanian)
                # If we find a new translation, it's a semantic duplicate
                if len(english_word_translations[english]) == 2:  # Only add to semantic duplicates once
                    english_semantic_duplicates[english] = english_word_translations[english]
        else:
            english_word_translations[english] = [lithuanian]
        
        # Track Lithuanian word count
        if lithuanian in lithuanian_word_count:
            lithuanian_word_count[lithuanian] += 1
            if lithuanian_word_count[lithuanian] == 2:  # Only add to duplicates list once
                lithuanian_exact_duplicates.append(lithuanian)
        else:
            lithuanian_word_count[lithuanian] = 1
        
        # Track different English translations for Lithuanian words
        if lithuanian in lithuanian_word_translations:
            if english not in lithuanian_word_translations[lithuanian]:
                lithuanian_word_translations[lithuanian].append(english)
                # If we find a new translation, it's a semantic duplicate
                if len(lithuanian_word_translations[lithuanian]) == 2:  # Only add to semantic duplicates once
                    lithuanian_semantic_duplicates[lithuanian] = lithuanian_word_translations[lithuanian]
        else:
            lithuanian_word_translations[lithuanian] = [english]
    
    return english_exact_duplicates, english_semantic_duplicates, lithuanian_exact_duplicates, lithuanian_semantic_duplicates


def find_lithuanian_words_not_in_audiobatches():
    """
    Find Lithuanian words from the app's wordlists that are NOT present in any 
    of the audiobatches text files.
    
    This function reads all .txt files in the audiobatches subdirectory and 
    compares them against all Lithuanian words in the app's wordlists to find
    which words from the app are missing from the audiobatches.
    
    Returns:
        list: A list of Lithuanian words from the app that are not found in any 
              audiobatches file.
    """
    import os
    import glob
    
    # Get all Lithuanian words from the app
    app_lithuanian_words = set()
    flat_words = get_all_word_pairs_flat()
    for word_pair in flat_words:
        app_lithuanian_words.add(word_pair['lithuanian'].lower())
    
    # Get the path to the audiobatches directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    audiobatches_dir = os.path.join(current_dir, 'lang_lt', 'audiobatches')
    
    # Read all words from all .txt files in audiobatches directory
    audiobatch_words = set()
    txt_files = glob.glob(os.path.join(audiobatches_dir, '*.txt'))
    
    for txt_file in txt_files:
        try:
            with open(txt_file, 'r', encoding='utf-8') as file:
                for line in file:
                    word = line.strip()
                    if word:  # Skip empty lines
                        audiobatch_words.add(word.lower())
        except Exception as e:
            print(f"Warning: Error reading file {txt_file}: {e}")
            continue
    
    # Find Lithuanian words from app that are NOT in any audiobatch file
    missing_from_audiobatches = []
    for lithuanian_word in sorted(app_lithuanian_words):
        if lithuanian_word not in audiobatch_words:
            missing_from_audiobatches.append(lithuanian_word)
    
    return missing_from_audiobatches


def print_words_by_frequency():
    """
    Print all words from the wordlists sorted by frequency_rank.
    
    Words with frequency_rank of None (null) will be printed at the end.
    For each word, prints: frequency_rank, English word, Lithuanian word, corpus, group
    """
    flat_words = get_all_word_pairs_flat()
    
    # Separate words with frequency_rank from those without
    words_with_rank = []
    words_without_rank = []
    
    for word_pair in flat_words:
        frequency_rank = word_pair.get('metadata', {}).get('frequency_rank')
        if frequency_rank is not None:
            words_with_rank.append(word_pair)
        else:
            words_without_rank.append(word_pair)
    
    # Sort words with frequency_rank by their rank (lower rank = more frequent)
    words_with_rank.sort(key=lambda x: x['metadata']['frequency_rank'])
    
    # Sort words without frequency_rank alphabetically by English word
    words_without_rank.sort(key=lambda x: x['english'].lower())
    
    # Print header
    print(f"{'Rank':<8} {'English':<20} {'Lithuanian':<20} {'Corpus':<20} {'Group':<30}")
    print("-" * 98)
    
    # Print words with frequency_rank
    for word_pair in words_with_rank:
        rank = word_pair['metadata']['frequency_rank']
        english = word_pair['english']
        lithuanian = word_pair['lithuanian']
        corpus = word_pair['corpus']
        group = word_pair['group']
        
        print(f"{rank:<8} {english:<20} {lithuanian:<20} {corpus:<20} {group:<30}")
    
    # Print separator for words without rank
    if words_without_rank:
        print("\n" + "=" * 98)
        print("WORDS WITHOUT FREQUENCY RANK:")
        print("=" * 98)
        
        # Print words without frequency_rank
        for word_pair in words_without_rank:
            english = word_pair['english']
            lithuanian = word_pair['lithuanian']
            corpus = word_pair['corpus']
            group = word_pair['group']
            
            print(f"{'N/A':<8} {english:<20} {lithuanian:<20} {corpus:<20} {group:<30}")
    
    # Print summary
    total_words = len(flat_words)
    words_with_rank_count = len(words_with_rank)
    words_without_rank_count = len(words_without_rank)
    
    print(f"\nSUMMARY:")
    print(f"Total words: {total_words}")
    print(f"Words with frequency rank: {words_with_rank_count}")
    print(f"Words without frequency rank: {words_without_rank_count}")


def create_audiobatch_file():
    """
    Create a new audiobatch file with all missing Lithuanian words, alphabetically sorted.
    
    This function finds all Lithuanian words that are not in any existing audiobatch file
    and creates a new audiobatch file (e.g., words8.txt) with all missing words in 
    alphabetical order.
    
    Returns:
        str: The filename of the created file, or None if no words were missing.
    """
    import os
    import glob
    
    # Find words missing from audiobatches (already sorted alphabetically)
    missing_words = find_lithuanian_words_not_in_audiobatches()
    
    if not missing_words:
        print("No missing words found. All Lithuanian words are already in audiobatch files.")
        return None
    
    print(f"Found {len(missing_words)} words missing from audiobatch files.")
    
    # Determine the next batch file number
    current_dir = os.path.dirname(os.path.abspath(__file__))
    audiobatches_dir = os.path.join(current_dir, 'lang_lt', 'audiobatches')
    
    # Find existing batch files and determine the next number
    existing_files = glob.glob(os.path.join(audiobatches_dir, 'words*.txt'))
    batch_numbers = []
    
    for file_path in existing_files:
        filename = os.path.basename(file_path)
        # Extract number from filename like "words7.txt"
        if filename.startswith('words') and filename.endswith('.txt'):
            try:
                number_str = filename[5:-4]  # Remove "words" and ".txt"
                batch_numbers.append(int(number_str))
            except ValueError:
                continue
    
    next_batch_number = max(batch_numbers) + 1 if batch_numbers else 1
    new_filename = f"words{next_batch_number}.txt"
    new_file_path = os.path.join(audiobatches_dir, new_filename)
    
    try:
        # Create the new audiobatch file with all missing words
        with open(new_file_path, 'w', encoding='utf-8') as file:
            for word in missing_words:
                file.write(f"{word}\n")
        
        print(f"Created new audiobatch file: {new_filename}")
        print(f"Added {len(missing_words)} words to the new batch file.")
        
        return new_filename
        
    except Exception as e:
        print(f"Error creating audiobatch file: {e}")
        return None
