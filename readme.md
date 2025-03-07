# KPG
A command-line knit pattern generator created in Python.

## Usage
`python3 -m kpg [-h] [-p {garter,meeting_corners_square,ribbing,seed,stockinette}] [-r ROWS] [-e] cast_on_count`

### -h
Show help message

### -p/--pattern (string)
Choose which pattern (garter, meeting_corners_square, ribbing, seed, stockinette) you will generate. Default is stockinette.
Each pattern has an explanation in the header.

### -r/--rows (integer)
Number of rows, default is 50. Not necessary for Meeting Corners Square. Must be an even number for stockinette, all other patterns accept any number between 10 and 500.

### -e/--expand (boolean)
Show EVERY row to be worked in the pattern, not just an abbreviated version. Useful for printing on paper and checking off as you work each row, and to get an idea of the scope of a project.

### cast_on_count (integer)
Positional (mandatory) argument. If you don't pass in any other arguments, you need to pass in this one. 50 is a good one to use with the default values.
 - Must be between 10 and 500 (9 and 499 for Meeting Corners Square)
 - Must be an even number for Ribbing and Seed
 - Must be an odd number for Meeting Corners Square
 
 Don't worry about remembering all these, if you make a mistake you will receive an error message telling you what to do :)