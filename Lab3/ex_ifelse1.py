"""
Name : Sujika Chuaichujit
ID : 364411760005
Group : MIT421
"""

"""
วิธีการรับประทานยาพาราเวตามอล
อายุต่ำกว่า10ปีไม่ควรรับประทาน
อายุ 10-15 ทานครั้งละ 1 เม็ด  10 <= age <= 15
อายุ 16-20 ทานครั้งละ 1.5 เม็ด
อายุ 20 ปีขึ้นไป ทานครั้งละ 2 เม็ด
"""

# if-else-if


# ถ้าอายุน้อยกว่า 20 คือเด็ก ถ้ามากกว่าหรือเท่ากับ 20 คือผู้ใหญ่
print("ระบบแนะนำการรับประทานยาพาราเซตามอล\n")
age = float(input("คุณอายุเท่าไหร่? : "))

if age < 10:
    print("ห้ามรับประทาน.")
elif age >= 10 and age <= 15:
    print("รับประทานครั้งละ 1 เม็ด.")
elif age >= 16 and age <= 20:
    print("รับประทานครั้งละ 1.5 เม็ด.")
else:
    print("รับประทานครั้งละ 2 เม็ด.")


print("ขอบคุณครับ/ค่ะ")
