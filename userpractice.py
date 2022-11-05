# Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

class User():
    def __init__ (self,first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points=0
# Add the display_info(self) method to the User class
    def display_info(self):
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Memeber Status: {self.is_rewards_member}')
        print(f'Current Points {self.gold_card_points}')
    
# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
    def enroll(self):
        self.is_rewards_member= True
        self.gold_card_points=300
# Implement the spend_points(self, amount) method
    def spend_points(self,amount):
        # Have the first user spend 50 points
        # self.gold_card_points= self.gold_card_points-50 
        self.gold_card_points-=amount


user_account=User('Randy','Luc','hellowlrd@gmail.com',87)
user_account.display_info()
user_account.enroll()
user_account.display_info()
user_account.spend_points(50)
user_account.display_info()







