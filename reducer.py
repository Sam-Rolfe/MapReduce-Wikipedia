#----HEADER---------------------------------------------------------------------------------------
# Date:     December 2024
# Authors:  Sam Rolfe, Ranvir Malik, Laila Ghabbour
# Script:   reducer.py
# Usage:    Reducer function for MapReduce of Wikipedia PageView
#*************************************************************************************************
import sys

# ----GLOBAL VARIABLES----------------------------------------------------------------------------
prev_key = ""
prev_count = 0
item_count = 0
#----FUNCTIONS------------------------------------------------------------------------------------
def reduce(name, view_count):
    # First file being read in
    if prev_key == name:
        prev_count += view_count
    else:
        if item_count != 0:
            print(prev_key + '\t' + prev_count) 
        prev_count = view_count
        prev_key = name
        item_count = 1

#----MAIN-----------------------------------------------------------------------------------------
for line in sys.stdin:
    info_arr = line.split('\t')
    if (len(info_arr) != 2):
        print(info_arr)
    # reduce(info_arr[0], info_arr[1])
