import time
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class Client:
    buffer_size = 4096

    def __init__(self, host, port):
        """
        Estabilish a connection to the main chat game server
        :param host: Host of the server
        :param port: Port of the server
        """
        self.socket_instance = socket(AF_INET, SOCK_STREAM)
        self.socket_instance.connect((host, port))
        # Await a welcome message from the server
        message = self.socket_instance.recv(Client.buffer_size).decode("utf8")
        print(message)
        Thread(target=self.__client_loop).start()

    def __client_loop(self):
        """
        Execute the main loop of the Client.
        This method will try to receive messages from the Server object.
        """
        while True:
            try:
                message = self.socket_instance.recv(Client.buffer_size).decode("utf8")
                print(f"[New Message]: {message}")
            except OSError:
                print("Something went wrong")
                break

    def send_message(self, message):
        """
        Send a message to the GameChat server.
        :param message: Message to send
        """
        self.socket_instance.send(message.encode())


if __name__ == "__main__":
    client = Client("", 53000)

