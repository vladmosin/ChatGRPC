from tkinter import Tk, StringVar, Entry, Frame, Text, LEFT, RIGHT, END, X, Y, BOTTOM, BOTH, INSERT, Scrollbar, Listbox, Button, simpledialog, YES
from tkinter import N, S, W, E, Grid

import argparse
import datetime
from threading import Lock


class ChatWindow:
    def __init__(self, root, username, sender):
        self.frame = Frame(root)
        self.username = username
        self.sender = sender
        self.put_message_lock = Lock()

        Grid.columnconfigure(self.frame, 0, weight=2)
        Grid.columnconfigure(self.frame, 1, weight=0)
        Grid.rowconfigure(self.frame, 0, weight=2)
        Grid.rowconfigure(self.frame, 1, weight=0)

        self.scrollbar = Scrollbar(self.frame)
        self.messages = Listbox(self.frame, yscrollcommand=self.scrollbar.set, height=15, width=50)
        self.scrollbar.grid(row=0, column=1, sticky=N+S)
        self.messages.grid(row=0, column=0, sticky=N+S+W+E)
        self.scrollbar.config(command = self.messages.yview)

        self.input_user = StringVar()
        self.input_field = Entry(self.frame, text=self.input_user)
        self.input_field.grid(row=1, column=0, sticky=W+E+S)

        self.send_button = Button(self.frame, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, sticky=S)

        self.input_field.bind("<Return>", lambda key: self.send_message())
        self.frame.pack(fill=BOTH, expand=YES)
        self.input_field.focus()

        

    def send_message(self):
        input_val = self.input_field.get() 
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if input_val == "":
            return
        if self.sender(input_val, self.username, date):
            self.put_message_in_chat(input_val, self.username, date)
            self.input_user.set("")
            self.messages.yview(END)

    def put_message_in_chat(self, message, username, date):
        with self.put_message_lock:
            self.messages.insert(END, date + "  " + username + ": " + message)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--address', type=str, required=False)
    parser.add_argument('--port', type=str, required=False)
    return parser


def client(address, port):
    root = Tk()
    root.title("Chat")
    root.withdraw()
    username = simpledialog.askstring("Username", "What's your name", parent=root)
    root.deiconify()

    chat_window = ChatWindow(root, username, lambda a, b, c: True)
    root.mainloop()


def server():
    pass


if __name__ == "__main__":
    args = create_parser().parse_args()
    if args.address is None and args.port is None:
        server()
    elif args.address is None or args.port is None:
        print("you should specify both address and port or none of them")
    else:
        client(args.address, args.port)
