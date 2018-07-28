from enum import Enum


class Color(Enum):
    DIAMOND = 1,
    HEART = 2,
    SPADE = 3,
    CLUB = 4

    color_str_dict = {"D": DIAMOND, "H": HEART, "S": SPADE, "C": CLUB}

    @classmethod
    def from_string(cls, str="D"):
        if str not in cls.color_str_dict:
            raise AttributeError()
        return cls.color_str_dict[str]


class Value(Enum):
    ACE = 0,
    KING = 1,
    QUEEN = 2,
    JACK = 3,
    TEN = 4,
    NINE = 5,
    EIGHT = 6,
    SEVEN = 7,
    SIX = 8,
    FIVE = 9,
    FOUR = 10,
    THREE = 11,
    TWO = 12

    value_str_dict = {"A": ACE, "K": KING, "Q": QUEEN, "J": JACK, "T": TEN, "9": NINE, "8": EIGHT, "7": SEVEN, "6": SIX,
                      "5": FIVE, "4": FOUR, "3": THREE, "2": TWO}

    @classmethod
    def from_string(cls, str="A"):
        if str not in cls.value_str_dict:
            raise AttributeError()
        return cls.value_str_dict[str]


class Card:

    def __init__(self, color=Color.CLUB, value=Value.ACE):

        if not isinstance(color, Color) or not isinstance(value, Value):
            raise TypeError()

        self._value = value
        self._color = color

    @classmethod
    def from_string(cls, str="AC"):
        if len(str) != 2:
            raise AttributeError()

        value_str = str[0]
        color_str = str[1]

        return Card(Color.from_string(color_str), Value.from_string(value_str))

    @property
    def value(self):
        return self._value

    @property
    def color(self):
        return self._color


class PokerHand:
    def __init__(self, cards=None):
        if cards is None or len(cards) != 5:
            raise AttributeError()
        self._cards = cards

    @property
    def cards(self):
        return self._cards

