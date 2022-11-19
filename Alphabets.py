'''Printing_A'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        
        value = (num+1)//2
        if row == 1 or col == 1 or col == num or row==var:
            if size%2 == 0:
                var = value +1  
                row == var  
            else:
                var = value
                row == var
            sign = "*"
            
            if (row==1 and col==1) or ( row==1 and col==num) :
                sign = " "
        else:
            sign = " "
        print(sign,end="")
    print()
    
    
'''Printing_B'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        value = (num+1)//2
        if row == 1 or col == 1 or col ==num or row==var or row == num:
            sign = "*"
            if col == num and (row==1 or row == num or row == (num+1)//2):
                sign = " "
                
            if size%2 == 0:
                var = value +1  
                row == var 
            else:
                var = value
                row == var
            print(sign , end="")
            
        else:
            print(" ",end="")
    print()
     
        
'''Printing_C'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        
        if row == 1 or col == 1 or row ==num or (row == 2 and col == num) or (row == (num-1) and col==num):
            sign = "*"
            if (row == (num+1)//2 and col ==num) or (row == 1 and col== num) or (row == num and col == num) or (row==1 and col==1) or (row==num and col==1): 
               sign = " "
          
            
            print(sign, end="")
        else:
            print(" ",end="")
    print()        
    

'''Printing_D'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):

        if row == 1 or col == 1 or col == num or row == num:
            sign = "*"
            
            if col == num and (row==1 or row == num):
                sign = " "
            
            print(sign ,end="")
            
        else:
            print("",end=" ")
    print()
    
    
'''Printing_E'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        
        value = (num+1)//2
        if (row == 1 ) or col == 1 or row==var or row == num:
            if size%2 == 0:
                var = value +1  
                row == var 
            else:
                var = value
                row == var
            print("*" , end="")

        else:
            print(" ",end="")
    print()
    
    
'''Printing_F'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        
        value = (num+1)//2
        if (row == 1 ) or col == 1 or row==var :
            if size%2 == 0:
                var = value +1  
                row == var 
            else:
                var = value
                row == var
            print("*" , end="")
    print()

    
'''Printing_G'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        
        if row == 1 or col == 1 or row ==num or (row == 2 and col == num) or (row == (num-1) and col==num) or (row==(num-1) and (col== num-1 or col==num or col== num-2)):
            sign = "*"
            
            if (row == (num+1)//2 and col ==num) or (row == 1 and col== num) or (row == num and col == num) or (row==1 and col==1) or (row==num and col==1): 
               sign = " "
               
            print(sign, end="")
        else:
            print(" ",end="")
    print()


'''Pritning_H'''

size = int(input("Enter the size of your alphabet: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if col == 1 or col == num or row == ((num+1)//2):
            sign = "*"
            
        else:
            sign = " "
        print(sign, end="")
        
    print()

    
'''Printing_I'''

size = int(input("Enter the size of your alphabet: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row == 1 or row == num or col == ((num+1)//2):
            sign = "*"
            
        else:
            sign = " "
        print(sign, end="")
        
    print()

    
'''Printing_J'''

size = int(input("Enter the size of your alphabet: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row == 1 or row == num or (col==1 and row== num-1) or col == num:
            sign = "*"
            if (row==num and col==num) or (row==num and col==1):
                sign = " "
            
        else:
            sign = " "
        print(sign, end="")
        
    print()

    
'''Printng_K'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        trick = row+col
        if col==1 or (row==col and row>=((num+1)//2)) or (trick==(num+1) and row<((num+1)//2)):
            sign = "*"
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    

    
'''Printing_L'''

size = int(input("Enter the size of your alphabet: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row== num or col==1:
            sign="*"
            
        else:
            sign = " "
        print(sign, end="")
        
    print()

    
'''Printing_M'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        trick = row+col
        if col==1 or col==num or (col==row and row<((num+1)//2)) or (trick==(num+1) and row<=((num+1)//2)):
            sign = "*"
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    

    
'''Printing_N'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if col==1 or col==num or (col==row):
            sign = "*"
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    

    
'''Printing_O'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row == 1 or col == 1 or row ==num or col==num:
            sign = "*"
            if (row==1 and col==1) or (row==1 and col==num) or (row==num and col==1) or (row==num and col==num):
                sign = " "
            print(sign,end="")
            
        else:
            print(" ",end="")
    print()

    
'''Printing_P'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if col==1 or row==1 or row== ((num+1)//2) or col==num :
            sign = "*"
            if (col==num and row> ((num+1)//2)) or (col==num and (row==1 or row==((num+1)//2))):
                sign = " "
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    
    

'''Printing_Q'''

size = int(input("Enter a number: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row==1 or (row == 1 and col == num-1) or col == 1 or row ==num or col==num-1 or (row== (num-2) and col==(num-2)):
            sign = "*"
            if (row==1 and col==1) or (row==num and col==1) or (row==num and col==num-1) or (row==1 and col== num or row==1 and col== num-1):
                sign = " "
            
            print(sign,end="")

        else:
            print(" ",end="")
    print()

    
'''Pritning_R'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if col==1 or row==1 or row== ((num+1)//2) or col==num or (row>=((num+1)//2) and row==col):
            sign = "*"
            if (col==num and row> ((num+1)//2) and row<num) or (col==num and (row==1 or row==((num+1)//2))):
                sign = " "
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    

    
'''Printing_S'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        tip = (num+1)//2
        if row==1 or row==num or row==tip or (col==1 and row<=tip) or (col==num and row>=tip):            
            sign = "*"
            if (row==1 and col==1) or (col==num and  row==num):
                sign = " "
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()   
 

'''Printing_T'''

size = int(input("Enter the size of your alphabet: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row== 1 or col== ((num+1)//2):
            sign="*"
            
        else:
            sign = " "
        print(sign, end="")
        
    print()
   

'''Printing_U'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row== num or col==1 or col==num:   
            sign = "*"
            if row==num and (col==1 or col==num):
                sign = " "
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    

    
'''Printing_W'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        trick = row + col
        if col==1 or col==num or ((row==col and row>=((num+1)//2) or (trick==(num+1)) and row>=((num+1)//2))):
            
            sign = "*"
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    
    

'''Printing_X'''

value = int(input("Enter a number: "))
num = value

for row in range(1,num+1):
    for col in range(1,num+1):
        hint = row+col
        if row == col or hint == num+1:
            print("*" , end="")
        else:
            print(" ",end="")
    
    print()
    
'''Printing_Y'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        tip = (num+1)//2
        if ((row == col and col <= tip) or ((row+col) == num+1) and col >= tip or (col==tip and row>= tip)):   
            
            sign = "*"
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()   

    
'''Printing_Z'''

value = int(input("Enter a number: "))
num = value

for row in range(1,num+1):
    for col in range(1,num+1):
        hint = row+col
        if hint == num+1 or row == 1 or row == num:
            print("*" , end="")
        else:
            print(" ",end="")
    
    print()
