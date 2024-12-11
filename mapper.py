#----HEADER---------------------------------------------------------------------------------------
# Date:     December 2024
# Authors:  Sam Rolfe, Ranvir Malik, Laila Ghabbour
# Script:   mapper.py
# Usage:    Mapper function for MapReduce of Wikipedia PageView
#*************************************************************************************************
from urllib.parse import unquote_plus
import re      # For regex pattern matching
import sys     # For stdin

# ----GLOBAL VARIABLES----------------------------------------------------------------------------
# Hard-coded page prefixes to be excluded from analysis (provided by spec.)
page_prefix_exclusions = ["Media:", "Special:", "Talk:", "User:", "User_talk:", "Project:", "Project_talk:", 
                          "File:", "File_talk:", "MediaWiki:", "MediaWiki_talk:", "Template:", "Template_talk:", 
                          "Help:", "Help_talk:", "Category:", "Category_talk:", "Portal:", "Wikipedia:", "Wikipedia_talk:"]
page_suffix_exclusions = [".jpg", ".gif", ".png", ".JPG", ".GIF", ".PNG", ".ico", ".txt"]

# ----HELPER FUNCTIONS----------------------------------------------------------------------------

# Given line of input, determine whether input is valid:
# Format: "en <page_name> <#_page_views> <file_size>"
# 1. Match only to English language Wikipedia (Proj: "en ")
# 2. Exclude pages that don't need to be considered when finding trending topics
# 3. Exclude pages not beginning in uppercase English letter
# 4. Exclude any article that ends with an image or text-file extension (jpg, gif, .png, .JPG, .GIF, .PNG, .ico, and .txt).
# 5. Exclude boilerplate pages (404_error, Main_Page, Hypertext_Transfer_Protocol, Favicon.ico, and Search).
def map(line):
    # Set regex pattern to match and extract record contents
    regex_capture = re.compile(r"(\S+)\s+(\S+)\s+(\S+)\s+(\S+)")
    match = regex_capture.match(line)

    # Confirm pattern
    if(not(match)):
        return False
    
    # Extract terms and convert to list (for mutability of 2nd term)
    terms = list(match.groups())

    # 1. Check for English language article
    if(terms[0] != "en"):
        return False
    
    # 2. Exclude hard-coded set of prefixes
    terms[1] = unquote_plus(terms[1])     # Fix percent encoding of 2nd term
    for page_prefix_exclusion in page_prefix_exclusions:
        if terms[1].startswith(page_prefix_exclusion):
            return False

    # 3. Exclude pages beginning in lowercase English letter
    if(terms[1][0].islower()):
        return False

    # 4. Exclude articles that end with an image or text-file extension
    for page_suffix_exclusion in page_suffix_exclusions:
        if terms[1].startswith(page_suffix_exclusion):
            return False
        
    # 5. Remove boilerplate pages (to do)
        
    # Map output if all criteria are met
    print(terms[1], '\t', terms[2])

#----MAIN-----------------------------------------------------------------------------------------

print("Processing lines...")
for line in sys.stdin:
    map(line)

#-------------------------------------------------------------------------------------------------
