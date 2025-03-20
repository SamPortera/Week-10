def compute_square_footage(length, width, height):
  square_footage = (2 * length * width) + (2 * length * height) + (2 * width * height)
  return square_footage

def compute_gallons_needed(square_footage):
  return square_footage / 50

def main():
  while True:
      proceed = input("Do you want to run the program? (Yes or No): ").strip().lower()
      if proceed != 'yes':
          break

      length = float(input("Enter length of the room: "))
      width = float(input("Enter width of the room: "))
      height = float(input("Enter height of the room: "))

      square_footage = compute_square_footage(length, width, height)
      gallons_needed = compute_gallons_needed(square_footage)

      print(f"The number of gallons needed to paint the room is: {gallons_needed:.2f}")

if __name__ == "__main__":
  main()
