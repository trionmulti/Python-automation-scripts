import pandas as pd
import os

INPUT_FILENAME = "input_data.csv"
OUTPUT_FILENAME = "output_data_cleaned.csv"
COLUMNS_TO_FILL = {"Email": "N/A", "Age": 0}

def main():
    print(f"Cleaning: {INPUT_FILENAME}")
    if not os.path.exists(INPUT_FILENAME):
        print("Error: Input file not found.")
        return

    try:
        df = pd.read_csv(INPUT_FILENAME)
        print(f"Original rows: {len(df)}")
        
        df_no_duplicates = df.drop_duplicates()
        df_no_duplicates.fillna(value=COLUMNS_TO_FILL, inplace=True)
        
        df_no_duplicates.to_csv(OUTPUT_FILENAME, index=False)
        print(f"Cleaned data saved to: {OUTPUT_FILENAME}")
        print(df_no_duplicates)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
