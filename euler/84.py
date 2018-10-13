import random


class Monopoly:
    class Case:

        def __init__(self, position, action=None):
            self.count = 0
            self.action = action
            self.position = position

        def add_passage(self):
            self.count += 1

        def get_action(self):
            return self.action

        def get_position(self):
            return self.position

    class Card:

        def __init__(self, action=None):
            self.action = action

        def get_action(self):
            return self.action

    class CardPile:

        def __init__(self, cards):
            self.cards = cards
            self.next_card_index = 0

        def use_next_card(self):
            action = self.cards[self.next_card_index].get_action()
            card = action()
            self.next_card_index += 1
            self.next_card_index %= len(self.cards)

            return card

    class CardCase(Case):

        def __init__(self, position, card_pile):
            self.card_pile = card_pile
            super().__init__(position, self.use_card)

        def use_card(self):
            return self.card_pile.use_next_card()

    class CommunityChest(CardPile):

        def __init__(self, monopoly):
            cards = []
            for i in range(0, 14):
                cards.append(Monopoly.Card(monopoly._stay_on_case))
            cards.append(Monopoly.Card(monopoly._go_to_jail))
            cards.append(Monopoly.Card(monopoly._go_to_go))

            monopoly.rand.shuffle(cards)

            super().__init__(cards)

    class Chance(CardPile):

        def __init__(self, monopoly):
            cards = []
            for i in range(0, 6):
                cards.append(Monopoly.Card(monopoly._stay_on_case))
            cards.append(Monopoly.Card(monopoly._go_to_jail))
            cards.append(Monopoly.Card(monopoly._go_to_go))
            cards.append(Monopoly.Card(monopoly._go_to_c1))
            cards.append(Monopoly.Card(monopoly._go_to_e3))
            cards.append(Monopoly.Card(monopoly._go_to_h2))
            cards.append(Monopoly.Card(monopoly._go_to_r1))
            cards.append(Monopoly.Card(monopoly._go_to_next_r))
            cards.append(Monopoly.Card(monopoly._go_to_next_r))
            cards.append(Monopoly.Card(monopoly._go_to_next_u))
            cards.append(Monopoly.Card(monopoly._go_3_case_back))

            monopoly.rand.shuffle(cards)

            super().__init__(cards)

    def __init__(self):
        self.rand = random.Random()

        self.cc = Monopoly.CommunityChest(self)
        self.ch = Monopoly.Chance(self)
        self.cases = [Monopoly.Case(i) for i in range(0, 40)]
        self.cases[2] = Monopoly.Case(2, self.cc.use_next_card)
        self.cases[7] = Monopoly.Case(7, self.ch.use_next_card)
        self.cases[17] = Monopoly.Case(17, self.cc.use_next_card)
        self.cases[22] = Monopoly.Case(22, self.ch.use_next_card)
        self.cases[30] = Monopoly.Case(30, self._go_to_jail)
        self.cases[33] = Monopoly.Case(33, self.cc.use_next_card)
        self.cases[36] = Monopoly.Case(36, self.ch.use_next_card)

        self.player_position = 0
        self.turn_count = 0

        self.consecutive_double = 0

    def _go_to_jail(self):
        return self.cases[10]

    def _go_to_go(self):
        return self.cases[0]

    def _go_to_c1(self):
        return self.cases[11]

    def _go_to_e3(self):
        return self.cases[24]

    def _go_to_h2(self):
        return self.cases[39]

    def _go_to_r1(self):
        return self.cases[5]

    def _go_to_next_r(self):
        if 5 <= self.player_position < 15:
            return self.cases[15]
        if 15 <= self.player_position < 25:
            return self.cases[25]
        if 25 <= self.player_position < 35:
            return self.cases[35]
        return self.cases[5]

    def _go_to_next_u(self):
        if 12 <= self.player_position < 28:
            return self.cases[28]
        return self.cases[12]

    def _go_3_case_back(self):
        return self.cases[self.player_position - 3]

    def _stay_on_case(self):
        return self.cases[self.player_position]

    def _roll_dices(self):
        d1 = self.rand.randint(1, 4)
        d2 = self.rand.randint(1, 4)
        if d1 == d2:
            self.consecutive_double += 1
        else:
            self.consecutive_double = 0

        return d1 + d2

    def _arrive_on_case(self, case):
        if case.get_action() is None:
            return case
        else:
            return case.get_action()()

    def _visit_case(self, case):
        case.add_passage()

    def next_turn(self):
        self.turn_count += 1
        step_count = self._roll_dices()

        if self.consecutive_double == 3:
            next_case = self._go_to_jail()

        else:
            self.player_position = (self.player_position + step_count) % len(self.cases)
            next_case = self._arrive_on_case(self.cases[self.player_position])

        self.player_position = next_case.get_position()
        self._visit_case(next_case)

    def get_probabilities(self):
        return [("0" + str(i), self.cases[i].count / self.turn_count) for i in range(0, len(self.cases))]


monop = Monopoly()
for i in range(1, 10000000):
    monop.next_turn()

for p1, p2 in monop.get_probabilities():
    print("i : " + str(p1) + ", proba : " + str(p2 * 100))

probas = monop.get_probabilities()
probas.sort(key=lambda r: r[1],reverse=True)
print("Solution : " + str(probas[0][0][-2:])+ str(probas[1][0][-2:])+ str(probas[2][0][-2:]))
