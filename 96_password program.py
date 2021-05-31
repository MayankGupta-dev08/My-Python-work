'''PROGRAM1'''
# import os
# import time
# #Must Access this to continue.
# def main():
#     while True:
#         UserName = input ("Enter Username: ")
#         PassWord = input ("Enter Password: ")

#         if UserName == 'admin' and PassWord == 'admin123':
#             time.sleep(30)
#             print ("Login successful!")
#             logged()
#             break

#         else:
#             print ("Password did not match!")

# def logged():
#     time.sleep(30)
#     print ("Welcome to ----")

# main()

'''PROGRAM2'''
# Example 1 : No Prompt provided by the caller
# A simple Python program to demonstrate
# getpass.getpass() to read password
# 
# import getpass
# try:
# 	p = getpass.getpass()
# except Exception as error:
# 	print('ERROR', error)
# else:
# 	print('Password entered:', p)

'''PROGRAM3'''
# Example 2 : Security Question
# A simple Python program to demonstrate
# getpass.getpass() to read security question

# import getpass

# p = getpass.getpass(prompt='Your favorite flower? ')

# if p.lower() == 'rose':
# 	print('Welcome..!!!')
# else:
# 	print('The answer entered by you is incorrect..!!!')

'''PROGRAM4'''
# Example 3 of getuser()
# Python program to demonstrate working of
# getpass.getuser()

import getpass
user = getpass.getuser()
print(user)

while True:
	pwd = getpass.getpass("User Name : %s" % user)
	if pwd == 'ank8':
		print("Welcome!!!")
		break
	else:
		print("The password you entered is incorrect.")
print(pwd)
