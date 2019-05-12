import unittest 
from user import User  
from credentials import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user and credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
 # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("ChristineMulindi","1234")
        self.new_credential = Credentials("Twitter", "Mulish", "1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "ChristineMulindi")
        self.assertEqual(self.new_user.password, "1234")

        self.assertEqual(self.new_credential.site_name, "Twitter")
        self.assertEqual(self.new_credential.site_username, "Mulish")
        self.assertEqual(self.new_credential.site_password, "1234")


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


 # Items up here...

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
            Credentials.credentials_list = []

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save user objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","1234")
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a user by user_name and display information
        '''

        self.new_user.save_user()
        test_user = User("Test", "1234")
        test_user.save_user()

        found_user = User.find_by_user_name("Test")

        self.assertEqual(found_user.user_name, test_user.user_name)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","1234")
        test_user.save_user()

        user_exists = User.user_exist("Test", "1234")

        self.assertTrue(user_exists)   

    


 #Tests for Credentials

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save credential objects to our credentials_list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("Instagram", "La", "1234")
            test_credential.save_credential()
            self.assertEqual(len(Credentials.credentials_list), 2)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials accounts
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credentials account from our credentials list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("Twitter","Musinzi","0734")
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credentials.credentials_list),1) 

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential account.
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("Test", "Jd","1234")
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist("Test")

        self.assertTrue(credential_exists)


if __name__ == '__main__':
    unittest.main()
