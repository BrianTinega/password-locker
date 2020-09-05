import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for user class behaviours
    '''
    new_user=User("Brian","12345")
    def SetUp(self):
        self.new_user = User ("Brian","12345")
    def tearDown(self):
        '''
        Function that clears after every test runs
        '''
        User.users_list=[]

    def test_init_(self):
        self.assertEqual(self.new_user.name,"Brian")
        self.assertEqual(self.new_user.password,"12345")
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("Mick","6789")
        test_user.save_user()
    def test_delete_user(self):
        self.new_user.save_user()
        self.new_user.delete_user()
        test_user = User("Mick","6789")
        test_user.save_user()
    def test_display_users(self):
        self.new_user.save_user()
        test_user = User ("Mick","6789")
        test_user.save_user()
        self.assertEqual(User.display_users(),User.users_list)

if __name__== '__main__':
    unittest.main()

  