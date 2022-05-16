class login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_login(self):
        if self.username == "admin" and self.password == "admin123":
            return True
        else:
            return False
