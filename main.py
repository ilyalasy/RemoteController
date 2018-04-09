from server import Server
from client import Client

def main():
    print("Welcome to Mouse Controller 9000!")
    print("Choose whether you are a server(s) or a client(c):")
    while True:
        app_type = input()
        if app_type.lower() == "s":
            server = Server()
            server.start()
            print("Press 'a' when ready to transfer mouse position to {}.".format(server.client_address))
            print("Press 's' if you'd like to stop transfering mouse position to {}.".format(server.client_address))
            print("Press 'x' if you'd like to exit application")
            while True:
                ipt = input()
                if ipt == "a":
                    server.enable_transfer()
                elif ipt == "s":
                    server.disable_transfer()
                elif ipt == "x":
                    server.close()
                    break
                else:
                    print("Wrong input!")
            break
        elif app_type.lower() == "c":
            client = Client()
            print("Press 'c' when ready to connect to server.")
            print("Press 'd' if you'd like to disconnect from the server")
            print("Press 'x' if you'd like to exit application")

            while True:
                ipt = input()
                if ipt == "c":
                    print("Enter server ip:")
                    ip = input()
                    client.connect(ip)
                elif ipt == "d":
                    client.disconnect()
                elif ipt == "x":
                    client.close()
                    break
                else:
                    print("Wrong input!")
            break
        print("Wrong input!")


if __name__ == '__main__':
    main()