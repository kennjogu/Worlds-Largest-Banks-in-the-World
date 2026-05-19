# Worlds-Largest-Banks-in-the-World by Market Capitalization

## 📌 Overview
This project implements a Python ETL (Extract, Transform, Load) pipeline to collect and process data on the top 10 largest banks in the world by market capitalization.

The pipeline:
- Extracts bank data from a public website
- Transforms market cap values into multiple currencies
- Loads the data into a CSV file and a SQLite database

---

## 🎯 Objectives
- Extract real-world data using web scraping
- Clean and structure financial data
- Convert market capitalization into:
  - GBP (British Pound)
  - EUR (Euro)
  - INR (Indian Rupee)
- Store processed data for analysis
- Implement logging of all ETL steps

---

## 📂 Project Structure

---

## ⚙️ ETL Process

### 1. Extract
- Scrapes the top 10 banks
- Cleans market capitalization values (USD)

### 2. Transform
- Reads exchange rates from a CSV file
- Converts USD values into GBP, EUR, and INR

### 3. Load
- Saves output to:
  - CSV file (Largest_banks_data.csv)
  - SQLite database (Banks.db)

### 4. Query
Example SQL query:

SELECT * FROM Largest_banks
ORDER BY MC_USD_Billion DESC
LIMIT 5;

---

## ▶️ How to Run

pip install pandas requests beautifulsoup4
python banks_project.py

---

## ✅ Outputs
- Largest_banks_data.csv
- Banks.db
- code_log.txt

---

## 🧠 Key Learnings
- ETL pipelines
- Web scraping
- Currency transformation
- SQLite databases
- Logging

---

## 👤 Author
Ken Njogu
