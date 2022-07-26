'''Atbash Cipher'''
def main():
    '''Atbash Cipher'''
x = input()
for i in x :
    if(i.isupper()):
        a = ord(i)
        b = 155 - a 
        print(chr(b), end="")
    elif(i.islower()):
        a = ord(i)
        b = 219 - a 
        print(chr(b), end="")
    else:
        print(i, end="")
        
main()
