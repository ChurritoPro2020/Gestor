import random

cl = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
lg = int(input('¿Que tan larga ser la contraseña?'))

ele = ''
for i in range (lg):
   ele += random.choice('+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') 

print(ele)
