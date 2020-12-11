full_sample = '''47
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

from itertools import combinations
import math

def format_sample(sample):
    '''returns the sample as a sorted with 0 and end+3'''

    sample = sample.split('\n')
    sample = [int(n) for n in sample]
    sample.insert(0,0)
    sample.sort()
    sample.append(sample[-1]+3)
    return sample

def get_clusters(sample):
    if isinstance(sample,str):
        sample = format_sample(sample)

    clusters = []
    tmp = []
    for s0, s1 in zip(sample,sample[1:]):
        diff = s1 - s0
        if diff == 1:
            tmp.append(s0)
        elif diff == 3:
            tmp.append(s0)
            clusters.append(tmp)
            tmp = []
        else:
            raise("Sum ting wong")
    clusters.append([sample[-1]])

    return clusters

def get_combinations_with_restrictions(cluster,require_start,require_end):

    unfiltered_combinations = []
    combination_lengths = [n+1 for n in range(len(cluster)) if n+1>=2] # for each length, but min 2
    if combination_lengths == []:
        return cluster
    for l in combination_lengths:
        coms = combinations(cluster,l)
        unfiltered_combinations.extend(list(coms))

    # must start and with a joltage that can connect either end
    filtered_combinations = [c for c in unfiltered_combinations if c[0]==require_start and c[-1]==require_end]
    # filter away if it makes too big a jump internally
    filtered_combinations = [c for c in filtered_combinations if c[0]+3 >=c[1]]

    return filtered_combinations

def get_valid_combinations(clusters):
    all_coms = []
    for index in range(1,len(clusters)):
        prev_c = clusters[index-1]
        this_c = clusters[index]
        try:
            next_c = clusters[index+1]
        except IndexError:
            all_coms.extend([next_c])
            break

        require_start = prev_c[-1]+3
        require_end = next_c[0]-3
        all_coms.append(get_combinations_with_restrictions(this_c,require_start,require_end))

    # ad hoc add the first element
    first_element = get_combinations_with_restrictions(clusters[0],require_start=0,require_end=clusters[1][0]-3)
    all_coms.insert(0,first_element)

    # get the length of each of the combinations
    all_coms_length = [len(c) for c in all_coms]
    # the number of possible ways is the product of all the ways to arrange the combinations.
    print(math.prod(all_coms_length))
    return all_coms

clusters = get_clusters(small_sample)
get_valid_combinations(clusters)

clusters = get_clusters(medium_sample)
get_valid_combinations(clusters)

clusters = get_clusters(full_sample)
get_valid_combinations(clusters)
