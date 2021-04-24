#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:07:57 2020

@author: flor
"""
import re


with open('dev1-raw.txt', mode='r') as f:
    with open('tokenized_text.txt', mode='w') as f2:
        digits = '(\d+\.\d*)'
        hyphenated = '(\w*(?:[-](?![-])\w*)+)'
        double_dash = '([A-Za-z0-9]--[A-Za-z0-9])|(\s--\s)'
        punctuation = '[(!?;:\.\,)]|[\'\`]+]'
        words = '\w+'
        contractions = "/[A-Za-z]+('[A-Za-z]+)?"
        abbrevs = '([A-Z]([a-z]{0,3}|[A-Z]\.)\.)+'
        for line in f:
            for token in re.findall(
                    f'({digits}|{hyphenated}|{punctuation}|{words}|{contractions}|{abbrevs})',
                    line.strip()):
                print(token[0])
                print(token[0], file=f2)

