def compute_ticket_price(miles):
  if miles >= 30:
      return 12
  elif 20 <= miles <= 29:
      return 10
  elif 10 <= miles <= 19:
      return 8
  else:
      return 5

def main():
  total_price = 0

  while True:
      proceed = input("Do you want to run the program? (Yes or No): ").strip().lower()
      if proceed != 'yes':
          break

      last_name = input("Enter last name: ").strip()
      miles = int(input("Enter miles from downtown Chicago: "))

      ticket_price = compute_ticket_price(miles)
      total_price += ticket_price

      print(f"The ticket price for {last_name} is: ${ticket_price:.2f}")

  print(f"Total price of all tickets: ${total_price:.2f}")

if __name__ == "__main__":
  main()
