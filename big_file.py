# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 21:22:04 2017

@author: Dominik Hemzaczek, 10360024
 -> read log file into variable
 -> create list with records (422 elements in one list)
 -> parse records as dictionary and add to new list (422 individual dictionaries)
 -> return list of dictionaries as pandas dataframe
 -> save dataframe into CSV file
"""

def get_data(file):
    f = open(file,'r')
    lines = f.read().splitlines()
    f.close()
    return lines

def get_records(lines):
    records=[]
    i=1
    marker = lines[0]
    while i < len(lines):
        record=[]
        #read one record into a list
        while lines[i] != marker:
            record.append(lines[i])
            i=i+1
        records.append(record)
        i=i+1
    return records

def parse_records(records):
    recs=[]    
    for r in records:
        # parse 'header' of record to dictionary
        head = r[0].strip().split('|')
        rec = {'commit':head[0].strip(),
               'user':head[1].strip(),
               'date_time':head[2].strip()[:19],
               'comments':int(head[3].strip().split(' ')[0])}
        
        # get 4th element from changes
        changes = map(lambda x: x[3], r[2:len(r)-rec['comments']-1])
        
        rec.update({'add':changes.count('A'),
                    'modify':changes.count('M'),
                    'delete':changes.count('D')})
        
        recs.append(rec)
    
    import pandas as pd
    df = pd.DataFrame(recs)
    #print df
    return df
    

if __name__ == '__main__':
    
    file = 'changes_python.log'
    lines = get_data(file)
    records = get_records(lines)
    df = parse_records(records)
    df.to_csv('commits.csv',index=False,header=True)
    