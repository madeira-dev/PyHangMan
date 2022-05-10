class login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_login(self):
        if self.username == self.username and self.password == self.password:
            return True
        else:
            return False
