# from csv_operations import read_csv, write_csv


# def add_record(date, category, amount):
#     records = read_csv()
#     records.append([date, category, amount])
#     write_csv(records)


# def delete_record(date):
#     records = read_csv()
#     updated_records = [record for record in records if record[0] != date]
#     write_csv(updated_records)


# def update_record(date, category=None, amount=None):
#     records = read_csv()
#     for record in records:
#         if record[0] == date:
#             if category:
#                 record[1] = category
#             if amount:
#                 record[2] = amount
#     write_csv(records)


# def read_all_records():
#     return read_csv()
