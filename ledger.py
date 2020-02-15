# Ledger Class
import json

class ledger:
    def __init__(self):
        self.user_list = []
        self.id_list = []
        self.avg_user_power = 0.0
        self.number_users = 0
        self.max_power = 0
        self.transactions = []

    def fill(self,avg_user_power,id_list,max_power,user_list,transactions):
        self.user_list = user_list
        self.id_list = id_list
        self.avg_user_power = avg_user_power
        self.max_power = max_power
        self.transactions = transactions

        num = 0
        for u in self.user_list:
            num += 1
        self.number_users = num

    def clean(self):
        self.user_list = []
        self.id_list = []
        self.avg_user_power = 0.0
        self.number_users = 0
        self.max_power = 0
        self.transactions = []

    def add_transaction(self,user_server,user_client):
        transaction = user_server.name + "->" + user_client.name
        self.transactions.append(transaction)

    def add_str_transaction(self,transaction):
        self.transactions.append(transaction)

    def fill_id_list(self):
        id_list = [(u.get_id() for u in self.user_list)]

    def get_id_list(self):
        if len(self.user_list) == 0:
            self.fill_id_list()
        return self.id_list

    def add_user(self, new_user):
        new_user_id = new_user.get_id()
        if new_user_id == -1 and not(new_user_id in self.id_list):
            #print("ADDING: ",new_user.get_name())
            id_list = self.get_id_list()
            next_id = 0
            for i in range(256):
                if not(i in id_list):
                    next_id = i
                    break
            if next_id == 256:
                print("No more available IDs")
                return False
            new_user.set_id(next_id)
            self.id_list.append(next_id)
        else:
            self.id_list.append(new_user_id)

        if(new_user.get_id()!=256):
            self.user_list.append(new_user)
        return True

    def get_num_users(self):
        num = 0
        for u in self.user_list:
            num += 1
        return num

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

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        out = "avg pow: " + str(self.avg_user_power) + "\n"
        out += "num users: " + str(self.number_users) + "\n"
        out += "max power: " + str(self.max_power) + "\n"
        for t in self.transactions:
            out += ":: " + str(t) + "\n"
        #out += "transactions: " + str(self.transactions)
        for u in self.user_list:
            out += str(u)
        return out




# User Class
class user:
    def __init__(self, name="Null", power=0, ip="0.0.0.0", id=-1):
        self.power = power
        self.name = name
        self.id = -1
        self.ip = ip

        if 'id' in locals():
            self.id = id

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
    test_user1 = user("Bob",1.0,"0.0.0.0",3)
    test_user2 = user("Alice",3.0)
    test_user3 = user("Bill",2.0)
    test_user4 = user("Amanda",8.0)
    test_user5 = user("Gerard",2.0)

    ledger1 = ledger()
    ledger1.add_user_list([test_user1, test_user2, test_user3, test_user4, test_user5])

    print("USERS: ",ledger1.get_user_list())
    print("IDs: ",ledger1.get_id_list())

    print(ledger1.toJSON())

#test_ledger()