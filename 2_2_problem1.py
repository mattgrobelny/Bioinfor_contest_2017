#
# Bioinformatics Contest 2017
# Contest link: http://contest.bioinf.me
#
# By: Mateusz Grobelny
#
# Problem 2

import sys
import re
test = open(
    '/Users/matt/github/Bioinformatics_Contests/Bioinfor_contest_2017/2_2p1_test.txt', 'r')
intial_chems = test.readline().strip('\n').split(" ")
print intial_chems
#intial_chems = sys.stdin.readline()

output_chems = []

chem_rxn_dic = {}

split_pattern = re.compile('[\+\->]')


def add_rnx(rxn):
    split_rxn_string = split_pattern.split(rxn)
    if len(split_rxn_string) == 2:

    print split_rxn_string
    key = split_rxn_string[0] + "_" + split_rxn_string[1]
    chem_rxn_dic[key] = chem_rxn_dic[key].append()

total_chems = 0


def output_rxn(list_of_present_chem):
    while total_chems <= 1000:
        for chem_L in intial_chems:
            for chem_R in intial_chems:
                chem_list = [chem_L, chem_R]
                output_of_it_rxn = chem_rxn_dic[chem_list]
                if output_of_it_rxn not in output_chems:
                    output_chems.append(output_of_it_rxn)
                elif output_of_it_rxn not in intial_chems:
                    intial_chems.append(output_of_it_rxn)
                total_chems += 1

for line in test:
    add_rnx(line.strip('\n'))

print chem_rxn_dic
