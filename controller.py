import socket
import pygame as pg

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DC_MSG = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

pg.init()
pg.joystick.init()
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
#think about appropriate data set for the wheel stuff

while True:
    for event in pg.event.get():
        if event.type == pg.JOYBUTTONDOWN:
            print(event)
            
            exit(0) #for testing
        elif event.type == pg.JOYHATMOTION:
            print(event)
        elif event.type == pg.JOYDEVICEREMOVED:
            print('EXITTING DEVICE REMOVED')
            send(DC_MSG)
            exit(0)






