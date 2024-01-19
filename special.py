a=eval(input ("enter a character"))
if a in '0123456789':
    print('digit')
elif a>='a' and a<='z':
    print ("upper case")
elif a>='a' and a<='z':
    print("lower case")
else:
    print("special character")
    
