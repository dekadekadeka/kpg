def seed(cast_on_count: int, rows: int, expand: bool) -> None:
  if cast_on_count < 10 or cast_on_count > 500:
    print("Cast-on count must be a number between 10 and 500. Try again!")
  elif rows < 10 or rows > 500:
    print("Row count must be between 10 and 500 for this pattern. Try again!")
  else:
    print("Seed Knitting Pattern")
    print("Makes a bumpy, diagonal textured pattern.")
    print(f"Cast on {cast_on_count} stitches.")

    loop_end: int = rows if expand else 2

    for i in range(1, loop_end):
      print(f"Row {i}: K1, P1 until reaching end of row.")
      print(f"Row {i + 1}: P1, K1 until reaching end of row.")


    if expand == False:
      print(f"Continue same pattern until having finished {rows} rows.")
    print("Fasten off.")
