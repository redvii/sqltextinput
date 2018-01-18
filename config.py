[DEFAULT]
#For READFROM and OUTPUT, you can type either CLIPBOARD or FILE (input.txt)
READFROM = FILE
HEADER = TRUE
FILESEP = \t
OUTPUT = FILE

[BYPASS]
#use this to bypass/override autodetection of column types
#accepted bypass type volues are str, int, and float. Comma separate them. Don't use quotes.
BYPASSSWITCH = OFF
BYPASS = str

[STRINGMODS]
#use modswitch to toggle prefix/suffix use on or off
MODSWITCH = OFF
PREFIX = SELECT
SUFFIX = FROM DUAL UNION ALL