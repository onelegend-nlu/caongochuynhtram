file = open('data.txt', mode="w")  # w = writing, r = reading
file.write("5\n")
file.write("Pham\n")
file.write("Tan\n")
file.write("Phat\n")
file.write("Đep\n")
file.write("Trai\n")
file.close()

file = open('data.txt', "r")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
file.close()
