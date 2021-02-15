class User:
    def __init__(self, user_name = "Robot"):
        self.user_name = user_name
        self.log_name = ""

    def getProfileName(self):
        return self.user_name

    def getLogName(self):
        return self.log_name

    def getPassword(self):    #реализовать в дальнейшем
        return "admin"

    def setProfileName(self, name):
        self.log_name = name
        if name == "admin":
            self.user_name = "Admin"
        elif name == "dimon":
            self.user_name = "Дмитрий"
        elif name == "egor":
            self.user_name = "Егор"
        else:
            self.user_name = "Robot"
