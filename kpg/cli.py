import argparse

def read_cli_args():
  parser = argparse.ArgumentParser(
    prog="kpg",
    description="Generates a knitting pattern. You select the number of cast on stitches, pattern, and number of rows."
  )
  parser.add_argument(
    "cast_on_count",
    type=int,
    help='How many stitches you cast on.'
  )
  parser.add_argument(
    "-p", "--pattern",
    type=str,
    choices=["garter", "meeting_corners_square", "ribbing", "seed", "stockinette"],
    help="Pattern style, default is stockinette.",
    default="stockinette"
  )
  parser.add_argument(
    "-r", "--rows",
    type=int,
    help="Number of rows, default is 50. Not necessary for square patterns.",
    default="50"
  )
  parser.add_argument(
    "-e", "--expand",
    action="store_true",
    help="Shows every row of the pattern, even if repetitive. Useful for printing out on paper and checking off each finished row.",
    default=False
  )
  return parser.parse_args()
