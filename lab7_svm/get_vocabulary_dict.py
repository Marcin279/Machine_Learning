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
        read_data = f.read()
        # read_data = read_data.split(sep='\t')
        read_data = read_data.split(sep='\n')
        for line in read_data:
            # line = line.split(sep='\t')
            line = line.split(sep='\t')
            if len(line) == 2:
                id, vacab = int(line[0]), line[1]
            parser_dict[id] = vacab

    return parser_dict
