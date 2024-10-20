import csv


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['January', 'February', 'March', 'April', 'May', 'Jun', 'July', 'August', 'September', 'October', 'November', 'December']

file = open("month1.csv", "w", newline = "")
csv_month = csv.writer(file)

csv_month.writerow(["Months", "Name", "Days"])  # Đảm bảo rằng tiêu đề sử dụng dấu phẩy

for i in range(12):
    row = [i+1, months[i], days[i]]
    csv_month.writerow(row)

file.close()