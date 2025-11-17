import pandas as pd
import os

# --- CONFIGURATION ---

# 1. The name of your messy input file.
INPUT_FILENAME = "input_data.csv"

# 2. The name of the file to save the clean data to.
OUTPUT_FILENAME = "output_data_cleaned.csv"

# 3. Columns to fill missing data in, and the value to use.
#    Format: {"column_name": "value_to_fill_with"}
#    You can add multiple columns.
COLUMNS_TO_FILL = {
    "Email": "N/A",
    "Age": 0
}
# ---------------------


def main():
    """
    Main function to load, clean, and save the CSV data.
    """
    print(f"Starting CSV cleaning process for: {INPUT_FILENAME}\n")
    
    # Check if the input file exists
    if not os.path.exists(INPUT_FILENAME):
        print(f"Error: Input file not found at '{INPUT_FILENAME}'")
        print("Please create it (see implementation instructions) and try again.")
        return

    try:
        # 1. Load the data from the CSV file into a DataFrame
        df = pd.read_csv(INPUT_FILENAME)
        
        print(f"Loaded {len(df)} rows from {INPUT_FILENAME}.")
        print("--- Original Data ---")
        print(df)
        print("\n" + "="*30 + "\n")

        # 2. Clean the data
        
        # --- Step 2a: Remove duplicate rows ---
        original_row_count = len(df)
        # 'subset=None' checks all columns for duplicates.
        df_no_duplicates = df.drop_duplicates(subset=None)
        
        rows_dropped = original_row_count - len(df_no_duplicates)
        if rows_dropped > 0:
            print(f"Cleaning Step 1: Removed {rows_dropped} duplicate row(s).")
        else:
            print("Cleaning Step 1: No duplicate rows found.")

        
        # --- Step 2b: Fill in missing values (NaN) ---
        print("Cleaning Step 2: Filling in missing values...")
        # .fillna() replaces all 'NaN' (empty) values in the specified columns
        # 'inplace=True' modifies the DataFrame directly
        df_no_duplicates.fillna(value=COLUMNS_TO_FILL, inplace=True)

        
        # 3. Save the cleaned data to a new CSV file
        #    'index=False' stops Pandas from adding a new row index column
        df_no_duplicates.to_csv(OUTPUT_FILENAME, index=False)
        
        print("\n" + "="*30 + "\n")
        print(f"Cleaning complete! Cleaned data saved to: {OUTPUT_FILENAME}")
        print("--- Cleaned Data ---")
        print(df_no_duplicates)

    except pd.errors.EmptyDataError:
        print(f"Error: The file {INPUT_FILENAME} is empty.")
    except KeyError as e:
        print(f"Error: Column not found. One of the keys in 'COLUMNS_TO_FILL' ({e})")
        print("does not match a column in the CSV.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
