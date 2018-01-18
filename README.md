# sqltextinput
Program for converting columns of values from Excel/CSVs/Clipboard to a SQL-digestable format

1) Open config.py and set the parameters
2) Data will be read from input.txt by default
2) Run main.py
3) Results will be outputted to either your clipboard, our output.txt based on your

-------------------------------------------------------------------------
Parameter options

READFROM: either FILE or CLIPBOARD. If FILE, script will read from input.txt. If CLIPBOARD, script will read from whatever you have copied most recently.

HEADER: TRUE or FALSE, depending on whether your input table has headers or not.

FILESEP: how your table's columns are separated. Can be values such as "\t" for tab-delimited, or "," for comma delimited (without the quotes)

OUTPUT: either FILE or CLIPBOARD. If FILE, script will output to output.txt.

BYPASSSWITCH: either ON or OFF. If OFF, the script will automatically detect your table's column types (string, float, etc.)
BYPASS = either STR, FLOAT, or INT. If you have multiple columns, you can comma separate their data types in order eg. "str, int, int, str, float" (without the quotes)

MODSWITCH: either ON or OFF. If ON, the script will add prefixes and suffixes to each data row. This is useful for SQL processing.
PREFIX: any value, such as "SELECT"
SUFFIX: any value, such as "FROM DUAL UNION ALL"
