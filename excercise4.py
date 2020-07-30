# def check(num1,num2):
#     if num1>=num2:
#         return num1 
#     else:
#         return num2
# num1=int(input("Enter your first number : "))
# num2=int(input("Enter your second number : "))
# greater= check(num1,num2)
# print(f"{greater} is greater")

# 3 number greater @@@@@@@@@@ ########

def check(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1 
    elif num2>num3 and num2>num3:
        return num2
    else:
        return num3
num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))
num3=int(input("Enter your third number : "))
greater= check(num1,num2,num3)
print(f"{greater} is greater")