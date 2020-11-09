import threading
import socket


class connection:
    port = 12345
    version = '0.01'
    host = '127.0.0.1'  # 139.162.136.115
    string_multiplayer = 2
    socket = None
    addr = None

    imh = None

    message_queue = []

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (self.host, self.port)

        try:
            self.socket.connect(self.addr)
            print('connected')
        except Exception as e:
            print(e)

        self.imh = threading.Thread(target=self.incoming_message_handler)

    def incoming_message_handler(self):
        while True:
            try:
                self.message_queue.append(self.socket.recv(1024 * self.string_multiplayer))
            except Exception as e:
                print(e)
                break

    def get_messages(self):
        outbound = self.message_queue
        self.message_queue = []
        return outbound

    def send_message(self, msg):
        try:
            self.socket.send(str.encode(msg))
        except Exception as e:
            print(e)
