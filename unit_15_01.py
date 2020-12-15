'''
Given the starting numbers 1,3,2, the 2020th number spoken is 1.
Given the starting numbers 2,1,3, the 2020th number spoken is 10.
Given the starting numbers 1,2,3, the 2020th number spoken is 27.
Given the starting numbers 2,3,1, the 2020th number spoken is 78.
Given the starting numbers 3,2,1, the 2020th number spoken is 438.
Given the starting numbers 3,1,2, the 2020th number spoken is 1836.
'''

from collections import defaultdict,deque
from elutils.decorators import timeit

@timeit
def get_nth_number_spoken(starting_nums, until_round=2020):
    if isinstance(starting_nums,str):
        starting_nums = starting_nums.split(',')

    rounds_numbers_appeared = {}
    round = 1
    for n in starting_nums[:-1]:
        rounds_numbers_appeared[n] = [round]
        round += 1
    most_recently_spoken_number = starting_nums[-1]
    while round != until_round:
        # not spoken before:
        if most_recently_spoken_number not in rounds_numbers_appeared:
            rounds_numbers_appeared[most_recently_spoken_number]=[round]
            most_recently_spoken_number = 0
        else:
            # spoken before:
            rounds_numbers_appeared[most_recently_spoken_number].append(round)
            most_recently_spoken_number = rounds_numbers_appeared[most_recently_spoken_number][-1] - rounds_numbers_appeared[most_recently_spoken_number][-2]
        round+=1

        #print(f"{round:3,}")
    return most_recently_spoken_number


assert get_nth_number_spoken([0,3,6])==436

assert get_nth_number_spoken([1,3,2])==1
assert get_nth_number_spoken([2,1,3])==10
assert get_nth_number_spoken([1,2,3])==27
assert get_nth_number_spoken([2,3,1])==78
assert get_nth_number_spoken([3,2,1])==438
assert get_nth_number_spoken([3,1,2])==1836

print(get_nth_number_spoken([2,15,0,9,1,20]))

print(get_nth_number_spoken([2,15,0,9,1,20],30_000_000))



