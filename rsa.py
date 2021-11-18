#!/usr/bin/env python3

import math 

def check_prime(a):
    if a > 1:
        for i in range(2, int(a/2)+1):
            if (a % i) == 0:
                return False
    return True

def find_n(a,b):
    return a * b

def phi_func(a,b):
    return (a - 1) * (b - 1)

def choose_e(b):
    for i in range(1,b):
        e = math.gcd(i,b)
    return i

def choose_d(e,b,i):
    p1 = e * i
    p2 = p1 % b
    e = p2
    return e

def encrypt(p,e,n):
    power = pow(p,e)
    c = power % n
    return c

def decrypt(p,e,n):
    power = pow(p,e)
    d = power % n
    return d

def main():
    
    step1 = True
    step5 = True
    step6 = True

    while step1 == True:

    # Step 1: chose 2 prime numbers
        p = int(input("Select a prime number for 'p': "))
        q = int(input("Select a prime number for 'q': "))

        p_str = str(p)
        q_str = str(q)

        if (check_prime(p) == True):
            print(p_str + ' is a prime number')
        else:
            print(p_str + ' is not a prime number')

        if (check_prime(q) == True):
            print(q_str + ' is a prime number')
        else:
            print(q_str + ' is not a prime number')
        if (check_prime(p) == True and check_prime(q) == True):
            step1 = False
        else:
            print("You must select 2 prime numbers...\n")
            step1 = True

    # Step 2: Find 'N' by multiplying the two prime numbers
    # You've Selected
    n = find_n(p,q)
    n_str = str(n)
    print('N is equal to: ' + n_str)

    # Step 3: Use the phi function to find 
    # the totient numbers that does not have a common factor with 'N'
    # AKA find the coprime numbers of 'N'
    phi_n = phi_func(p,q)
    phi_n_str = str(phi_n)
    print('phi of N is equal to: ' + phi_n_str)

    # Step 4: Choose the encryption key.
    # Has to be between 1 < e < phi(n)
    # Must be coprime with n and phi(n)
    e = choose_e(phi_n)
    e_str = str(e)
    print('Encryption key is: ' + e_str)

    # Step 5: Choose the decryption key.
    # Choose a number for 'd'
    # d * e (mod phi(n) = 1
    while step5 == True:

        d_key = int(input("Choose a decryption key number: "))
        d = choose_d(e, phi_n, d_key)
        if d != 1:
            print("Your decryption key does not equal to 1")
            step5 = True
        elif d_key == e:
            print("You cannnot use the same key as the encryption key")
            step5 = True
        else:
            d_str = str(d_key)
            print('Decryption key is: ' + d_str)
            step5 = False

    # Step 6: Encrypt the text using the generated encryption and decryption keys
    # Find out cipher text using the formula,
    while step6 == True:

        plain_text = input("Enter a plain text character: ")
        if plain_text == '' or plain_text is None:
            print("Not allowed null values")
            step6 = True
        else:
            step6 = False

    text_list = []
    encr_list = []
    decr_list = []
    print("Converting a letter into a number")
    # Converting the plain text into a number
    for i in plain_text:
        text_list.append(ord(i)-96)

    for p in text_list:
        encr_list.append(encrypt(p,e,n))
    print('Cipher text: '+ str(encr_list))

    # Step 7: Decrypt the cipher text
    for p in encr_list:
        decr_list.append(decrypt(p,e,n))

    print('Decrypted text: ' + str(decr_list))

main()
