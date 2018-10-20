import re
import math
from pathlib import Path


# Misc
APP_NAME = 'vk-code-names'
APP_DIR = Path(__file__).parent

# Regexps
RE_GAME_REQUEST = re.compile(r'^го')
RE_TEXT_WITH_REFERENCE = re.compile(r'^\[.+\|.+\]\s?,?\s?(.*?)$')
RE_WORD_AND_NUMBER = re.compile(r'^(\w+)\s(\d+)$')
RE_WANTS_TO_PLAY = re.compile(r'^я$')
RE_NO_MORE_PLAYERS = re.compile(r'^все$')

# Button colors
BUTTON_COLOR_NEGATIVE = 'negative'
BUTTON_COLOR_POSITIVE = 'positive'
BUTTON_COLOR_DEFAULT = 'default'
BUTTON_COLOR_PRIMARY = 'primary'

# Emojis
EMOJI_BLUE_HEART = '💙'
EMOJI_GREEN_HEART = '💚'
EMOJI_RED_HEART = '❤'
EMOJI_BLACK_HEART = '🖤'

# Map
N_BLUE_CELLS = 7
N_RED_CELLS = 6
N_NEUTRAL_CELLS = 4
N_KILLER_CELLS = 1
N_TOTAL_CELLS = sum([
    N_BLUE_CELLS,
    N_RED_CELLS,
    N_NEUTRAL_CELLS,
    N_KILLER_CELLS
])
N_CELLS_IN_ROW = 3
N_CELLS_IN_COL = 6
assert N_CELLS_IN_ROW * N_CELLS_IN_COL == N_TOTAL_CELLS

# Game
MAX_WORD_LEN = 16
MAX_GUESS_ATTEMPTS = max(N_BLUE_CELLS, N_RED_CELLS)
WORD_LIST_NAME = 'ru-nouns.txt'
