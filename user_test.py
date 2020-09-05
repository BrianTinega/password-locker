import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for user class behaviours
    '''
    new_user=User("Brian","12345")
    def SetUp(self):
        self.new_user = User ("Brian","12345")

    def test_init_(self):
        self.assertEqual(self.new_user.name,"Brian")
        self.assertEqual(self.new_user.password,"12345")
    
    def test_save_password(self):
        self.new_user.save_password()
        self.assertEqual(len(User.users_list),1)

if __name__== '__main__':
    unittest.main()

  