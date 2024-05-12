import random
import string
class PasswordGenerator:
    def __init__(self):
        pass
    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    password_generator = PasswordGenerator()
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        exit()

generated_password = password_generator.generate_password(length)
print("Generated Password:", generated_password)