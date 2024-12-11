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
first_item = True
#----FUNCTIONS------------------------------------------------------------------------------------
def reduce(name, view_count):
    # Declare global variables
    global prev_key, prev_count, first_item

    # First file being read in
    if prev_key == name:
        prev_count += view_count
    else:
        if not first_item:
            print(prev_key + '\t' + prev_count, end="") 
        prev_count = view_count
        prev_key = name
        first_item = False

#----MAIN-----------------------------------------------------------------------------------------
for line in sys.stdin:
    line = line.lstrip()
    info_arr = line.split('\t')
    if (len(info_arr) != 2):
        continue
    reduce(info_arr[0], info_arr[1])
