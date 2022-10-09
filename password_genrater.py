import random
latters = [ 'a' , 'b', 'c', 'd','e','f']
numbers = ['1','2','3','4','5','6','7','8','9'] 
symbols = ['!','@','#']  
a =int(input("How much latters do you want in your password: "))   
b =int(input("How much numbers do you want in your password: "))  
c =int(input("How much symbols do you want in your password: ")) 
 
list=[]  

for char in range(1, a+1):
    list.append(random.choice(latters))
    
for char in range(1, b+1):
    list.append(random.choice(numbers))
    
for char in range(1, c+1):
    list.append(random.choice(symbols))
    
password=""
# print(list)
random.shuffle(list)
# print(list)

for char in list:
    password += char
print(f"Your random password is :{password}")

    

    