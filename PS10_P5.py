def get_assessed_value_percent(county):
  county = county.lower()
  assessed_values = {
      "cook": 0.90,
      "dupage": 0.80,
      "mchenry": 0.75,
      "kane": 0.60
  }
  return assessed_values.get(county, 0.70)  # Default to 0.70 for all others

def compute_assessed_value(county, market_value):
  assessed_percent = get_assessed_value_percent(county)
  return market_value * assessed_percent

def main():
  total_market_value = 0
  total_assessed_value = 0

  while True:
      proceed = input("Do you want to run the program? (Yes or No): ").strip().lower()
      if proceed != 'yes':
          break

      county = input("Enter county: ").strip()
      market_value = float(input("Enter market value of the home: "))

      assessed_value = compute_assessed_value(county, market_value)

      total_market_value += market_value
      total_assessed_value += assessed_value

      print(f"The assessed value for the home in {county} County is: ${assessed_value:.2f}")

  print(f"Total market value of all homes: ${total_market_value:.2f}")
  print(f"Total assessed value of all homes: ${total_assessed_value:.2f}")

if __name__ == "__main__":
  main()
