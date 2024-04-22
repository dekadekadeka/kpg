from kpg.cli import read_cli_args
from kpg.garter import garter
from kpg.meeting_corners_square import meeting_corners_square
from kpg.ribbing import ribbing
from kpg.seed import seed
from kpg.stockinette import stockinette

def main():
  args = read_cli_args()
  if args.pattern == "garter":
    garter(args.cast_on_count, args.rows, args.expand)
  elif args.pattern == "granny_square":
    print("Granny Square function will go here")
  elif args.pattern == "meeting_corners_square":
    meeting_corners_square(args.cast_on_count, args.expand)
  elif args.pattern == "ribbing":
    ribbing(args.cast_on_count, args.rows, args.expand)
  if args.pattern == "seed":
    seed(args.cast_on_count, args.rows, args.expand)
  elif args.pattern == "stockinette":
    stockinette(args.cast_on_count, args.rows, args.expand)

if __name__ == "__main__":
  main()
