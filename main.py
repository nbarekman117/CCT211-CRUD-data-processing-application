# Various packages imported to create the application
import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import re

CSV_FILE = "FinanceData.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount", "Date"])

# CRUD functions
def add_record():
    '''
    This function adds a record to the CSV file and refreshes the table to display the new record.
    '''
    category = entry_category.get()
    amount = entry_amount.get()
    date = entry_date.get()

    if not category or not amount or not date:
        messagebox.showerror("Input Error", "All fields are required!")
        return
    try:
        amount = float(amount)
    except ValueError:
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
        writer.writerow([category, f"{amount:.2f}", date])
        if messagebox.askyesno('Submit Value', 'Do you confirm you want to submit values?'):
            messagebox.showinfo('Yes', 'Record added successfully!')
        else:
            messagebox.showinfo('No', 'The values are not submitted')
    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    refresh_table()


def update_record():
    '''
    This function updates a record in the CSV file and refreshes the table to display the updated record.
    '''
    selected = table.selection()
    if not selected:
        messagebox.showerror("Error", "No record selected!")
        return

    category = entry_category.get()
    amount = entry_amount.get()
    date = entry_date.get()

    if not category or not amount or not date:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a valid number!")
        return

    date_pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(date_pattern, date):
        messagebox.showerror("Input Error", "Date must be in YYYY-MM-DD format!")
        return

    if messagebox.askyesno("Update Record", "Are you sure you want to update this record?"):
        for item in selected:
            table.item(item, values=(category, f"{amount:.2f}", date))
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount", "Date"])
            for row in table.get_children():
                values = table.item(row)["values"]
                writer.writerow(values)
        messagebox.showinfo("Record Updated", "Record updated successfully!")
    else:
        messagebox.showinfo("Update Cancelled", "Update operation cancelled!")

    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_date.delete(0, tk.END)


def delete_record():
    '''
    This function deletes a record from the CSV file and refreshes the table to show the changes.
    '''
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
    '''
    This function refreshes the table to show the records from the CSV file.
    '''
    for row in table.get_children():
        table.delete(row)
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for i, record in enumerate(reader):
            table.insert("", "end", values=(record[0], record[1], record[2]))


# Application window that contains all widgets and UI
main_window = tk.Tk()
main_window.title("Personal Finance Tracker")
main_window.geometry("1000x600")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
style.configure("Treeview", rowheight=25)

# Header frame to show the title of the application
top_frame = tk.Frame(main_window, bg="lightblue", height=50)
top_frame.pack(fill=tk.X)

header_label = tk.Label(top_frame, text="Coin Compass", font=("Aileron", 20, "bold"), bg="lightblue")
header_label.pack(pady=10)

# Second highest frame to show makers of the product
secondtop_frame = tk.Frame(main_window, bg="lightgray", height=30)
secondtop_frame.pack(fill=tk.X)

footer_label = tk.Label(secondtop_frame, text="Finance Tracker Application - Developed by VNRW", bg="lightgray", fg="black")
footer_label.pack(pady=5)

# Left Frame for table of records
left_frame = tk.Frame(main_window, bg="white")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Right frame for performing CRUD operations on the records
right_frame = tk.Frame(main_window, bg="white",padx=10, pady=10)
right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# Header for the right frame
right_frame_header = tk.Label(right_frame, text="Add Record Here", font=("Arial", 14, "bold"))
right_frame_header.grid(row=0, column=0, columnspan=2, pady=10)

# Table of records on the left frame
table = ttk.Treeview(left_frame, columns=("Category", "Amount", "Date"), show="headings", height=20)
table.heading("Category", text="Category")
table.heading("Amount", text="Amount")
table.heading("Date", text="Date")
table.column("Category", anchor=tk.W, width=200)
table.column("Amount", anchor=tk.CENTER, width=100)
table.column("Date", anchor=tk.CENTER, width=150)
table.pack(fill=tk.BOTH, expand=True)

# Various input fields for creation of records on the right frame
tk.Label(right_frame, text="Category (e.g., Food, Rent):").grid(row=1, column=0, sticky="w", pady=5, padx=5)
entry_category = tk.Entry(right_frame, width=15, bg="whitesmoke")
entry_category.grid(row=1, column=1, pady=5)

tk.Label(right_frame, text="Amount (e.g., 100):").grid(row=2, column=0, sticky="w", pady=5, padx=5)
entry_amount = tk.Entry(right_frame, width=15, bg="whitesmoke")
entry_amount.grid(row=2, column=1, pady=5)

tk.Label(right_frame, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="w", pady=5, padx=5)
entry_date = tk.Entry(right_frame, width=15, bg="whitesmoke")
entry_date.grid(row=3, column=1, pady=5)

# Various CRUD-based buttons on the right frame
btn_add = tk.Button(right_frame, text="Add Record", command=add_record, width=15, bg="lightblue", font=("Arial", 10, "bold"))
btn_add.grid(row=4, column=0, columnspan=2, pady=10)

btn_delete = tk.Button(right_frame, text="Delete Record", command=delete_record, width=15, bg="lightblue", font=("Arial", 10, "bold"))
btn_delete.grid(row=5, column=0, columnspan=2, pady=10)

btn_update = tk.Button(right_frame, text="Update Record", command=update_record, width=15, bg="lightblue", font=("Arial", 10, "bold"))
btn_update.grid(row=6, column=0, columnspan=2, pady=10)

refresh_table()

main_window.mainloop()
