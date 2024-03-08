# import the get_random_secret_key() function
from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
print("SECRET KEY:", secret_key)
print("Paste above secret key into .env file")
