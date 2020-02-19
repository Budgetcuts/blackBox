def run_gui():
    import tkinter as tk
    import ledger as lg
    import ledger_manager as lm
    import random as rand
    import server

    ledger = lg.ledger()
    ledger.clean()

    temp_user1 = lg.user("Bob", 1.0, "0.0.0.0")
    temp_user2 = lg.user("Marty", 2.0, "0.0.0.1")
    temp_user3 = lg.user("Alice", 3.0, "0.0.0.2")
    temp_user4 = lg.user("Whemble", 4.0, "0.0.0.3")
    userlist = [temp_user1, temp_user2, temp_user3, temp_user4]

    ip = ""

    root = tk.Tk()

    text = tk.Text(root)
    text.pack()

    frame1 = tk.Frame(root, width=400, height=100)

    frame1.pack(fill=None, expand=False)
    # frame2.place(relx=.5, rely=.5, anchor="c")

    class Application(tk.Frame):

        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.server_active = False
            self.client_active = False
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

            self.entry = tk.Entry(self)
            self.entry.pack(side="right")
            jn_server = tk.Button(root, text="Join Server", command=self.join_server)
            jn_server.pack(side="bottom")

            self.quit = tk.Button(self, text="QUIT", fg="black",
                                  command=self.master.destroy)
            self.quit.pack(side="bottom")

        def add_user(self):
            user = userlist[rand.randint(0, 3)]
            add_success = ledger.add_user(user)
            if add_success == True:
                text.insert(tk.INSERT, "Added: %s\n" % user.name)
                # print("added: ", user)
                # ledger.add_user(temp_user1)
                lm.write_json(ledger)
            else:
                text.insert(tk.INSERT, "Could not add user: %s\n" % user.name)

        def clear_ledger(self):
            # print("cleaned ledger")
            text.insert(tk.INSERT, "Cleaned Ledger\n")
            ledger.clean()
            lm.write_json(ledger)

        def join_server(self):
            # text.insert(tk.INSERT, "Hello.....")
            # text.insert(tk.END, "Bye Bye.....")
            ip = "0.0.0.0"  # self.entry.get()
            self.client_active = True
            # print("IP: %s\n" % ip)
            text.insert(tk.INSERT, "Connected to: %s\n" % ip)
            text.pack()

        def start_server(self):
            if (server.is_server_open == True):
                text.insert(tk.INSERT, "Server Already Open!\n")
            else:
                text.insert(tk.INSERT, "Server Opened On: %s\n" % server.get_ip())
                self.server_active = True
            text.pack()
            # server.start()

    app = Application(master=root)
    app.mainloop()
