from user import User


def create_user(uname, password):
    '''
    Function to create a new user
    '''
    new_user = User(uname, password)
    return new_user


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def find_user(user_name):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_user_name(user_name)


def check_existing_users(user_name):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(user_name)
