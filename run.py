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
    user.save_contact()
def delete_user(user):
    '''
    
