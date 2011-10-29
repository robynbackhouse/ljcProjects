#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# This code was written jointly by myself and Jonathan Hartley, who very kindly provided all the python expertise.
# His rather cool blog (featuring of course python among other interesting snippets) can be found here:  http://tartley.com/

from functional_list import FunctionalList, Nil


SUITS = {
    'c': 'Clubs',
    'd': 'Diamonds',
    'h': 'Hearts',
    's': 'Spades',
}


def cards_from_str(string):
    return FunctionalList.of(*string.split())


def _find_jack(cards):
    head = cards.head
    value = head[0]
    suit = head[1]
    return suit if value == 'J' else _find_jack(cards.tail)

def find_jack(hand):
    return SUITS[_find_jack(cards_from_str(hand))]


def _find_pair(cards):
    return (
        Nil()
        if isinstance(cards, Nil) or isinstance(cards.tail, Nil)
        else (
            cards
            if cards.head[0] == cards.tail.head[0]
            else _find_pair(cards.tail)
        )
    )
