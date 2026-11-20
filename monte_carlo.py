import numpy as np

import math

# MONTE CARLO SIMULATION

def monte_carlo(num_times = 100000, seed = 15):
    
    deck = np.arange(0, 52, 1)

    suit = deck // 13

    rank = deck % 13

    # Step 1: Creating a (100000, 52) and shuffling it

    grand_matrix = np.broadcast_to(deck, (num_times, 52))

    hat =  np.random.default_rng(seed = seed)

    shuffled_matrix = hat.permuted(grand_matrix, axis = 1)

    # now we are getting our actual same suit matrix

    actual_suit = shuffled_matrix[:, 0:5]

    actual_suit = actual_suit // 13

    print(f"Actual Suit Shape: {actual_suit.shape}")

    # now getting dealt hand matrix
    dealt_hand = shuffled_matrix[:, 0:5]

    print(f"Delat Hands Shape: {dealt_hand.shape}")

    # getting same rank matrix

    actual_rank = shuffled_matrix[:, 0:5] % 13

    print(f"Same Rank Shape: {actual_rank.shape}")

    # calculating flush mathematically

    math_flush = (4 * math.comb(13, 5)) / math.comb(52, 5)

    print(f"Mathematical Flush: {math_flush}")

    # now doing with our suit matrix

    diff = np.diff(actual_suit)

    # print(diff)

    boolean = (diff == 0).all(axis = 1)
    
    print(boolean.shape)

    # print(actual_suit[boolean])

    print(f"Manual Probability of Suit: {np.mean(boolean)}")

    # now getting probability of ranks

    sort = np.sort(actual_rank)

    difference = (sort[:, 0] == sort[:, 3]) | (sort[:, 1] == sort[:, 4])

    print(f"Manual Probability of Rank: {np.mean(difference)}")

    # print(actual_rank[difference])

    # mathematical rank

    math_four_of_a_kind = (13 * 48) / math.comb(52, 5)

    print(f"Mathematical Four of a Kind: {math_four_of_a_kind}")

if __name__ == "__main__":
    monte_carlo()
