'''
Created on Mar 5, 2013

@author: Rizky
'''
def encrypt():
    encrypt=eval(input("Input the number that want to be encrypted :\t"))
    encrypt[1] = (encrypt[1]+7)%10
    encrypt[2] = (encrypt[2]+7)%10
    encrypt[3] = (encrypt[3]+7)%10
    encrypt[4] = (encrypt[4]+7)%10
    encrypt[1],encrypt[3] = encrypt[3],encrypt[1]
    encrypt[2],encrypt[4] = encrypt[4],encrypt[2]

def decrypt():
    decrypt=eval(input("Input the number that want to be decrypted :\t"))
    decrypt[1],decrypt[3] = decrypt[3],decrypt[1]
    decrypt[2],decrypt[4] = decrypt[4],decrypt[2]
    