"""
Name : Sujika Chuaichujit
ID : 364411760005
Group : MIT421
"""

#3 เขียนฟังก์ชัน Calculator(a,b,op) โดยรับ parameter 3 ตัว ได้แก่ a, b ซึ่งเป็นจำนวนใดๆ และ op ซึ่ง
# เป็นสายอักขระที่เป็นไปได้ 4 แบบ คือ +, -, *, /
# • ถ้า op เป็น + ให้ return a+b
# • ถ้า op เป็น - ให้ return a-b
# • ถ้า op เป็น * ให้ return a*b
# • ถ้า op เป็น / ให้ return a/b

a = int(input("function1 : "))
b = int(input("function2 : "))
op = str(input("function3 : "))
def Calculator(a,b,op):
    if a=+b:
        print(a+b)
    else:
        print(a-b)
