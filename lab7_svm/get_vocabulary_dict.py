#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from typing import Dict


# PASSED
def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """
    # FIXME: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}
    parser_dict = {}
    with open('data/vocab.txt', encoding="utf-8") as f:
        read_data = csv.reader(f, delimiter='\t')
        for line in read_data:
            elem_id, elem_vacab = int(line[0]), line[1]
            parser_dict[elem_id] = elem_vacab

    return parser_dict


# def get_vocabulary_dict() -> Dict[int, str]:
#     diction = {}
#     with open('data/vocab.txt', newline='') as file:
#         spamreader = csv.reader(file, delimiter='\t')
#         for row in spamreader:
#             print(row)
#             # diction[int(row[0])] = row[1]
#     file.close()
#     return diction


# print('len', len(get_vocabulary_dict()))
