from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

#time.sleep(2)
#keyboard.press("a")
#time.sleep(1)
#keyboard.release("a")

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
