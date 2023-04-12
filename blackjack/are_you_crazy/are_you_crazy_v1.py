#!/usr/bin/env python3

from typing import List, Tuple
import gym
import numpy as np
import matplotlib.pyplot as plt
import argparse


def are_you_crazy(env: gym.Env, rounds: int, num_players: int) -> List[float]:
    """
    Simulates multiple rounds of the Blackjack game for multiple players, and returns a list of each player's total payout.
    :param env: The Blackjack environment to use for the simulation
    :param rounds: The number of rounds to simulate for each player
    :param num_players: The number of players to simulate
    :return: A list of each player's total payout after the specified number of rounds
    """
    payouts = []
    for player in range(num_players):
        round = 1
        total_payout = 0

        while round < rounds:
            player, dealer, ace = env.reset()[0]
            is_done = False

            while not is_done:
                action = 0 if player >= 18 else 1
                obs, payout, is_done, _, _ = env.step(action)
                player, _, _ = obs

            total_payout += payout
            round += 1

        payouts.append(total_payout)

    return payouts


def plot(payouts: List[float], rounds: int, num_players: int) -> None:
    """
    Plots a line graph of the average payout after the specified number of rounds for the specified number of players.
    :param payouts: A list of each player's total payout after the specified number of rounds
    :param rounds: The number of rounds that were simulated for each player
    :param num_players: The number of players that were simulated
    """
    plt.plot(payouts)
    plt.xlabel('num_player')
    plt.ylabel('payout after ' + str(rounds) + ' rounds')
    plt.show()
    print("Average payout of a player after {} rounds is {}".format(rounds, sum(payouts) / num_players))


def main() -> None:
    """
    The main function of the script. Parses command-line arguments and calls the other functions to run the simulation and plot the results.
    """
    parser = argparse.ArgumentParser(description='Blackjack simulation with configurable rounds and number of players.')
    parser.add_argument('--rounds', type=int, default=1000, help='Number of rounds per player (default: 1000)')
    parser.add_argument('--num_players', type=int, default=1000, help='Number of players (default: 1000)')

    args = parser.parse_args()

    env = gym.make('Blackjack-v1')

    rounds = args.rounds
    num_players = args.num_players

    payouts = are_you_crazy(env, rounds, num_players)
    plot(payouts, rounds, num_players)


if __name__ == "__main__":
    main()
