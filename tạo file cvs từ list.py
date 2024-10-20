#tạo một file csv từ list 
#tới bước đây t làm hong có chú thích, ai hog hiểu thì hỏi t 
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['January', 'February', 'March', 'April', 'May', 'Jun', 'July', 'August', 'September', 'October', 'November', 'December']

file = open("month.csv", "w")
file.write("Meo, meo, meo\n")  # Đảm bảo rằng tiêu đề sử dụng dấu phẩy

for i in range(12):
    row = "{},{},{}\n".format(i+1, months[i], days[i])
    file.write(row)

file.close()