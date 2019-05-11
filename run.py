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


def main():
    print("Hello Welcome to Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}.")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new user, fc -find a user, ex -exit the contact list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New User")
            print("-"*10)

            print("User name ....")
            user_name = input()

            print("Password ...")
            password = input()

                           
            # create and save new user.
            save_users(create_user(user_name, password))
            print('\n')
            print(f"New User {user_name} created")
            print('\n')

                   
        elif short_code == 'fc':
            print("Enter the username you want to search for")
            search_user_name = input()
            if check_existing_users(search_user_name):
                search_user_name = find_user(search_user_name)
                print(f"{search_user_name.user_name}")
                print('-' * 20)

            else:
                print("That contact does not exist")

        elif short_code == "ex":
             print("Bye .......")
             break
        else:
             print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()

