class serviceKey:
    def __init__(self,url,userName):
        self.url = url
        self.userName = userName


class servicePassword:
    def __init__(self, key):
        self.key = key
        self.password=''
        self.groups=set()

    def setKey(self,key):
        self.url = key

    def setPassword(self,password):
        self.password = password;


