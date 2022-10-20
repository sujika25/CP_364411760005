"""
Name : Sujika Chuaichujit
ID : 364411760005
Group : MIT421
"""

# Exception
print("Start")

x = "MIT421"

try:
    print(x)
except NameError:
    print("Variable name not define.")
except:
    print("Something went wrong.")
else:
    print("No error.")
finally:
    print("Error has been excepted.")


print("End")