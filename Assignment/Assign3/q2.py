"""
Name : Sujika Chuaichujit
ID : 364411760005
Group : MIT421
"""

#2 เขียนฟังก์ชันเพื่อยกกำลังสองสมาชิกทุกตัวใน list และ return list ที่เป็นผลลัพธ์จากการยกกำลังสองออกมา
# กำหนดให้ฟังก์ชันนี้รับ parameter 1 ตัว คือ listA ที่มีสมาชิกเป็นจำนวนใด ๆ

list = [10,20,30]
power = 2

for x in range(len(list)):
    print(list[x],"ยกกำลัง",power,"เท่ากับ",pow(list[x], power))

# function
'return'
def myfunction(list):
    # return statement
    return 10,20,30
# calling function with parameter and return statement
print(myfunction(list))