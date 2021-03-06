class User:
    """
    Class that generates new instances of users.
    """

    def __init__(self, user_name, password):

        self.user_name = user_name
        self.password = password
        

    user_list = [] 


    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def find_by_user_name(cls, user_name):
        '''
        Method that takes in a user_name and returns a user that matches that number.

        Args:
            user_name: User_name to search for
        Returns :
            User of person that matches the user_name.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exist(cls,user_name, password):
        '''
        Method that checks if a user exists from the user list.
        Args:
            user_name: User_name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        
        user = ""
        for user in cls.user_list:
            if user.user_name == user_name and user.password == password :
                user = user.user_name
                return user
