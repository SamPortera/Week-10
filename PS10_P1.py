def get_forecast_percentage(month):
  forecast_dict = {
      ('Jan', 'Feb', 'Mar'): 0.10,
      ('Apr', 'May', 'Jun'): 0.15,
      ('Jul', 'Aug', 'Sep'): 0.20,
      ('Oct', 'Nov', 'Dec'): 0.25
  }
  for months, percent in forecast_dict.items():
      if month in months:
          return percent
  return 0  # Default case if the month is invalid

def compute_next_month_sales(month, sales):
  forecast_percent = get_forecast_percentage(month)
  next_month_sales = sales * (1 + forecast_percent)
  return next_month_sales

def main():
  while True:
      proceed = input("Do you want to run the program? (Yes or No): ").strip().lower()
      if proceed != 'yes':
          break

      last_name = input("Enter last name: ").strip()
      month = input("Enter month: ").strip()
      sales = float(input("Enter sales: "))

      next_sales = compute_next_month_sales(month, sales)
      print(f"Next month's sales forecast for {last_name} is: ${next_sales:.2f}")

if __name__ == "__main__":
  main()
