#tìm số nhỏ nhất trong list
numbers = [91,6,3,12,52,24,2]
#cách 1 có thể dùng numbers.sort() và sẽ tìm ra được min ở vị trí 0 
#cách 2, so sách từng phần tử với phần tử thứ 0
smallest = numbers[0]  
for number in numbers:
	if number < smallest:
		smallest = number
print(smallest)
print('-'*50)

#cách 3 tương tự cách 2 nhưng dùng while, 
#tô đen và ấn tổ hợp phím Ctrl + Shift + / , để ẩn cách 2 trước khi chạy cách 3 
smallest = numbers[0]
i = 0 
while i < len(numbers):
	if numbers[i] < smallest:
		smallest = numbers[i]
	i += 1  #while phải có cái này =))
print(smallest)