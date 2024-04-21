def stockinette(cast_on_count: int, rows: int, expand: bool) -> None:
  if cast_on_count < 10 or cast_on_count > 500:
    print("Cast-on count must be a number between 10 and 500, otherwise this pattern will not work. Try again!")
  elif rows % 2 != 0 or rows < 10 or rows > 500:
    print("Row count must be an even number between 10 and 500 for this pattern. Try again!")
  else:
    print("Stockinette Knitting Pattern")
    print("Makes a V-shaped knit pattern on the front/right side of the project.")
    print(f"Cast on {cast_on_count} stitches.")
    print(f"Row 1 (RS): Knit.")
    print(f"Row 2 (WS): Purl.")

    if expand:
      for i in range(3, rows, 2):
        print(f"Row {i}: Knit.")
        
        if i < rows - 1:
          print(f"Row {i + 1}: Purl.")
    else:
      print(f"Continue same pattern until reaching row {rows}.")

    print(f"Row {rows} (WS): Purl.")
    print("Fasten off.")
