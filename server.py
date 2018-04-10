import socket
import pyautogui as pag
import pickle
import threading


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = get_ip()
        self.port = 3000
        self.transfer_mod = False
        self.client_address = ""

    def start(self):
        print("Started server with ip: {}".format(self.ip))
        self.s.bind((self.ip, self.port))
        self.get_connection()

    def get_connection(self):
        print("Waiting for connection...")
        while True:
            request, self.client_address = self.s.recvfrom(4096)
            if request:
                self.s.sendto(request, self.client_address)
                print("{} connected!".format(self.client_address))

                break

    def enable_transfer(self):
        print("Transfer to {} enabled".format(self.client_address))
        self.transfer_mod = True
        transfer_thread = threading.Thread(target=self.transfer_mouse)
        transfer_thread.start()

    def disable_transfer(self):
        print("Transfer to {} disabled".format(self.client_address))
        self.transfer_mod = False

    def transfer_mouse(self):
        while self.transfer_mod:
            pos = pag.position()
            data = pickle.dumps(pos)

            self.s.sendto(data, self.client_address)

    def close(self):
        self.disable_transfer()
        self.s.close()