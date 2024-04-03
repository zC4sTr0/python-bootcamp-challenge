class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0
        print("Creating a new user")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "GabrielCastro")
print(user_1.id)
user_2 = User("002", "Joao")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)