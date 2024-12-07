import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import readline
import glob
from datetime import datetime

class RepairData:
    def __init__(self, macbook_costs, harvested_part_values, repair_costs, resale_values, overhead):
        self.macbook_costs = macbook_costs
        self.harvested_part_values = harvested_part_values
        self.repair_costs = repair_costs
        self.resale_values = resale_values
        self.overhead = overhead

def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]

readline.set_completer(complete)
readline.parse_and_bind('tab: complete')

def collect_inputs():
    try:
        num_repairs = int(input("Enter the number of MacBooks repaired: "))
        if (num_repairs <= 0):
            print("Number of repairs must be positive.")
            return None

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
        return RepairData(macbook_costs, harvested_part_values, repair_costs, resale_values, overhead)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None

def import_csv():
    csv_file = input("Enter the path to the CSV file: (use TAB for file autocompletion) ")
    if not os.path.exists(csv_file):
        print("File does not exist.")
        return None
    repair_data = pd.read_csv(csv_file)
    required_columns = ["MacBook Cost ($)", "Harvested Value ($)", "Repair Cost ($)", "Resale Value ($)"]
    if not all(col in repair_data.columns for col in required_columns):
        print(f"CSV file must contain columns: {', '.join(required_columns)}")
        return None
    return repair_data

def calculate_profits(macbook_costs, harvested_part_values, repair_costs, resale_values, overhead):
    profits = [
        (resale - macbook_cost - repair_cost + harvested_value)
        for resale, macbook_cost, repair_cost, harvested_value
        in zip(resale_values, macbook_costs, repair_costs, harvested_part_values)
    ]
    total_profit = sum(profits) - overhead
    return profits, total_profit

def show_summary_table(repair_data, total_profit):
    print("\n--- Repair Summary ---")
    print(repair_data.to_string(index=False))
    print(f"\nTotal Profit after overhead ($): {total_profit:.2f}")

def plot_results(repair_data):
    plt.figure(figsize=(8, 6))
    plt.bar(repair_data["Repair #"], repair_data["Profit ($)"], color="lightgreen", label="Profit per Repair")
    plt.axhline(0, color="red", linestyle="--", label="Break-even Line")
    plt.title("Profit per Repaired MacBook")
    plt.xlabel("Repair #")
    plt.ylabel("Profit ($)")
    plt.legend()
    plt.show()

def save_data_to_csv(repair_data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"repair_data_{timestamp}.csv"
    repair_data.to_csv(filename, index=False)
    print(f"\nRepair data saved to {filename}")

def main():
    print("Welcome to MacProfitsCLI!")
    print("Calculate MacBook repair profitability for part harvesting and reselling.\n")

    print("Choose an option:")
    print("1 - Enter repair data manually")
    print("2 - Import repair data from CSV file")
    choice = input("Enter your choice: ")

    if choice == '1':
        repair_data = collect_inputs()
        if repair_data is None:
            return
        profits, total_profit = calculate_profits(repair_data.macbook_costs, repair_data.harvested_part_values, repair_data.repair_costs, repair_data.resale_values, repair_data.overhead)
        repair_data_df = pd.DataFrame({
            "Repair #": range(1, len(repair_data.macbook_costs) + 1),
            "MacBook Cost ($)": repair_data.macbook_costs,
            "Harvested Value ($)": repair_data.harvested_part_values,
            "Repair Cost ($)": repair_data.repair_costs,
            "Resale Value ($)": repair_data.resale_values,
            "Profit ($)": profits
        })
    elif choice == '2':
        repair_data_df = import_csv()
        if repair_data_df is None:
            return
        overhead = float(input("\nEnter fixed overhead costs for the period (e.g., tools, electricity) ($): "))
        repair_data_df["Profit ($)"] = repair_data_df["Resale Value ($)"] - repair_data_df["MacBook Cost ($)"] - repair_data_df["Repair Cost ($)"] + repair_data_df["Harvested Value ($)"]
        total_profit = repair_data_df["Profit ($)"].sum() - overhead
    else:
        print("Invalid choice.")
        return

    show_summary_table(repair_data_df, total_profit)
    plot_results(repair_data_df)
    save_data_to_csv(repair_data_df)

if __name__ == "__main__":
    main()