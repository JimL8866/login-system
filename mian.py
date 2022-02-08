import hashlib

SALT = b"Today is Monday"
script_is_on = True
account_dict = {}


class Account:
    func_list = ["login", "retrieve", "logout"]

    def __init__(self, user_name, user_pwd):
        self.name = user_name
        self.password = user_pwd
        self.enc_password = None

    @classmethod
    def md5(cls, pwd):
        encryption = hashlib.md5(SALT)
        encryption.update(pwd.encode("utf-8"))
        return encryption.hexdigest()

    def login(self):
        username = input("What is your user name?")
        password = input("What is your password")
        password_encrypted = Account.md5(password)

        if self.name == username and self.enc_password == password_encrypted:
            print("Access Granted")
        else:
            print("Access Denied")

    @staticmethod
    def retrieve():
        r_username = input("Please put in your username")
        r_pwd = account_dict[r_username]
        print(f"Your password is {r_pwd} ")

    @staticmethod
    def logout():
        print("You've successfully logged out.")
        global script_is_on
        script_is_on = False

    @staticmethod
    def run():
        while script_is_on:
            print("Hi there, you have the following options to choose:")
            for i, func in enumerate(Account.func_list, 1):
                print(i, func)
            num = int(input("Please choose a number in the option to continue."))
            user_func = getattr(acct, Account.func_list[num - 1])
            user_func()


while True:
    user_name = input("Please create a user name")
    if user_name not in account_dict:
        user_pwd = input("Please create a password")
        account_dict[user_name] = user_pwd
        acct = Account(user_name, user_pwd)
        acct.enc_password = Account.md5(user_pwd)
        acct.run()
        script_is_on = True
        print(account_dict)