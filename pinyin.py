import re

SYLLABLE_PATTERN = re.compile(r"([a-zA-ZüÜvV]+)([0-5])")
VOWELS = "aeiouüAEIOUÜ"
TONE_MARKS = {
    "a": "āáǎà",
    "e": "ēéěè",
    "i": "īíǐì",
    "o": "ōóǒò",
    "u": "ūúǔù",
    "ü": "ǖǘǚǜ",
    "A": "ĀÁǍÀ",
    "E": "ĒÉĚÈ",
    "I": "ĪÍǏÌ",
    "O": "ŌÓǑÒ",
    "U": "ŪÚǓÙ",
    "Ü": "ǕǗǙǛ",
}


def find_mark_index(syllable: str) -> int:
    lowered = syllable.lower()
    for vowel in "ae":
        if vowel in lowered:
            return lowered.index(vowel)
    if "ou" in lowered:
        return lowered.index("ou")

    return max(index for index, character in enumerate(syllable) if character in VOWELS)


def convert_syllable(syllable: str, tone: int) -> str:
    syllable = syllable.replace("v", "ü").replace("V", "Ü")
    if tone in (0, 5) or not any(character in VOWELS for character in syllable):
        return syllable

    index = find_mark_index(syllable)
    marked = TONE_MARKS[syllable[index]][tone - 1]

    return syllable[:index] + marked + syllable[index + 1:]


def convert_text(text: str) -> str:
    return SYLLABLE_PATTERN.sub(
        lambda match: convert_syllable(match.group(1), int(match.group(2))),
        text,
    )
