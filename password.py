import string
import random
print('\n----PASSWWORD GENERATOR----\n\n')
print("Enter password length:")
PassLength=int(input())
random1=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,k=PassLength))
print('Following is your generated Password: ' 
      +random1)
