import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
# from csv_operations import read_csv, write_csv
# from crud_operations import add_record, delete_record, update_record, read_all_records
import re

# CSV file setup
CSV_FILE = "FinanceData.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount", "Date"])  # Header row


# Functions
def add_record():
    category = entry_category.get()
    amount = entry_amount.get()
    date = entry_date.get()

    if not category or not amount or not date:
        messagebox.showerror("Input Error", "All fields are required!")
        return
    if not amount.isdigit():
        messagebox.showerror("Input Error", "Amount must be a number!")
        return
    if not category.isalpha():
        messagebox.showerror("Input Error", "Category must be alphabetic!")
        return
    date_pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(date_pattern, date):
        messagebox.showerror("Input Error", "Date must be in YYYY-MM-DD format!")
        return

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, date])
        if messagebox.askyesno('Submit Value', 'Do you confirm you want to submit values?'):
            messagebox.showinfo('Yes', 'Record added successfully!')
        else:
            messagebox.showinfo('No', 'The values are not submitted')
    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    refresh_table()

def delete_record():
    selected = table.selection()
    if not selected:
        messagebox.showerror("Error", "No record selected!")
        return
    if messagebox.askyesno("Delete Record", "Are you sure you want to delete this record?"):
        for item in selected:
            table.delete(item)
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount", "Date"])
            for row in table.get_children():
                values = table.item(row)["values"]
                writer.writerow(values)
        messagebox.showinfo("Record Deleted", "Record deleted successfully!")
    else:
        messagebox.showinfo("Delete Cancelled", "Delete operation cancelled!")


def refresh_table():
    for row in table.get_children():
        table.delete(row)
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for i, record in enumerate(reader):
            table.insert("", "end", values=(record[0], record[1], record[2]))


# Main Application Window
main_window = tk.Tk()
main_window.title("Personal Finance Tracker")
main_window.geometry("1000x600")

# Top Frame for title or header
top_frame = tk.Frame(main_window, bg="lightblue", height=50)
top_frame.pack(fill=tk.X)

header_label = tk.Label(top_frame, text="Coin Compass", font=("Aileron", 20, "bold"), bg="lightblue")
header_label.pack(pady=10)

# Second Top Frame
secondtop_frame = tk.Frame(main_window, bg="lightgray", height=30)
secondtop_frame.pack(fill=tk.X)

footer_label = tk.Label(secondtop_frame, text="Finance Tracker Application - Developed by VNRW", bg="lightgray", fg="black")
footer_label.pack(pady=5)

# Left Frame for Table
left_frame = tk.Frame(main_window, bg="white")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Right Frame for Inputs and Buttons
right_frame = tk.Frame(main_window, bg="white")
right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# Header for the Right Frame
right_frame_header = tk.Label(right_frame, text="Add Record Here", font=("Arial", 14, "bold"), bg="black")
right_frame_header.grid(row=0, column=0, columnspan=2, pady=10)

# Table (Left Frame)
table = ttk.Treeview(left_frame, columns=("Category", "Amount", "Date"), show="headings", height=20)
table.heading("Category", text="Category")
table.heading("Amount", text="Amount")
table.heading("Date", text="Date")
table.column("Category", anchor=tk.W, width=200)
table.column("Amount", anchor=tk.CENTER, width=100)
table.column("Date", anchor=tk.CENTER, width=150)
table.pack(fill=tk.BOTH, expand=True)

# Input Fields (Right Frame)
tk.Label(right_frame, text="Category (e.g., Food, Rent):", bg="black").grid(row=1, column=0, sticky="w", pady=5, padx=5)
entry_category = tk.Entry(right_frame, width=15)
entry_category.grid(row=1, column=1, pady=5)

tk.Label(right_frame, text="Amount (e.g., 100):", bg="black").grid(row=2, column=0, sticky="w", pady=5, padx=5)
entry_amount = tk.Entry(right_frame, width=15)
entry_amount.grid(row=2, column=1, pady=5)

tk.Label(right_frame, text="Date (YYYY-MM-DD):", bg="black").grid(row=3, column=0, sticky="w", pady=5, padx=5)
entry_date = tk.Entry(right_frame, width=15)
entry_date.grid(row=3, column=1, pady=5)

# Buttons
btn_add = tk.Button(right_frame, text="Add Record", command=add_record, width=15, bg="lightblue", font=("Arial", 10, "bold"))
btn_add.grid(row=4, column=0, columnspan=2, pady=10)

btn_add = tk.Button(right_frame, text="Delete Record", command=delete_record, width=15, bg="lightblue", font=("Arial", 10, "bold"))
btn_add.grid(row=5, column=0, columnspan=2, pady=10)

btn_add = tk.Button(right_frame, text="Update Record", command=add_record, width=15, bg="lightblue", font=("Arial", 10, "bold"))
btn_add.grid(row=6, column=0, columnspan=2, pady=10)

# Initialize Table with Data
refresh_table()

# Run the Application
main_window.mainloop()
