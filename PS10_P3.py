def get_discount_percentage(make, model, ev_code):
  if ev_code.upper() == 'Y':
      return 0.30
  elif make.lower() == 'honda' and model.lower() == 'accord':
      return 0.10
  elif make.lower() == 'toyota' and model.lower() == 'rav4':
      return 0.15
  else:
      return 0.05

def compute_out_the_door_price(msrp, make, model, ev_code):
  discount_percent = get_discount_percentage(make, model, ev_code)
  discounted_price = msrp * (1 - discount_percent)
  total_price = discounted_price * 1.07  # Adding 7% sales tax
  return total_price

def main():
  total_msrp = 0
  total_sales_price = 0

  while True:
      proceed = input("Do you want to run the program? (Yes or No): ").strip().lower()
      if proceed != 'yes':
          break

      make = input("Enter car make: ").strip()
      model = input("Enter car model: ").strip()
      ev_code = input("Is it an electric vehicle? (Y or N): ").strip()
      msrp = float(input("Enter MSRP (sticker price): "))

      total_price = compute_out_the_door_price(msrp, make, model, ev_code)

      total_msrp += msrp
      total_sales_price += total_price

      print(f"The out-the-door price for the {make} {model} is: ${total_price:.2f}")

  print(f"Total MSRP of all cars: ${total_msrp:.2f}")
  print(f"Total sales price of all cars: ${total_sales_price:.2f}")

if __name__ == "__main__":
  main()
