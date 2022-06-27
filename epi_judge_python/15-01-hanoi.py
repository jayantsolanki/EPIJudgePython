import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
https://www.mathsisfun.com/games/towerofhanoi.html
The only way to solve the puzzle was to build interim towers on the different pegs
ou start at the bottom, not the top! Here’s how it works. If all the disks are on Peg A at the left, and you need to move them all to Peg C on the right, then you need to move the bottom disk, the largest one, to Peg C. Obviously.
Only way you can release nth disk is by building a n-1 disk tower on the empty area.

To do that, you need to build an interim tower on Peg B with the next largest disk at the bottom. And to do that, you need to build an interim tower on Peg C with the next largest disk.

aWESOME EXPLANATION HERE: https://www.youtube.com/watch?v=boS4N1_TLBk&ab_channel=FlorianLudewig
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).
Time: O(2^n)

Another https://blog.tjd.phlegethon.org/post/107154349862/technical-interviews-and-the-towers-of-hanoi
The largest disk moves exactly once, to the left (wrapping around). The second-largest disk moves twice, both times to the right, which matches the algorithm: it moves right to allow the largest disk to move left, and then right again to land on top of it. The third-largest disk moves four times, to the left each time, and the pattern continues for bigger towers. So we know two things: each disk has a preferred direction, and the full solution for N disks has (1 + 2 + ... + 2^(N-1)) == (2^N) - 1 total moves. The iterative algorithm looks like this:

define hanoi(N):
    repeat 2^N - 1 times:
        move the largest disk that can go in its preferred direction

You have the following constraints:

(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk. Write a program to move the disks from the first tower to the
last using Stacks.

The pattern here is :
 - Shift 'n-1' disks from 'origin' to 'buffer', using destination.
 - Shift last disk from 'origin' to 'destination'.
 - Shift 'n-1' disks from 'buffer' to 'destination', using origin.

moveDisks(int n, Tower origin, Tower destination, Tower buffer) {

/* Base case */
if (n <= 0) return;

/* move top n - 1 disks from origin to buffer, using destination as a buffer. */
moveDisks(n - 1, origin, buffer, destination);

/* move top from origin to destination
moveTop(origin, destination);

/* move top n - 1 disks from buffer to destination, using origin as a buffer. */

moveDisks(n - 1, buffer, destination, origin);
}
"""

NUM_PEGS = 3 #number of towers
#ring means those individual disks

def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg,
                                  use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg,
                                      to_peg)#move n - 1 disk to buffer using destination 
            #this the disk leaving 'from' tower get added to 'destination' tower
            # pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg,
                                      from_peg)# move 'n-1' disks from 'buffer' to 'destination', using origin

    # Initialize pegs.
    result: List[List[int]] = []
    #initializing towers
    # pegs = [list(reversed(range(1, num_rings + 1)))
    #         ] + [[] for _ in range(1, NUM_PEGS)]
    #same as above
    # pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(NUM_PEGS - 1)] 
    # print(pegs)
    compute_tower_hanoi_steps(num_rings, 0, 2, 1) #i changed the destination to 3 (index 2), earlier it was middle (2)
    return result

# compute_tower_hanoi(3)

#more simple version
# https://www.youtube.com/watch?v=rf6uf3jNjbo&ab_channel=Reducible
def compute_tower_hanyoi(num_rings: int) -> List[List[int]]:
    def hanoi(n, start, end):
        if n == 1:#lets imagine if there is only one, you move it directly to destination
            result.append([start, end])
        else:
            #using 3 here, since 0 + 1 + 2 = 3, video shows 6 , since 1 + 2 + 3
            other = 3 - (start + end)#method of finding the auxiliary/buffer rod at any given time in the recursion
            #above formual find which rod is available for next free legal move
            hanoi(n - 1, start, other)#first move to buffer, you can imagine this step for total disk ==2
            result.append([start, end])#move
            hanoi( n - 1, other, end)
    result: List[List[int]] = []
    hanoi(num_rings, 0, 2)
    return result
compute_tower_hanoi(2)




@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('15-01-hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
