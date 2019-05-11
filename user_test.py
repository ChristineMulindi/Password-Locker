import unittest 
from user import User  


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
 # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("ChristineMulindi","1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "ChristineMulindi")
        self.assertEqual(self.new_user.password, "1234")


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


 # Items up here...

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save user contact
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","1234")
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()
