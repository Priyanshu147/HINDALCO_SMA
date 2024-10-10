import psycopg2
import numpy as np
import pandas as pd

# Database connection parameters (Update these with your database details)
db_params = {
    'dbname': 'HINDALCO',
    'user': 'postgres',
    'password': 'priyanshu',
    'host': 'localhost',
    'port': 5432
}

# Load the data from the Excel file
file_path = 'D:/priyanshu/HINDALCO/HINDALCO_1D.xlsx'
data = pd.read_excel(file_path)

# Function to insert data into PostgreSQL
def insert_data_to_postgres(data, db_params):
    # Connect to PostgreSQL
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # SQL query to insert data
    insert_query = """
    INSERT INTO stock_data (datetime, open, high, low, close, volume, instrument)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    # Insert each row of the dataframe into the database
    for _, row in data.iterrows():
        cursor.execute(insert_query, (
            row['datetime'], row['open'], row['high'], row['low'], row['close'], 
            int(row['volume']), row['instrument']
        ))

    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()

# Call the function to insert data
insert_data_to_postgres(data, db_params)

# ------- PART 2: SMA Crossover Strategy ---------

# Calculate short-term and long-term SMA
data['SMA_10'] = data['close'].rolling(window=10).mean()  # Short-term (10-day SMA)
data['SMA_50'] = data['close'].rolling(window=50).mean()  # Long-term (50-day SMA)

# Create signals based on SMA crossover
data['Signal'] = 0  # Default is no position
data.loc[10:, 'Signal'] = np.where(data['SMA_10'][10:] > data['SMA_50'][10:], 1, -1)  # Buy (1) / Sell (-1)
# Shift signals to capture the moment of crossover
data['Position'] = data['Signal'].shift(1)

# Calculate strategy performance
data['Returns'] = data['close'].pct_change()

print(data.to_string())



# ------- PART 3: Unit Testing ---------

import unittest
from datetime import datetime

class TestStockData(unittest.TestCase):
    def test_data_types(self):
        # Test 'datetime' type
        self.assertTrue(isinstance(data['datetime'].iloc[0], pd.Timestamp), "datetime column should be of datetime type")

        # Test 'open', 'high', 'low', 'close' types
        for col in ['open', 'high', 'low', 'close']:
            self.assertTrue(np.issubdtype(data[col].dtype, np.number), f"{col} column should be numeric")
        
        # Test 'volume' type
        self.assertTrue(np.issubdtype(data['volume'].dtype, np.integer), "volume column should be integer")

        # Test 'instrument' type
        self.assertTrue(isinstance(data['instrument'].iloc[0], str), "instrument column should be string")

# Run tests
if __name__ == '__main__':
    unittest.main()
