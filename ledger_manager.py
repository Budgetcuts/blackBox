import json
import ledger as lg

def write_json(ledger):
    file = open('ledger.json','w+')
    ledger_as_json = ledger.toJSON()
    file.write(ledger_as_json)
    print('Wrote ledger to "ledger.json"')

def json_to_ledger():
    file = open('ledger.json','r+')
    json_file = file.read()
    ledger_as_json = json.loads(json_file)
    user_list_as_json = ledger_as_json['user_list']
    user_list = isolate_users_from_user_list(user_list_as_json)

    avg_user_power = json_file[0]
    id_list = json_file[1]
    max_power = json_file[2]
    transactions = json_file[4]

    ledger = lg.ledger()
    ledger.fill(avg_user_power,id_list,max_power,user_list,transactions)

    num_users = ledger.get_num_users()

    print('Read ledger from "ledger.json"')
    print('Found',num_users,'users')
    return ledger

def json_to_user(user_as_json):
    #print(user_as_json)
    name = user_as_json['name']
    power = user_as_json['power']
    ip = user_as_json['ip']
    id = user_as_json['id']
    temp_user = lg.user(name,power,ip,id)
    return temp_user

def isolate_users_from_user_list(user_list_as_json):
    #print(user_list_as_json)
    userlist = []
    for u in user_list_as_json:
        userlist.append(json_to_user(u))
    return userlist

def test():
    test_user1 = lg.user("Bob",1.0,"0.0.0.0",3)
    test_user2 = lg.user("Alice",3.0)
    test_user3 = lg.user("Bill",2.0)
    test_user4 = lg.user("Amanda",8.0)
    test_user5 = lg.user("Gerard",2.0)
    ledger1 = lg.ledger()
    ledger1.add_user_list([test_user1, test_user2, test_user3, test_user4, test_user5])
    ledger1.add_transaction(test_user1,test_user2)
    write_json(ledger1)

    ledger2 = json_to_ledger()
    print(ledger1)
    #print(ledger2)
#test()