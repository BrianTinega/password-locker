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

   
