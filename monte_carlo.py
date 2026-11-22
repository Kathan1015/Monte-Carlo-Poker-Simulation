import numpy as np

import math

# MONTE CARLO SIMULATION

def monte_carlo(num_times = 100000, seed = 25):

    deck = np.arange(0, 52, 1)

    #print(deck)

    grand_matrix = np.broadcast_to(deck, (100000, 52))

    #print(grand_matrix.shape)

    hat = np.random.default_rng(seed = 25)

    shuffle_matrix = hat.permuted(grand_matrix, axis = 1)  # NOTE: DO NOT FORGOT TO USE axis = 1

    #print(shuffle_matrix)
    #print(shuffle_matrix.shape)

    suit = shuffle_matrix[:, 0:5] // 13

    #print(suit)
    #print(suit.shape)

    rank = shuffle_matrix[:, 0:5] % 13

    #print(rank)
    #print(rank.shape)

    # using np.diff() on suit to find out manual probability

    diff = np.diff(suit)

    #print(diff)
    #print(diff.shape)

    boolean1 = (diff == 0).all(axis = 1)

    #print(suit[boolean1])

    print(f"Manual probability of same suit: {np.mean(boolean1)}")

    # using np.sort() to find out manual probability for rank

    sort = np.sort(rank)

    #print(sort)
    #print(sort.shape)

    boolean2 = (sort[:, 0] == sort[:, 3]) | (sort[:, 1] == sort[:, 4])

    #print(rank[boolean2])

    print(f"Manual probability of same rank: {np.mean(boolean2)}")

    # now calculating mathematical probabilty

    same_suit = (4 * math.comb(13, 5)) / math.comb(52, 5)

    print(f"Mathematical probability of same suit: {same_suit}")

    same_rank = (13 * 48) / math.comb(52, 5)

    print(f"Mathematical probability of same rank: {same_rank}")

    # Errors

    print(f"Error for same suit: {abs(np.mean(boolean1) - same_suit)}")

    print(f"Error for same rank: {np.mean(boolean2) - same_rank}")

if __name__ == "__main__":
    monte_carlo()
