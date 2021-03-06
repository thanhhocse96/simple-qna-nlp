import enum

CORPUS_CSV = "corpus/corpus.csv"
CORPUS_HEADER_LIST = list(["word", "n-gram", "cat", "name-index"])

STUDENTS_CSV = "input/students.csv"
STUDENTS_HEADER_LIST = list(["full_name", "id", "subject", "room", "day", "start_time", "class_length"])

INPUT_QUESTION_NUMBER = 4
INPUT_QUESTION_PATH_PREFIX = "input/question"
INPUT_QUESTION_PATH_POSTFIX = ".txt"

class SENTENCE_TYPE(enum.Enum):
    ASSERT = 1
    COMMAND = 2
    YNQUERY = 3
    WHQUERY = 4

class N_GRAM(enum.Enum):
    ONE_GRAM = 1
    TWO_GRAM = 2
    MORE_GRAM = 3

class WORD_CAT(enum.Enum):
    NOUN = 1
    VERB = 2
    PREP = 3
    ADV = 4
    PRO = 5
    NUM = 6
    NAME = 7
    OTHER = 8