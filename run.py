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
