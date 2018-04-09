import socket
import pyautogui as pag
import pickle
import threading


class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = 3000
        self.connection = False

    def connect(self, server_ip):
        request = bytes("Request","utf-8")
        self.s.sendto(request, (server_ip, self.port))

        self.connection = True
        threading.Thread(target=self.receive_data()).start()

    def receive_data(self):
        while self.connection:
            data, server = self.s.recvfrom(4096)
            pos = pickle.loads(data)
            self.control_mouse(pos)

    def disconnect(self):
        self.connection = False

    def control_mouse(self, position):
        pag.moveTo(position[0], position[1])

    def close(self):
        self.disconnect()
        self.s.close()