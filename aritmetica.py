n1 = int(input())
s1 = input("")
n2 = int(input())
s2 = input("")
n3 = int(input())
op1 = int(0)

if (s1 == "*") or (s1 == "/"):
    if s1 == "*":
        op1 = int(n1*n2)

    elif s1 == "/":
        if n2 == 0:
            print("erro", end="")
            quit()
        else: op1 = int(n1/n2)

    if s2 == "*":
        print(op1*n3, end="")
    
    elif s2 == "/":
        if n3 == 0:
            print("erro", end="")
            quit()
        else: print(op1/n3, end="")
    
    elif s2 == "+":
        print(op1+n3, end="")

    elif s2 == "-":
        print(op1-n3, end="")

else:

    if s2 == "*":
        op1 = n2*n3
    
    elif s2 == "/":
        if n3 == 0:
            print("erro", end="")
            quit()
        else: op1 = int(n2/n3)
    
    elif s2 == "+":
        op1 = n2+n3

    elif s2 == "-":
        op1 = n2-n3

    if s1 == "+":
        print(n1+op1, end="")
    
    elif s1 == "-":
        print(n1-op1, end="")








#elif s2 == "*":
#    op1 = int(n2*n3)
#
#elif s2 == "/":
#    if n3 == 0:
#        print("erro", end="")
#        quit()
#    else: op1 = int(n2/n3)
#
#else: 
#    if s1 == "+":
#        op1 = n1+n2
#    
#    elif s1 == "-":
#        op1 = n1-n2









    
    

