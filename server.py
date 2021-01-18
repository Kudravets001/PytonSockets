import socket
import random

host = '127.0.0.1'
port = 14900
Max_Connections = 5
missed = 0
secret = ""
turns = 5

def win(word, input):
    if input.lower() == "к" and word.lower() == "н":
        return "win"
    elif input.lower() == "к" and word.lower() == "б":
        return "lose"
    elif input.lower() == "н" and word.lower() == "б":
        return "win"
    elif input.lower() == "н" and word.lower() == "к":
        return "lose"
    elif input.lower() == "б" and word.lower() == "к":
        return "win"
    elif input.lower() == "б" and word.lower() == "н":
        return "lose"
    else:
        return "draw"


try:
    srv_sock = socket.socket()  # creates a socket
    print("Сокет создан.!")
except Exception as e:
    print("Ошибка создания сокета: ", e)

try:
    srv_sock.bind(("localhost", port))
    print("Сокет подключён по хосту: ", host, " и порту: ", port)
except Exception as e:
    print("ошибка настройки сокета: ", e)
    # while True:

srv_sock.listen(Max_Connections)
conn, addr = srv_sock.accept()
print("Успешное соединение : " + str(addr))


print("добро пожаловать в Камень Ножницы Бумагу.\n Введите К или Н или Б для игры")
guess = str(conn.recv(1024).decode())
data = input("Ввод: ")
def correct_input(inp):
        if inp.lower() not in ["к","н","б"]:
            print("некорректный ввод")
            data1 = input("Ввод: ")
            correct_input(data1)
        pass
correct_input(data)
message = win(guess,data)
print(f"{data} vs {guess}")
print(message)
if message == "win":
    conn.send(f"{guess} vs {data}\nlose".encode())
else:
    conn.send(f"{guess} vs {data}\nwin".encode())
while True:
    guess = str(conn.recv(1024).decode())
    data = input("Ввод: ")
    def correct_input(inp):
        if inp.lower() not in ["к","н","б"]:
            print("некорректный ввод")
            data1 = input("Ввод: ")
            correct_input(data1)
        pass
    correct_input(data)
    message = win(guess, data)
    print(f"{data} vs {guess}")
    print(message)
    if message == "win":
        conn.send(f"{guess} vs {data}\nlose".encode())
    else:
        conn.send(f"{guess} vs {data}\nwin".encode())







