import string as st
import random
from time import sleep


letras=st.ascii_letters
numeros=st.digits
especial=st.punctuation
tudo=(letras+numeros+especial)

while True:
    chave=input('''quer gerar uma senha [1]SIM OU [2] NÃO ''')
    if chave == '1':
        chave_user=''.join(random.choice(tudo) for _ in range(8))
        print(f'sua senha é essas {chave_user}')
        sleep(2)
      
    if chave =='2':
        print('tchau')
        break
    

    
        