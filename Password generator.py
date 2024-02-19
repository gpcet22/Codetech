# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:18:58 2024

@author: Rakesh
"""

import random
import string

def generate_password(length, complexity):
    if complexity not in ["low", "medium", "high"]:
        print("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")
        return None

   

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if complexity == "low":
        chars = lowercase_letters + uppercase_letters + digits
    elif complexity == "medium":
        chars = lowercase_letters + uppercase_letters + digits + symbols
    else:
        chars = lowercase_letters + uppercase_letters + digits + symbols

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        complexity = input("Choose complexity level (low, medium, high): ").lower()
        
        password = generate_password(length, complexity)
        
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__== "__main__":
    main()