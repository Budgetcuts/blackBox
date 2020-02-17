import tkinter as tk
import ledger as lg
import ledger_manager as lm
import random as rand
import server

ledger = lg.ledger()
ledger.clean()

temp_user1 = lg.user("Bob",1.0,"0.0.0.0")
temp_user2 = lg.user("Marty",2.0,"0.0.0.1")
temp_user3 = lg.user("Alice",3.0,"0.0.0.2")
temp_user4 = lg.user("Whemble",4.0,"0.0.0.3")
userlist = [temp_user1,temp_user2,temp_user3,temp_user4]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.add_rand_user = tk.Button(self)
        self.add_rand_user["text"] = "Add Rand User"
        self.add_rand_user["command"] = self.add_user
        self.add_rand_user.pack(side="top")

        self.clr_ledger = tk.Button(self)
        self.clr_ledger["text"] = "Clear Ledger"
        self.clr_ledger["command"] = self.clear_ledger
        self.clr_ledger.pack(side="top")

        st_server = tk.Button(root, text="Start Server", command=self.start_server)
        st_server.pack(side="left")

        jn_server = tk.Button(root, text="Join Server", command=self.join_server)
        jn_server.pack(side="right")

        self.join_server = tk.Button(self)
        self.join_server["text"] = "Join Server"
        self.join_server["command"] = self.join_server
        self.join_server.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_user(self):
        user = userlist[rand.randint(0, 3)]
        ledger.add_user(user)
        print("added: ", user)
        # ledger.add_user(temp_user1)
        lm.write_json(ledger)

    def clear_ledger(self):
        print("cleaned ledger")
        ledger.clean()
        lm.write_json(ledger)

    def join_server(self):
        #text.insert(tk.INSERT, "Hello.....")
        #text.insert(tk.END, "Bye Bye.....")
        text.pack()

    def start_server(self):
        if(server.is_server_open == True):
            text.insert(tk.INSERT, "Server Already Open!\n")
        else:
            text.insert(tk.INSERT, "Server Opened On: %s\n" % server.get_ip())
            server.start()
        text.pack()
        #server.start()


root = tk.Tk()

text = tk.Text(root)
text.pack()

frame1 = tk.Frame(root, width=400, height=100)

frame1.pack(fill=None, expand=False)
#frame2.place(relx=.5, rely=.5, anchor="c")


app = Application(master=root)
app.mainloop()