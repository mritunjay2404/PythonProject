# no_row=int(input("enter no. of rows: "))
# for row in range(1,no_row+1):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()   
# for row in range(no_row,0,-1):
#     for col in range(row-1,0,-1):
#         print(row,end=" ")
#     print()     

# no_row=int(input("enter no. of rows: "))
# for row in range(1,no_row+1):
#     for col in range(1,row+1):
#         print(f'{row}{col}',end=' ')
#     print()   
# for row in range(no_row,0,-1):
#     for col in range(row-1,0,-1):
#         print(f'{row}{col}',end=' ')
#     print()

# ch= 65

# no_row=int(input("enter no. of rows: "))
# for row in range(0,no_row+1):
#     for col in range(0,row+1):
#         print(f'{chr(ch+row)}',end=' ')
#     print()   
# for row in range(no_row,0,-1):
#     for col in range(row-1,0,-1):
#         print(f'{chr(ch+row)}',end=' ')
#     print()

# diamond using list ::::::::::::::::::::::::::::::::::::::::::::

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,1,1,1,1,1,0],
#   [0,0,1,1,1,0,0],
#   [0,0,0,1,0,0,0]
# ]
# for row in picture:
#     for col in row:
#         if col==1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# tringle type::::::::::::::::::::::::::::

# no_row=int(input("enter no. of rows: "))
# for row in range(1,no_row+1):
#     for col in range(1,no_row):
#         if col>=(no_row+1)-row:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# for row in range(no_row-1,0,-1):
#     for col in range(no_row-1,0,-1):
#         if col >=(no_row+1)-row:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# diamond:::::::::::::::::::::::

no_row=int(input("enter no. of rows: "))
for row in range(1,no_row+1):
    for col in range(1,row+1):
        if col>=(no_row+1)-row and col<=(no_row-1)+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
     