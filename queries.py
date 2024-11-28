import pandas as pd
import pandasql as ps

# Constants
CSV_FILE = "FinanceData.csv"


# Load CSV data
def load_csv():
    try:
        data = pd.read_csv(CSV_FILE)
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


# Query 1: Total income vs. total expenses
def query_total_income_vs_expenses(data):
    query = """
    SELECT 
        SUM(CASE WHEN Category = 'Income' THEN Amount ELSE 0 END) AS Total_Income,
        SUM(CASE WHEN Category != 'Income' THEN Amount ELSE 0 END) AS Total_Expenses
    FROM data;
    """
    result = ps.sqldf(query, locals())
    return result


# Query 2: List all expenses in a specific category
def query_expenses_by_category(data, category):
    query = f"""
    SELECT Date, Amount 
    FROM data 
    WHERE Category = '{category}';
    """
    result = ps.sqldf(query, locals())
    return result


# Query 3: Show the average expenses per month
def query_average_expense_per_month(data):
    query = """
    SELECT 
        strftime('%Y-%m', Date) AS Month,
        AVG(Amount) AS Avg_Expense
    FROM data
    WHERE Category != 'Income'
    GROUP BY Month;
    """
    result = ps.sqldf(query, locals())
    return result


# Query 4: Find the highest expense in a given category
def query_highest_expense(data):
    query = """
    SELECT Date, Category, Amount
    FROM data
    WHERE Amount = (SELECT MAX(Amount) FROM data WHERE Category != 'Income');
    """
    result = ps.sqldf(query, locals())
    return result


# Main execution
if __name__ == "__main__":
    data = load_csv()
    if data is not None:
        print("Total Income vs. Expenses:")
        print(query_total_income_vs_expenses(data))
        print("\nExpenses in Category 'Food':")
        print(query_expenses_by_category(data, "Food"))
        print("\nAverage Expense Per Month:")
        print(query_average_expense_per_month(data))
        print("\nHighest Expense:")
        print(query_highest_expense(data))
