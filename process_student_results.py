import pandas as pd

# 1. Load the two datasets
math_df    = pd.read_excel("dataset_math_only.xlsx")
science_df = pd.read_excel("dataset_science_only.xlsx")

# 2. Prompt user for roll numbers
math_roll    = input("Enter the Math roll number (e.g. R007): ").strip()
science_roll = input("Enter the Science roll number (e.g. R012): ").strip()

# 3. Look up each row
row_math = math_df[math_df["Roll Number"] == math_roll]
row_sci  = science_df[science_df["Roll Number"] == science_roll]

# 4. Check we found them
if row_math.empty:
    print(f"No Math entry found for roll number {math_roll}")
if row_sci.empty:
    print(f"No Science entry found for roll number {science_roll}")

# 5. Combine and write to results.xlsx
if not row_math.empty and not row_sci.empty:
    results = pd.concat([row_math, row_sci], ignore_index=True)
    results.to_excel("results.xlsx", index=False)
    print("✅ Written matching entries to results.xlsx")
