


# Levels configuration for verbs and phrases only
# Nouns are now loaded per-level from generated structure files
levels = {
    "level_1": [
        # No verbs or phrases in level 1
    ],
    "level_2": [
        # No verbs or phrases in level 2
    ],
    "level_3": [
        # No verbs or phrases in level 3
    ],
    "level_4": [
        {"corpus": "verbs_present", "group": "Mental & Emotional"},
    ],
    "level_5": [
        {"corpus": "verbs_present", "group": "Actions & Transactions"},
    ],
    "level_6": [
        {"corpus": "verbs_present", "group": "Basic Needs & Daily Life"},
        {"corpus": "verbs_present", "group": "Sensory Perception"},
    ],
    "level_7": [
        {"corpus": "verbs_past", "group": "Mental & Emotional"},
        {"corpus": "verbs_past", "group": "Actions & Transactions"},
        {"corpus": "verbs_past", "group": "Basic Needs & Daily Life"},
    ],
    "level_8": [
        {"corpus": "verbs_present", "group": "Movement & Travel"},
        {"corpus": "verbs_past", "group": "Movement & Travel"},
        {"corpus": "verbs_past", "group": "Sensory Perception"},
    ],
    "level_9": [
        {"corpus": "verbs_present", "group": "Learning & Knowledge"},
        {"corpus": "verbs_past", "group": "Learning & Knowledge"},
    ],
    "level_10": [
        {"corpus": "phrases_one", "group": "Greetings"},
    ],
    "level_11": [
        # No verbs or phrases in level 11
    ],
    "level_12": [
        {"corpus": "verbs_future", "group": "Basic Needs & Daily Life"},
        {"corpus": "verbs_future", "group": "Movement & Travel"},
        {"corpus": "verbs_future", "group": "Mental & Emotional"},
        {"corpus": "verbs_future", "group": "Sensory Perception"},
        {"corpus": "verbs_future", "group": "Learning & Knowledge"},
        {"corpus": "verbs_future", "group": "Actions & Transactions"},
    ],
    "level_13": [
        # No verbs or phrases in level 13
    ],
    "level_14": [
        # No verbs or phrases in level 14
    ],
    "level_15": [
        {"corpus": "phrases_one", "group": "Asking for Directions"},
        {"corpus": "phrases_one", "group": "Transportation"},
        {"corpus": "phrases_one", "group": "Restaurant"},
        {"corpus": "phrases_one", "group": "Personal Comfort"},
    ],
}
