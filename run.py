#!/usr/bin/env python3.6
from user import User

def sign_up(name,password):
    '''
    A function that allows a user to sign up
    '''
    new_user = User(name,password)
    return new_user
def save_user(user):
    '''
    A function that saves users credentials
    '''
    user.save_user()
def delete_user(user):
    '''
    A function that deletes a user upon request
    '''
    user.delete_user_credential()
def display_users():
    '''
    A function that displays all registered users
    '''
    return User.display_users()

def main():
    print("Welcome to password locker..What is your name?")
    user_name = input()
    print(f"Welcome {user_name} use the following commands: su-signup,del-delete, dis-display users, ex-exit")
    while True:
        commands = input().lower()
        if commands == 'su':
            print("New User")
            print("-"*10)
            print("Enter your username")
            name = input()
            print("Enter your password")
            password = input()
            save_user(sign_up(name,password))
            print(f"New User{name} and {password} created successfully")
       
        elif commands == 'dis':
            if display_users():
                print("the following is a list of users you've created")
                for user in display_users():
                    print(f"{user.name} {user.password}")
            else:
                print("No users created yet")           
        elif commands == 'del':
            user == input().su
            delete_user(user) 
            print("Delete successful")
          
        elif commands == 'ex':
            print("Goodbye")
            break
        else:
            print("Kindly use the above codes only")  
               
            
                

               
           

                   
                        
                    


main()
                
               