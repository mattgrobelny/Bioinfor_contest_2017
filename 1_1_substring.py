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


def where_substring(string, substring):
    start_locations = []
    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            start_locations.append(i + 1)
        else:
            continue
    return(start_locations)


stri = 'GATATATGCATATACTT'
sub = 'ATAT'
print(where_substring(stri, sub))


import re


def find_motif(seq, motif):
    return [match.start() + 1 for match in re.finditer(r'(?=%s)' % re.escape(motif), seq)]

print find_motif('GATATATGCATATACTT', 'ATAT')
