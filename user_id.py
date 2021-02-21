class User:
    def __init__(self, user_name = "Robot"):
        self.user_name = user_name
        self.log_name = ""

    def get_profile_name(self):
        return self.user_name

    def get_log_name(self):
        return self.log_name

    def test_password(self):   # реализовать в дальнейшем
        return "admin"

    def set_profile_name(self, name):
        self.log_name = name
        if name == "admin":
            self.user_name = "Admin"
        elif name == "dimon":
            self.user_name = "Дмитрий"
        elif name == "egor":
            self.user_name = "Егор"
        else:
            self.user_name = "Robot"
