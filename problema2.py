


import re
repeticiones=["42536258796157867 "    
"4424444424442444 "     
"5122-2368-7954 - 3214"   
"44244x4424442444 "       
"0525362587961578"]

regex=r""

regex=r"[456]\\d{3}\\d{4}\\d{4}"
repeticiones = [ str(i)*4 for i in range(10)]


for tarjeta in repeticiones:
   tarjeta = tarjeta.strip()

   if re.search(regex, tarjeta):
        new_tarjeta = tarjeta.replace('-','')
        rep = [ True  for repeticion in repeticiones if re.search(repeticion, new_tarjeta)]
        if not rep:
            print( f'{tarjeta} -> Valid')
                
            continue
                
   print( f'{tarjeta} -> Invalid')


#


import re
from typing import Text

from matplotlib.pyplot import text
Text= [
   [ "4123456789123456"
     "5123-4567-8912-3456"
     "61234-567-8912-3456"
     "4123356789123456"
     "5133-3367-8912-3456"
    "5123 - 3567 - 8912 - 3456"

    ]
]

     
source= [] 

text= open("./src/text.txt").readlines()

    