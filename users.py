class UserManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        user_accounts = {}
        
    def load_users():
        print(self.user_accounts)
   
    def save_users(self, username, password):
        self.user_accounts.append[username] = username
        self.user_accounts.append[password] = password
   
    def validate_username(self, username):
        if username in self.user_accounts:
            pass
            
   
    def validate_password(self):
        while len(self.password) < 4:
            print('Password must be at least 4 characters long.')
            password = input('Enter password: ')
            save_users()
  
    def register(self):
        self.username = input('Enter username: ')
        validate_username(self)
        
        self.password = input('Enter password: ')
        validate_password(self)
        
    def login(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        
        if username in self.user_accounts and password in self.user_accounts:
            
    
class user:
    def menu():
        print('Menu:')
        print('\n (1) Register')
        print('(2) Log In')
        print('(3) Exit')
        
        choice = int(input('Enter your choice: '))
        
        while True:
            try:
                if choice == 1:
                    UserManager().register()
                elif choice == 2:
                    UserManager().log_in()
                elif choice == 3:
                    exit()
                else:
                    print('Inavalid Input.')
            except ValueError:
                print('Invalid Input.')
    
    def main_menu():
        print('\n(1) Start Game')
        print('(2) Show top scores')
        print('(3) Log Out')
        
        choice = int(input('Enter your choice: '))
        
        while True:
            try:
                if choice == 1:
                    DiceGame()
                elif choice == 2:
                    score()
                elif choice ==3:
                    menu()
                else:
                    print ("Invalid Input")
                
            except ValueError:
                print('Invald Input.')
                
        
        
        