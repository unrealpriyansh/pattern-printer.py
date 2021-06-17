n = int(input("Enter the number of rows : \n"))
print("For reverse order,type 0 and for simple order, type 1.\n")
choice=int(input("Enter choice->"))
c=bool(choice)
if c==True:    
       for i in range(0, n):  
            for j in range(0, i + 1):    
                print("* ", end="")
            print()
elif c==False:
    for i in range(n,0,-1 ):  
        for j in range(1,i+1):    
            print("* ", end="")       
        print()  

