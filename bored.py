#no_row=int(input("enter no. of rows: "))
# for row in range(1,no_row+1):
#     for col in range(1,row+1):
#         if col>=(no_row+1)-row and col<=(no_row-1)+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

my_string=input('enter your string: ')
length= len(my_string)
# i=0
# while True:
for row in range(0,length):
    for col in range(0,length):
        if col>=(length-1)-row:
            print(my_string[col],end=' ')
        else:
            print(' ',end=' ')
    print()
for row in range(0,length-1):
    for col in range(0,length):
        if col==0 or col==length-1 or col == row:
            print(my_string[col],end=' ')
        else:
            print(' ',end=' ')
    print()

for row in range(0,length):
    for col in range(0,row+1):
        if col>=(length-1)-row and col<=(length+1)+row:
            print(my_string[col],end=' ')
        else:
            print(' ',end=' ')
    print()

for row in range(0,length):
    print(' '*(length-row-1)+my_string*(row+1))
for col in range(0,length-1):
    print(' '*(row+1)+my_string*(length-row-1))  


for row in range(0,length):
    for col in range(0,length):
        
