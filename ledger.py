# Ledger Class
class ledger:
    def __init__(self):
        self.user_list = []
        self.id_list = []
        self.avg_user_power = 0.0
        self.number_users = 0
        self.max_power = 0

    def fill_id_list(self):
        id_list = [(u.get_id() for u in self.user_list)]

    def get_id_list(self):
        if len(self.user_list) == 0:
            self.fill_id_list()
        return self.id_list

    def add_user(self, new_user):
        #print("ADDING: ",new_user.get_name())
        id_list = self.get_id_list()
        next_id = 0
        if len(id_list) != 0:
            next_id = max(id_list)+1
        if next_id == 256:
            print("No more available IDs")
        else:
            #print("\tID: ",next_id)
            new_user.set_id(next_id)
            self.id_list.append(next_id)
            self.user_list.append(new_user)

    def add_user_list(self, users):
        for u in users:
            self.add_user(u)

    def get_user_list(self):
        return self.user_list

    def calculate_max_power(self):
        powers = [u.power for u in self.user_list]
        self.max_power = sum(powers)

    def gen_id(self):
        rand_id = 255

# User Class
class user:
    def __init__(self, name, power, ip):
        self.power = power
        self.name = name
        self.id = -1
        self.ip = ip

    def get_ip(self):
        return self.ip

    def set_id(self, new_id):
        self.id = new_id

    def get_power(self):
        return self.power

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def __repr__(self):
        return "["+str(self.id)+"] "+self.name+": power = "+str(self.power)

# Test Method
def test_ledger():
    test_user1 = user("Bob",1.0)
    test_user2 = user("Alice",3.0)
    test_user3 = user("Bill",2.0)
    test_user4 = user("Amanda",8.0)

    ledger1 = ledger()
    ledger1.add_user_list([test_user1, test_user2, test_user3, test_user4])

    print("USERS: ",ledger1.get_user_list())
    print("IDs: ",ledger1.get_id_list())