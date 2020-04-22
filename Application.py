import argparse
import datetime
from tkinter import N, S, W, E, Grid
from tkinter import Tk, StringVar, Entry, Frame, END, BOTH, Scrollbar, Listbox, Button, simpledialog, YES
from threading import Lock

from Server import serve

from Client import Client
from MessageSubscriber import MessageSubscriber


class ChatWindow(MessageSubscriber):
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
        if self.sender(input_val, date, self.username):
            self.put_message_in_chat(input_val, date, self.username, color="blue")
            self.input_user.set("")

    def put_message_in_chat(self, message, date, username, color="red"):
        with self.put_message_lock:
            self.messages.insert(END, date + "  " + username + ": " + message)
            self.messages.itemconfig(END, {"fg": color})
            self.messages.yview(END)

    def receive_message(self, text, date, name):
        self.put_message_in_chat(text, date, name)


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

    rpc_client = Client(f'{address}:{port}')
    chat_window = ChatWindow(root, username, rpc_client.send_message)
    rpc_client.subscriber = chat_window

    root.mainloop()


def server(port):
    serve(port)


if __name__ == "__main__":
    args = create_parser().parse_args()
    if args.address is None and args.port is not None:
        server(args.port)
    elif args.port is None:
        print("you should specify port")
    else:
        client(args.address, args.port)
