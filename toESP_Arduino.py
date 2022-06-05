"""連接ESP"""
from cmd import Cmd
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ESP_connect(addr):
    #addr = input("Please enter the Server ip:")
    port = 5289
    s.connect((addr,port))
    print("Client start at : ",s.getsockname())

    """傳送F代表前進B代表後退L代表左轉R代表右轉S代表停止全部是大寫
    一個指令會執行到下個指令覆蓋掉為止
    範例: s.send("S".encode())
    """
def ESP_send(cmd):
    #cmd = input("Please input message:")
    if 'Forward' in cmd:
        move = 'F'
    elif 'Stop'  in cmd:
        move = 'S'
    elif 'Left' in cmd:
        move = 'L'
    elif 'Right' in cmd:
        move = 'R'
    #@ if detect nothing send 'NONE'
    else : move = 'NONE'
    s.send(move.encode())

def ESP_close():
    print ("Close socket")
    s.close()
        