class User:
    login_attempts = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.password = None
        self.email = None

    def describe_user(self):
        print(f"The first name {self.first_name}")
        print(f"The last name {self.last_name}")
        print(f"Email {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} Welcome to my heart")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1=User('Ahmad' , 'Sami')
user2=User('Sami' , 'Ahmad')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3=User("Hamza" , "Mohammad")
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()

print(user1.login_attempts)
print(user3.login_attempts)

user3.reset_login_attempts()
print(user3.login_attempts)