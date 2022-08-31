import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Team Photo Day - 1
Design an algo that takes as input two teams and the heights of the players in the teams and checks if it is possible
to place players to take the photo subject to the placement contraint.
A team photo consists of a front row of players and a back row of players. A player in the back row must be taller than the player in 
the front of him. All players in a row must be from same team.
Logic:
    We should focus on hardest to place players. That is tall players in both teams. Let assume there are two team A and B.
    If Team A is going to be placed in the back row, then A's Tallest player should be taller than B's Tallest player, else
    configuration not possible. Conversely, A's tallest player should be placed before B's Tallest player, same for second tallest, third 
    tallest, so on so forth.

Time: O(nlogn)

"""
class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height: List[int]) -> None:
        self._players = [Team.Player(h) for h in height]

    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0: 'Team', team1: 'Team') -> bool:

        return all(
            a < b
            for a, b in zip(sorted(team0._players), sorted(team1._players)))

@enable_executor_hook
def valid_placement_exists_wrapper(executor, team0, team1, expected_01,
                                   expected_10):
    t0, t1 = Team(team0), Team(team1)

    result_01 = executor.run(
        functools.partial(Team.valid_placement_exists, t0, t1))
    result_10 = executor.run(
        functools.partial(Team.valid_placement_exists, t1, t0))
    if result_01 != expected_01 or result_10 != expected_10:
        raise TestFailure('')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('13-10-is_array_dominated.py',
                                       'is_array_dominated.tsv',
                                       valid_placement_exists_wrapper))
