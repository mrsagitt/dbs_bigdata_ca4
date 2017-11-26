# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 2017

@author: Dominik Hemzaczek, 10360024
 -> read log file into class 
 -> test for correct reading whole file, 5255 lines
 -> test for reading record (422 objects)
 -> test for content of the first record (from dataframe)
"""
import unittest, pandas as pd
from big_file import get_data, get_records, parse_records

class TestRecords(unittest.TestCase):

    def setUp(self):
        self.lines = get_data('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.lines))

    def test_number_of_records(self):
        records = get_records(self.lines)
        self.assertEqual(422, len(records))

    def test_first_record(self):
        df = pd.DataFrame
        records = get_records(self.lines)        
        df = parse_records(records)
        self.assertEqual('Thomas', df.iloc[0]['user'])
        self.assertEqual('r1551925', df.iloc[0]['commit'])
        self.assertEqual(2, df.iloc[0]['add'])
        self.assertEqual(2, df.iloc[0]['delete'])
        self.assertEqual(0, df.iloc[0]['modify'])

if __name__ == '__main__':
    unittest.main()
