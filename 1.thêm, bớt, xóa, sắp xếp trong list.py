juices = ["apple", 'banana']
print(len(juices)) # kết quả là 2, lenght = chiều dài 

#Thêm một phần tử ra sau list(phần tử ở vị trí số 2 tính từ 0) ta dùng juices.append()
juices.append('perl') 
print(juices[0]) #in ra apple
print(juices[2]) #in ra perl

#Để check phần tử đó nằm ở vị trí nào ta dùng juices.index
juices.index("apple") #tìm vị trí của apple
print(juices.index("apple")) #Kết quả bằng 0

#Loại bỏ phần tử trong list ta dùng juices.remove()
juices.remove('apple')  

#về soft, ta có một list 
numbers = [1,2,3,4,5,6,7,9,12,22,30]

numbers.sort()  #k ghi gì hết thì sắp xếp thì bé tới lớn
print(numbers)  #phần print sẽ hơi khác so với những phần 

numbers.sort(reverse = True) #sắp xếp chiều lớn tới bé, reverse là đảo ngược

print(numbers)