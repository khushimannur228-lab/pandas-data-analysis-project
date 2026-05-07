import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
csv_file_path = '/content/sample_data/california_housing_test.csv'

print(f"Loading data from: {csv_file_path}")

try:
    df = pd.read_csv(csv_file_path)
    print("\n Dataset loaded successfully!")

    # Show first rows
    print("\nFirst 5 rows:")
    print(df.head())

    # Basic info
    print("\nDataset Info:")
    df.info()

    # Descriptive stats
    print("\nDescriptive Statistics:")
    print(df.describe())

    # ---------------------------
    #  Data Cleaning
    # ---------------------------
    print("\nCleaning data...")
    df = df.dropna()
    print("Missing values removed")

    # ---------------------------
    #  Filtering
    # ---------------------------
    print("\nFiltering houses with high income (>5):")
    high_income = df[df['median_income'] > 5]
    print(high_income.head())

    # ---------------------------
    #  Grouping
    # ---------------------------
    print("\nGrouping by housing age (average house value):")
    grouped = df.groupby('housing_median_age')['median_house_value'].mean()
    print(grouped.head())

    # ---------------------------
    #  Insights
    # ---------------------------
    print("\n Insights:")

    avg_price = df['median_house_value'].mean()
    max_price = df['median_house_value'].max()

    print(f"Average house price: {avg_price}")
    print(f"Maximum house price: {max_price}")

    print("Higher income areas tend to have higher house prices.")

    # ---------------------------
    #  Graph 
    # ---------------------------
    print("\nGenerating graph...")
    df['median_house_value'].hist()
    plt.title("House Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.show()

except Exception as e:
    print(f"Error: {e}")
