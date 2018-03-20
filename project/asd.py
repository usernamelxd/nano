import os
import codecs


def getData(path):
    if not os.path.exists(path):
        return "aaa"
    file = codecs.open(path, "rb", encoding="utf-8", errors="ignore")
    myList = file.readlines()
    return myList
    # print(myList)

path = r'甘肃省.csv'
data = getData(path)
# print(data)
car_list= []
a = 0

for lines in data:

    lines = lines.split(",")
    if lines[0] == "湖南":

        car_list.append(lines[7])
        a+=1
print(car_list)
print(a)
print(type(car_list))


    # if lines[0] == "云南":
    #     car_list.add(str(lines[7]))
    #     plate_list.add(str(lines[8]) + str(lines[9]) + str(lines[10] + str(lines[11])))



path1 = r'江苏.txt'
f = open(path1,'wb')
f.write(car_list)