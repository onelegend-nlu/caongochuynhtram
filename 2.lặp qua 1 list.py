names = ["Dung", "Lai", "Huy", "Le"]
#cách 1, dùng while
i = 0
while i < len(names):
	print(names[i])
	i += 1


#cách 2, dùng for. 
#note thêm: ở hàm for dưới đây, giá trị của i sẽ tự động reset nên không cần lo lắng về việc lỗi ở trên 
print("-"*50)
for i in range(len(names)):
	print(names[i])

#cách 3 
print("-"*50)
for name in names:   
	print(name)

#nếu chúng ta for name(tự đặt) in names(một danh sách), 
#thì giá trị name(tự đặt) sẽ lần lượt bằng các phần tử trong list(names)
#có thể thay đổi name thành tên khác nếu muốn
for a in names:
	print(a)