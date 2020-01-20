import json
from firstPackage.service import *
class database:
    def __init__(self):
        self.setOfKeys = set()
        self.servicesWithPasswords = {}
        self.uniqueGroupsNames = set()

# addGroup
# deleteGroup
# renameGroup
#
# addService
# deleteService
# changeService
#
# addServiceToGroup
# removeServiecFromGroup



myKey = serviceKey("url","userName")
myService = servicePassword(myKey)
json_string = json.dumps(myKey)
print(json_string)
print(myService)

# #myService.setUrl("hoho")
# print(myService)
# myService = service()
# print(myService)
# myService.setUrl("hoho")
# print(myService)

# mySet = set()
# mySet.add("a")
# mySet.add("b")
# print(mySet)
# mySet.add("a")
# print(mySet)
