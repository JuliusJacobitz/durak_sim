import itertools, random
from typing import List, Tuple
import copy
 
def _compare_cards(attack:Tuple, defend:Tuple):
    """
    return true if defended
    """
    # TODO Trumpf
    if attack[1] == defend[1]:
        if defend[0] > attack[0]:
            return True
    
    return False


def defendable(attacker:List, defender:List):
    """
    returns true if defender deck can defend attacker
    """
    a_1 = attacker[0]
    a_2 = attacker[1]

    d_1 = defender[0]
    d_2 = defender[1]

    return (_compare_cards(a_1,d_1) and _compare_cards(a_2, d_2)) or (_compare_cards(a_1,d_2) and _compare_cards(a_2,d_1))


if __name__ == "__main__":
    # make a deck of cards
    deck = list(itertools.product([1,2,3,4,5,6,7,8,9,10,11,12,13],  # 2 - king
                                ['Spade','Heart','Diamond','Club']))
    
    
    N = 100000
    defend_count = 0
    for i in range(N):
        random.shuffle(deck)
        atk = deck[0:2]
        dfd = deck[2:4]

        if defendable(atk,dfd):
            defend_count += 1


    print(defend_count/N)
   


