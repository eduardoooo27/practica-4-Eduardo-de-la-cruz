
#problemas de ficheros

from sympy import re


n=0
while n<1 or n>10:
     n=int(input("ingrese un nro del 1 al 10: " ))


with open(f"./tabla-{n}.txt","w") as f:
    for i in range(1,13):
        texto=f"{i}x{n}={i*n}\n"
        f.write(texto)
        


for i in range(1,13):
    print(f"{i}x{n}={i*n}\n")    #para multiplicacion 




#problema 2 

n = int(input("Introducir numero del 1 al 10: "))
file = "tabla-{n}.txt"
try: 
    f = open(file, 'r')
except FileNotFoundError:
  
    print('No existe el fichero de la tabla del', n)
else:
    print(f.read())



#problema 3

m= int(input("Introducir numero del 1 al 10: "))
file = "tabla-{m}.txt"
try: 
    f = open(file, 'r')
except FileNotFoundError:
  
    print('No existe el fichero de la tabla del', m)
else:
    print(f.read())

  

#problemas de expresiones regulares



#problema 4

regex = r""

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   


