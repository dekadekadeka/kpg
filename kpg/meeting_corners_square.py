def meeting_corners_square(cast_on_count: int, expand: bool) -> None:
  if cast_on_count % 2 == 0 or cast_on_count < 5 or cast_on_count > 499:
    print("Must be odd number between 5 and 499, otherwise this pattern will not work. Try again!")
  else:
    print("Meeting Corners Square Knitting Pattern")
    print("Makes a garter stitch square with a raised line cutting diagonally across.")
    print("One side of the square is roughly half the size of the cast-on count.")
    
    row_number: int = 1
    
    print(f"Cast on {cast_on_count} stitches.")
    print(f"Row {row_number} (WS): Knit.")

    # subtract 3 from the cast_on_count for the first pattern row
    base_row_stitch_count: int = cast_on_count - 3
    loop_end: int = 1 if expand else cast_on_count - 10

    for i in range(base_row_stitch_count, loop_end, -2): # decrease by 2 each step
      # divide by 2
      half: int = i // 2

      # increment row_number
      row_number += 1
      print(f"Row {row_number}: K{half}. Center dec. K{half}.")

      # increment row_number for right side plain row
      row_number += 1
      
      if i > 2:
        print(f"Row {row_number}: Knit.")

    if expand == False:
      print(f"Continue same pattern until 3 stiches remain.")
    print("Center dec. Fasten off remaining stitches.")
