from django.contrib.auth.hashers import PBKDF2PasswordHasher


class UserPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    iterations = PBKDF2PasswordHasher.iterations * 10
