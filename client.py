import socket

host = '127.0.0.1'
port = 14900

cli_sock = socket.socket()
cli_sock.connect(("localhost", port))


print("добро пожаловать в Камень Ножницы Бумагу.\n Введите К или Н или Б для игры")
data = input("Ввод: ")
def correct_input(inp):
        if inp.lower() not in ["к","н","б"]:
            print("некорректный ввод")
            data1 = input("Ввод: ")
            correct_input(data1)
        pass
correct_input(data)
cli_sock.send(str(data).encode())
print(cli_sock.recv(1024).decode())
#word = cli_sock.recv(1024).decode()
while True:
    data = input("Ввод: ")
    def correct_input(inp):
        if inp.lower() not in ["к","н","б"]:
            print("некорректный ввод")
            data1 = input("Ввод: ")
            correct_input(data1)
        pass
    correct_input(data)
    cli_sock.send(str(data).encode())
    print(cli_sock.recv(1024).decode())


cli_sock.close()