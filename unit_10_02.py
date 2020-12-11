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

medium_sample= '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

from itertools import combinations,zip_longest
import math


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



def get_combination_with_restrictions(cluster, must_start_with, must_end_with):
    coms = []
    combination_length = [n for n in range(1,len(cluster)+1)]

    for length in combination_length:
        com = combinations(cluster,length)
        com = [c for c in com if c[0]==must_start_with and c[-1]==must_end_with]
        coms.extend(com)
    return coms

def get_combinations_of_combinations(coms1,coms2):

    all_coms =[]
    for c in coms1:
        both = [c,*coms2]
        coms = list(combinations(both,2))
        coms = [c for c in coms if c[0]==coms1[0]]
        all_coms.extend(coms)
    return all_coms


def get_total_number_of_permutations(raw_sample):
    sample = format_sample(raw_sample)
    clusters = []
    tmp = []

    for s0,s1 in zip(sample,sample[1:]):
        diff = s1-s0
        if diff==1:
            tmp.append(s0)
        elif diff==3:
            tmp.append(s0)
            clusters.append(tmp)
            tmp=[]
        else:
            raise("Som ting wong")
    clusters.append([sample[-1]])

    total_coms = []
    for prev_c,next_c in zip(clusters,clusters[1:]):
        total_coms.append(get_permutations(prev_c,must_start_with=prev_c[0],must_end_with=next_c[0]-3))


    all_coms = []
    for this_cluster,next_cluster in zip(clusters,clusters[1:]):
        all_coms.append(get_combination_with_restrictions(this_cluster, must_start_with=this_cluster[0], must_end_with=next_cluster[0] - 3))

    coms_of_coms = []
    for ac1,ac2 in zip(all_coms,all_coms[1:]):
        if len(ac1)==2:
            continue
        coms_of_coms.append(get_combinations_of_combinations(ac1,ac2))
    print(coms_of_coms)

get_total_number_of_permutations(small_sample)
get_total_number_of_permutations(medium_sample)
