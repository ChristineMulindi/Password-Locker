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


