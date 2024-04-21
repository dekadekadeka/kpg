from kpg.cli import read_cli_args
from kpg.meeting_corners_square import meeting_corners_square
from kpg.stockinette import stockinette

def main():
  args = read_cli_args()
  print(args)
  if args.pattern == "garter":
    print("Garter function will go here")
  elif args.pattern == "granny_square":
    print("Granny Square function will go here")
  elif args.pattern == "meeting_corners_square":
    meeting_corners_square(args.cast_on_count, args.expand)
  elif args.pattern == "ribbing":
    print("Ribbing function will go here")
  if args.pattern == "seed":
    print("Seed function will go here")
  elif args.pattern == "stockinette":
    stockinette(args.cast_on_count, args.rows, args.expand)

if __name__ == "__main__":
  main()
