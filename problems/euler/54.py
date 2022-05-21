import collections
from enum import Enum


class Card:

    def __init__(self, suit, rank):

        if not isinstance(suit, Card.Suit) or not isinstance(rank, Card.Rank):
            raise TypeError()

        self._rank = rank
        self._suit = suit

    @classmethod
    def from_string(cls, str="AC"):
        if len(str) != 2:
            raise AttributeError()

        rank_str = str[0]
        suit_str = str[1]

        return Card(Card.Suit.from_string(suit_str), Card.Rank.from_string(rank_str))

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    class Suit(Enum):
        DIAMOND = 1,
        HEART = 2,
        SPADE = 3,
        CLUB = 4

        @classmethod
        def from_string(cls, str="D"):
            suit_str_dict = {"D": cls.DIAMOND, "H": cls.HEART, "S": cls.SPADE, "C": cls.CLUB}

            if str not in suit_str_dict:
                raise AttributeError()
            return suit_str_dict[str]

    class Rank(Enum):
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

        @classmethod
        def from_string(cls, str="A"):
            rank_str_dict = {"A": cls.ACE, "K": cls.KING, "Q": cls.QUEEN, "J": cls.JACK, "T": cls.TEN, "9": cls.NINE,
                             "8": cls.EIGHT, "7": cls.SEVEN, "6": cls.SIX,
                             "5": cls.FIVE, "4": cls.FOUR, "3": cls.THREE, "2": cls.TWO}

            if str not in rank_str_dict:
                raise AttributeError()
            return rank_str_dict[str]


