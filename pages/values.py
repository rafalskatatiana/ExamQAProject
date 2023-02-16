class User:
    def __init__(self, username="standard_user", password="secret_sauce"):
        self.username = username
        self.password = password

    def fill_data(self):
        """Fill data by value"""
        self.username = "standard_user"
        self.password = "secret_sauce"

    def __repr__(self):
        return f"User:(username={self.username},  password={self.password}"
