# if elif else

#ticket 
#1-3(free)
#4-10(150)
#11-60(250)
#above 60 (200)

age = int(input("type ur age:"))
if age==0:
    print("u can't watch")
elif  0<age<=3:
    print("ticket price:Free")
elif 4<age<=10:
    print("ticket price:150")
elif 11<age<=60:
    print("ticket price:250")
else :
    print("ticket price:200")