class PokerHand:
    CARD_COUNT = 5

    def __init__(self, cards=None):
        if cards is None or len(cards) != self.CARD_COUNT:
            raise AttributeError()
        self._cards = cards
        self._evaluator = PokerHand.Evaluator()
        self._evaluation = self._evaluator.evaluate(self)

    @classmethod
    def from_string(cls, hand_str):
        card_strs = hand_str.split()
        cards = [Card.from_string(card_str) for card_str in card_strs]
        return PokerHand(cards)

    @classmethod
    def compare(cls, hand1, hand2):
        if not isinstance(hand1, PokerHand) or not isinstance(hand2, PokerHand):
            raise TypeError()

        hand1_value = hand1.evaluation.rank.value[0]
        hand2_value = hand2.evaluation.rank.value[0]

        if hand1_value > hand2_value:
            return 1

        if hand2_value > hand1_value:
            return 2

        hand1_card_value = hand1.evaluation.rank_card_value
        hand2_card_value = hand2.evaluation.rank_card_value

        if hand1_card_value > hand2_card_value:
            return 1

        if hand2_card_value > hand1_card_value:
            return 2

        hand1_card_values = hand1.evaluation.other_card_values
        hand2_card_values = hand2.evaluation.other_card_values

        for i in range(0, len(hand1_card_values)):
            if hand1_card_values[i] > hand2_card_values[i]:
                return 1

            if hand2_card_values[i] > hand1_card_values[i]:
                return 2
        return 0

    @property
    def evaluation(self):
        return self._evaluation

    @property
    def cards(self):
        return self._cards

    def get_suits(self):
        return [card.suit for card in self.cards]

    def get_ranks(self):
        return [card.rank for card in self.cards]

    class Rank(Enum):
        HIGH_CARD = 0,
        ONE_PAIR = 1,
        TWO_PAIRS = 2,
        THREE_OF_A_KIND = 3,
        STRAIGHT = 4,
        FLUSH = 5,
        FULL_HOUSE = 6,
        FOUR_OF_A_KIND = 7,
        STRAIGHT_FLUSH = 8,
        ROYAL_FLUSH = 9

    class Evaluation:

        def __init__(self, rank, rank_card_value, other_card_values):
            if not isinstance(rank, PokerHand.Rank):
                raise TypeError()

            self._rank = rank
            self._rank_card_value = rank_card_value
            self._other_card_values = other_card_values

        @property
        def rank(self):
            return self._rank

        @property
        def rank_card_value(self):
            return self._rank_card_value

        @property
        def other_card_values(self):
            return self._other_card_values

    class Evaluator:

        value_dict = {
            Card.Rank.ACE: 12,
            Card.Rank.KING: 11,
            Card.Rank.QUEEN: 10,
            Card.Rank.JACK: 9,
            Card.Rank.TEN: 8,
            Card.Rank.NINE: 7,
            Card.Rank.EIGHT: 6,
            Card.Rank.SEVEN: 5,
            Card.Rank.SIX: 4,
            Card.Rank.FIVE: 3,
            Card.Rank.FOUR: 2,
            Card.Rank.THREE: 1,
            Card.Rank.TWO: 0
        }

        def evaluate(self, poker_hand):
            if not isinstance(poker_hand, PokerHand):
                raise TypeError()

            if self._is_royal_flush(poker_hand):
                return PokerHand.Evaluation(
                    PokerHand.Rank.ROYAL_FLUSH,
                    self._evaluate_rank(Card.Rank.ACE),
                    []
                )

            if self._is_straight_flush(poker_hand):
                return PokerHand.Evaluation(
                    PokerHand.Rank.STRAIGHT_FLUSH,
                    self._get_highest_rank(poker_hand.cards),
                    []
                )

            if self._is_four_of_a_kind(poker_hand):
                rank_counter = collections.Counter(poker_hand.get_ranks())
                four_of_a_kind_rank = rank_counter.most_common()[0][0]
                other_card_rank = rank_counter.most_common()[1][0]
                return PokerHand.Evaluation(
                    PokerHand.Rank.FOUR_OF_A_KIND,
                    self._evaluate_rank(four_of_a_kind_rank),
                    [self._evaluate_rank(other_card_rank)]
                )

            if self._is_full_house(poker_hand):
                rank_counter = collections.Counter(poker_hand.get_ranks())
                three_of_a_kind_rank = rank_counter.most_common()[0][0]
                pair_card_rank = rank_counter.most_common()[1][0]
                return PokerHand.Evaluation(
                    PokerHand.Rank.FULL_HOUSE,
                    self._evaluate_rank(three_of_a_kind_rank),
                    [self._evaluate_rank(pair_card_rank)]
                )

            if self._is_flush(poker_hand):
                card_values = self._evaluate_ranks(poker_hand.get_ranks())
                card_values.sort(reverse=True)
                return PokerHand.Evaluation(
                    PokerHand.Rank.FLUSH,
                    card_values[0],
                    card_values[1:]
                )

            if self._is_straight(poker_hand):
                max_card_value = max(self._evaluate_ranks(poker_hand.get_ranks()))
                return PokerHand.Evaluation(
                    PokerHand.Rank.STRAIGHT,
                    max_card_value,
                    []
                )

            if self._is_three_of_a_kind(poker_hand):
                rank_counter = collections.Counter(poker_hand.get_ranks())
                three_of_a_kind_rank = rank_counter.most_common()[0][0]
                other_card_ranks = [rank_counter.most_common()[1][0], rank_counter.most_common()[2][0]]
                other_card_values = self._evaluate_ranks(other_card_ranks)
                other_card_values.sort(reverse=True)

                return PokerHand.Evaluation(
                    PokerHand.Rank.THREE_OF_A_KIND,
                    self._evaluate_rank(three_of_a_kind_rank),
                    other_card_values
                )

            if self._is_two_pairs(poker_hand):
                rank_counter = collections.Counter(poker_hand.get_ranks())
                first_pair_rank = rank_counter.most_common()[0][0]
                second_pair_rank = rank_counter.most_common()[1][0]
                other_card_value = self._evaluate_rank(rank_counter.most_common()[2][0])
                max_pair_value = max(self._evaluate_ranks([first_pair_rank, second_pair_rank]))
                min_pair_value = max(self._evaluate_ranks([first_pair_rank, second_pair_rank]))

                return PokerHand.Evaluation(
                    PokerHand.Rank.TWO_PAIRS,
                    max_pair_value,
                    [min_pair_value, other_card_value]
                )

            if self._is_pair(poker_hand):
                rank_counter = collections.Counter(poker_hand.get_ranks())
                pair_rank = rank_counter.most_common()[0][0]
                other_card_ranks = [rank_counter.most_common()[i][0] for i in range(1, 4)]
                other_card_values = self._evaluate_ranks(other_card_ranks)
                other_card_values.sort(reverse=True)

                return PokerHand.Evaluation(
                    PokerHand.Rank.ONE_PAIR,
                    self._evaluate_rank(pair_rank),
                    other_card_values
                )

            card_values = self._evaluate_ranks(poker_hand.get_ranks())
            card_values.sort(reverse=True)
            return PokerHand.Evaluation(
                PokerHand.Rank.HIGH_CARD,
                card_values[0],
                card_values[1:]
            )

        def _is_royal_flush(self, poker_hand):

            if not self._is_flush(poker_hand):
                return False

            royal_flush_rank_set = {Card.Rank.TEN, Card.Rank.JACK, Card.Rank.QUEEN, Card.Rank.KING, Card.Rank.ACE}
            if royal_flush_rank_set != set(poker_hand.get_ranks()):
                return False

            return True

        def _is_straight_flush(self, poker_hand):

            if not self._is_flush(poker_hand):
                return False

            if not self._is_straight(poker_hand):
                return False

            return True

        def _is_four_of_a_kind(self, poker_hand):

            rank_counter = collections.Counter(poker_hand.get_ranks())
            if 4 not in rank_counter.values():
                return False
            return True

        def _is_full_house(self, poker_hand):

            rank_counter = collections.Counter(poker_hand.get_ranks())
            if 3 not in rank_counter.values() or 2 not in rank_counter.values():
                return False
            return True

        def _is_flush(self, poker_hand):
            distinct_suit_count = len(set(poker_hand.get_suits()))
            if distinct_suit_count > 1:
                return False
            return True

        def _is_straight(self, poker_hand):
            ranks = poker_hand.get_ranks()
            values = [self._evaluate_rank(rank) for rank in ranks]
            values.sort()
            min_value = min(values)
            if values != list(range(min_value, min_value + PokerHand.CARD_COUNT)):
                return False

            return True

        def _is_three_of_a_kind(self, poker_hand):

            rank_counter = collections.Counter(poker_hand.get_ranks())
            if 3 not in rank_counter.values():
                return False
            return True

        def _is_two_pairs(self, poker_hand):

            rank_counter = collections.Counter(poker_hand.get_ranks())
            pair_count = 0
            for value in rank_counter.values():
                if value == 2: pair_count += 1
            if pair_count != 2:
                return False
            return True

        def _is_pair(self, poker_hand):
            rank_counter = collections.Counter(poker_hand.get_ranks())
            pair_count = 0
            for value in rank_counter.values():
                if value == 2: pair_count += 1
            if pair_count != 1:
                return False
            return True

        def _evaluate_rank(self, card_rank):
            return self.value_dict[card_rank]

        def _evaluate_ranks(self, card_ranks):
            return [self._evaluate_rank(card_rank) for card_rank in card_ranks]

        def _get_highest_rank(self, card_ranks):
            return max([self._evaluate_rank(rank) for rank in card_ranks])


poker_file = open("poker.txt", 'r')
poker_list = poker_file.readlines()
hand_1_win_count = 0
hand_2_win_count = 0
hand1_ranks = {}
hand2_ranks = {}

for hands_str in poker_list:
    hand1_str = hands_str[0:14]
    hand2_str = hands_str[15:29]
    hand1 = PokerHand.from_string(hand1_str)
    hand2 = PokerHand.from_string(hand2_str)

    if hand1.evaluation.rank not in hand1_ranks:
        hand1_ranks[hand1.evaluation.rank] = 0
    if hand2.evaluation.rank not in hand2_ranks:
        hand2_ranks[hand2.evaluation.rank] = 0
    hand1_ranks[hand1.evaluation.rank] += 1
    hand2_ranks[hand2.evaluation.rank] += 1

    if PokerHand.compare(hand1, hand2) == 1:
        hand_1_win_count += 1

    if PokerHand.compare(hand1, hand2) == 2:
        hand_2_win_count += 1
print("Solution : " + str(hand_1_win_count))
