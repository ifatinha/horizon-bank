class Historic:

    def __init__(self, account) -> None:
        self.__id = None
        self.__account = account

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, account):
        self.__account = account

    def to_tuple(self):
        return (self.account.id_account,)
