# dbs_bigdata_ca4
this is my ca4 final submission
content of this repository:
1. changes_python.log - text file that needs to be read and analysed
2. big_file.py - main file for reading and processing file from .log file to .CSV file using pandas dataframe.
  Calls are at the end of file so running this module will create below variables:
    * df - pandas dataframe, to call individual records use df.iloc[i] where i is record number to be called
    * lines - whole content of 'changes_python.log' file read into variable
    * records - list of 422 individual records (commits), not parsed
   Also, 'commit.csv' file is created in working directory
3. test_big_file.py - testing units to maks sure functions work properly
4. ca4.Rmd - Rmarkdown file with analysis and graphs.
