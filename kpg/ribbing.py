def ribbing(cast_on_count: int, rows: int, expand: bool) -> None:
  if cast_on_count < 10 or cast_on_count > 500:
    print("Cast-on count must be a number between 10 and 500. Try again!")
  elif rows < 10 or rows > 500:
    print("Row count must be between 10 and 500 for this pattern. Try again!")
  else:
    print("Ribbing Knitting Pattern")
    print("Makes a vertical textured pattern.")
    print(f"Cast on {cast_on_count} stitches.")

    if expand:
      for i in range(1, rows):
        print(f"Row {i}: K1, P1 until reaching end of row.")
    else:
      print("Row 1 (and all subsequent rows): K1, P1 until reaching end of row.")
      print(f"Continue same pattern until reaching row {rows}.")

    print(f"Row {rows}: K1, P1 until reaching end of row.")
    print("Fasten off.")
