import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import glob
import readline

def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]

readline.set_completer(complete)
readline.parse_and_bind('tab: complete')

def main():
    print("Welcome to MacProfitsCLI!")
    print("Calculate MacBook repair profitability for part harvesting and reselling.\n")

    # Step 1: Collect Inputs
    try:
        num_repairs = int(input("Enter the number of MacBooks repaired: "))
        if num_repairs <= 0:
            print("Number of repairs must be positive.")
            return

        macbook_costs = []
        harvested_part_values = []
        repair_costs = []
        resale_values = []

        for i in range(num_repairs):
            print(f"\nRepair #{i + 1}")
            macbook_cost = float(input("  Enter cost of broken MacBook ($): "))
            harvested_value = float(input("  Enter value of parts harvested from this MacBook ($): "))
            repair_cost = float(input("  Enter cost of parts/supplies for repair ($): "))
            resale_value = float(input("  Enter resale value of repaired MacBook ($): "))

            macbook_costs.append(macbook_cost)
            harvested_part_values.append(harvested_value)
            repair_costs.append(repair_cost)
            resale_values.append(resale_value)

        overhead = float(input("\nEnter fixed overhead costs for the period (e.g., tools, electricity) ($): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Step 2: Calculate Profits
    profits = [
        (resale - macbook_cost - repair_cost + harvested_value)
        for resale, macbook_cost, repair_cost, harvested_value
        in zip(resale_values, macbook_costs, repair_costs, harvested_part_values)
    ]
    total_profit = sum(profits) - overhead

    # Step 3: Show Summary Table
    repair_data = pd.DataFrame({
        "Repair #": range(1, num_repairs + 1),
        "MacBook Cost ($)": macbook_costs,
        "Harvested Value ($)": harvested_part_values,
        "Repair Cost ($)": repair_costs,
        "Resale Value ($)": resale_values,
        "Profit ($)": profits
    })

    print("\n--- Repair Summary ---")
    print(repair_data.to_string(index=False))
    print(f"\nTotal Profit after overhead ($): {total_profit:.2f}")

    # Step 4: Plot Results
    plt.figure(figsize=(8, 6))
    plt.bar(repair_data["Repair #"], repair_data["Profit ($)"], color="lightgreen", label="Profit per Repair")
    plt.axhline(0, color="red", linestyle="--", label="Break-even Line")
    plt.title("Profit per Repaired MacBook")
    plt.xlabel("Repair #")
    plt.ylabel("Profit ($)")
    plt.legend()
    plt.show()

    # Step 5: Save data to a CSV file that's timestamped.
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"repair_data_{timestamp}.csv"
    repair_data.to_csv(filename, index=False)
    print(f"\nRepair data saved to {filename}")



if __name__ == "__main__":
    main()
