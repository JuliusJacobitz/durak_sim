import itertools, random
from typing import List, Tuple
import copy
 
def _compare_cards(attack:Tuple, defend:Tuple, trump:str):
    """
    return true if defended
    """
    # TODO Trumpf
    if attack[1] == defend[1]:
        if defend[0] > attack[0]:
            return True
    elif (attack[1] != trump and defend[1] == trump):
        return True
    
    return False


def defendable(attacker:List, defender:List, trump:str):
    """
    returns true if defender deck can defend attacker
    """
    a_1 = attacker[0]
    a_2 = attacker[1]

    d_1 = defender[0]
    d_2 = defender[1]

    return (_compare_cards(a_1,d_1,trump) and _compare_cards(a_2, d_2,trump)) or (_compare_cards(a_1,d_2,trump) and _compare_cards(a_2,d_1,trump))


if __name__ == "__main__":
    # make a deck of cards
    colors = ['Spade','Heart','Diamond','Club']
    deck = list(itertools.product([1,2,3,4,5,6,7,8,9,10,11,12,13],  # 2 - king
                                colors))
    


    N = 1000000
    defend_count = 0
    for i in range(N):
        random.shuffle(deck)
        random.shuffle(colors)


        atk = deck[0:2]
        dfd = deck[2:4]
        trump = colors[0]

        if defendable(atk,dfd,trump):
            defend_count += 1


    print(defend_count/N)
   


