class user_login():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_username(self):
        self.username = input("insira o nome de usuário:")
        return self.username

    def create_password(self):
        self.password = input("insira a senha:")
        return self.password

    def check_login(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            return False

    def change_password(self, username, password):
        if username == self.username and password == self.password:
            self.password = input("insira a nova senha:")
            return self.password
        else:
            return False
