class Credentials:
    """
    Class that generates new instances of credentials.
    """

    def __init__(self, site_name, site_username, site_password):
        self.site_name = site_name
        self.site_username = site_username
        self.site_password = site_password

    credentials_list = []

    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''

        Credentials.credentials_list.append(self)


    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    def delete_credential(self):

        '''
        delete_credential method deletes a credentil account from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
    
    @classmethod
    def credential_exist(cls, site_name):
        '''
        Method that checks if a credential account exists from the contact list.
        Args:
            site_name: Site_name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                    return True

        return False

