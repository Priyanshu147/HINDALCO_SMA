# Stock Data Analysis and Simple Moving Average (SMA) Crossover Strategy

This project loads stock data from an Excel file, inserts it into a PostgreSQL database, and applies a Simple Moving Average (SMA) crossover strategy for trading signals. The strategy compares the performance of the trading signals with the market returns. Additionally, unit tests are implemented to validate the data types in the stock data.

## Features

- **PostgreSQL Integration**: Insert stock data into a PostgreSQL database.
- **SMA Crossover Strategy**: A trading strategy using two moving averages (short-term and long-term).
- **Performance Comparison**: Compare cumulative returns of the strategy and market.
- **Unit Testing**: Ensures that the stock data columns are of the correct data type.

## Prerequisites

Make sure you have the following software installed:

- **Python 3.x** (Python 3.6 or higher is recommended)
- **PostgreSQL**: Install PostgreSQL or have access to a PostgreSQL database.
- **pip**: Python package installer
- **virtualenv** (optional but recommended)



## Database Setup

Make sure you have PostgreSQL running, and create a database named `HINDALCO`. Create a table to store the stock data with the following schema:

```sql
CREATE TABLE stock_data (
    datetime TIMESTAMP,
    open DECIMAL,
    high DECIMAL,
    low DECIMAL,
    close DECIMAL,
    volume INTEGER,
    instrument VARCHAR(50)
);
# HINDALCO_SMA
