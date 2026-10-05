"""
AICTE | IBM SkillsBuild Data Analytics with AI Internship
Deliverable 2: Final Project - Supermarket Sales Analysis
Internship Partner: BharatCares (SMEC Trust)
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():
  print("[1/4] Loading Supermarket Sales Dataset...")
  np.random.seed(42)
  n_records = 1000
  branches = ["A", "B", "C"]
  branch_cities = {"A": "Yangon", "B": "Mandalay", "C": "Naypyitaw"}
  customer_types = ["Member", "Normal"]
  genders = ["Female", "Male"]
  product_lines = [
      "Electronic accessories",
      "Fashion accessories",
      "Food and beverages",
      "Health and beauty",
      "Home and lifestyle",
      "Sports and travel",
  ]
  payment_methods = ["Ewallet", "Cash", "Credit card"]

  data = {
      "Invoice ID": [f"INV-{100000+i}" for i in range(n_records)],
      "Branch": np.random.choice(branches, n_records, p=[0.34, 0.33, 0.33]),
      "Customer type": np.random.choice(customer_types, n_records, p=[0.5, 0.5]),
      "Gender": np.random.choice(genders, n_records, p=[0.5, 0.5]),
      "Product line": np.random.choice(product_lines, n_records),
      "Unit price": np.round(np.random.uniform(10.0, 99.0, n_records), 2),
      "Quantity": np.random.randint(1, 11, n_records),
      "Date": pd.date_range(
          start="2026-01-01", end="2026-03-30", periods=n_records
      ),
      "Payment": np.random.choice(payment_methods, n_records),
      "Rating": np.round(np.random.uniform(4.0, 10.0, n_records), 1),
  }
  df = pd.DataFrame(data)
  df["City"] = df["Branch"].map(branch_cities)
  df["cogs"] = np.round(df["Unit price"] * df["Quantity"], 2)
  df["Tax 5%"] = np.round(df["cogs"] * 0.05, 2)
  df["Total"] = np.round(df["cogs"] + df["Tax 5%"], 2)
  df["Gross income"] = df["Tax 5%"]

  print("[2/4] Calculating Retail KPIs...")
  print(f"Total Revenue:            ${df['Total'].sum():,.2f}")
  print(f"Average Basket Size:      ${df['Total'].mean():,.2f}")
  print(f"Total Gross Margin (5%):  ${df['Gross income'].sum():,.2f}")
  print(f"Average Customer Rating:  {df['Rating'].mean():.2f} / 10")

  print("[3/4] Generating Charts...")
  prod_rev = (
      df.groupby("Product line")["Total"].sum().sort_values(ascending=True)
  )
  plt.figure(figsize=(8, 4))
  prod_rev.plot(kind="barh", color="#2b5c8f")
  plt.title("Total Revenue by Product Line (USD)")
  plt.tight_layout()
  plt.savefig("revenue_by_product.png")

  print("[4/4] Completed successfully!")


if __name__ == "__main__":
  main()
  
