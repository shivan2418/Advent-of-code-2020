sample = '''47
99
115
65
10
55
19
73
80
100
71
110
64
135
49
3
1
98
132
2
38
118
66
116
104
87
79
114
40
37
44
97
4
140
60
86
56
133
7
146
85
111
134
53
121
77
117
21
12
81
145
129
107
93
22
48
11
54
92
78
67
20
138
125
57
96
26
147
124
34
74
143
13
28
126
50
29
70
39
63
41
91
32
84
144
27
139
33
88
72
23
103
16'''

small_sample = '''16
10
15
5
1
11
7
19
6
12
4'''

from itertools import combinations

def format_sample(sample):
    '''returns the sample as a sorted with 0 and end+3'''

    sample = sample.split('\n')
    sample = [int(n) for n in sample]
    sample.insert(0,0)
    sample.sort()
    sample.append(sample[-1]+3)
    return sample

def get_permutations(nums,must_start_with,must_end_with):
    coms = []
    for i in range(len(nums)):
        coms.extend(list(combinations(nums, i + 1)))


    coms = [c for c in coms if c[-1]==must_end_with and c[0]==must_start_with]
    return coms

small_sample = format_sample(small_sample)


clusters = []

tmp = []
for s0,s1 in zip(small_sample,small_sample[1:]):
    diff = s1-s0
    if diff==1:
        tmp.append(s0)
    elif diff==3:
        tmp.append(s0)
        clusters.append(tmp)
        tmp=[]
    else:
        raise("Som ting wong")


total_coms = []
for cluster0,cluster1 in zip(clusters,clusters[1:]):
    total_coms.append(get_permutations(cluster0,must_start_with=cluster0[0],must_end_with=cluster1[0]-3))


possible_coms= 0
calc_nums = []
for com_list in total_coms:
    calc_nums.append(len(com_list))

import math
print(calc_nums)
print(math.product(calc_nums))