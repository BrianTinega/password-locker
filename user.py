class User:
    '''
    Class that generates new Usernames and passwords
    '''
    pass

    users_list=[]
    def __init__(self,name,password):
        '''
        A function to create username and password
        '''
        self.name = name
        self.password= password
    def save_user(self):
        '''
        A function that allows us to save users password
        '''
        User.users_list.append(self) 
    @classmethod
    def delete_user(cls):
        '''
        A function that deletes a users credentials
        '''
        User.users_list.remove(cls)
    @classmethod
    def display_users(cls):
        '''
        A function that displays all users saved in a user list
        '''
        return cls.users_list
    @classmethod
    def find_user_by_name(cls,name):
        '''
        Method that takes in a name and returns a contact that matches that number.

        Args:
            name:name to search for
        Returns :
           User of person that matches the number.
        '''
        for user in cls.users_list:
            if user.name == name: 
                return user.__str()
            else:
                return None
            