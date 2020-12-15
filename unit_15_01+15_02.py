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

    last_number_spoken_in_round = {}
    round = 1
    for n in starting_nums[:-1]:
        last_number_spoken_in_round[n] = round
        round += 1
    most_recently_spoken_number = starting_nums[-1]
    for round in range(round,until_round):
        # not spoken before:
        if most_recently_spoken_number not in last_number_spoken_in_round:
            last_number_spoken_in_round[most_recently_spoken_number]=round
            most_recently_spoken_number = 0
        else:
            # spoken before:
            last_spoken_in_round = last_number_spoken_in_round[most_recently_spoken_number]
            last_number_spoken_in_round[most_recently_spoken_number] = round
            most_recently_spoken_number = last_number_spoken_in_round[most_recently_spoken_number]-last_spoken_in_round


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



