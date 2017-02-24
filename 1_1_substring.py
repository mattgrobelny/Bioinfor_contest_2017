#
# Bioinformatics Contest 2017
# Contest link: http://contest.bioinf.me
#
# By: Mateusz Grobelny
#

# Given:
#     Two DNA strings s and t(each of length at most 1 kbp).
#
# Return:
#     All locations of t as a substring of s
#
#
# Sample Input:
# GATATATGCATATACTT
# ATAT
# Sample Output:
# 2 4 10

# put your python code here


import sys


def where_substring(string, substring):
    start_locations = ""
    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            start_locations = start_locations + str(i + 1) + ' '
        else:
            continue
    return(start_locations[0:-1])


s = sys.stdin.readline()
t = sys.stdin.readline()
s = s.strip('\n')
t = t.strip('\n')
print(where_substring(s, t))
