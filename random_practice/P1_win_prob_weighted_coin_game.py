import numpy as np


def P1_win_prob_weighted_coin_game(num_games, prob_heads=.5):
    player_one_wins = 0
    for n in range(0, num_games):
        num_flips = 0
        win = 0
        while win == 0:
            turn = np.random.uniform(0, 1)
            num_flips += 1
            if turn <= prob_heads:
                if num_flips % 2 != 0:
                    player_one_wins += 1
                win += 1
    return float(player_one_wins) / float(num_games)


print(P1_win_prob_weighted_coin_game(2, 1))
'''
https://towardsdatascience.com/probability-in-a-weighted-coin-flip-game-using-python-and-numpy-bc1686c49a35
'''
