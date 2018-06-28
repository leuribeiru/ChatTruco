#coding: utf-8

from socket import *

class Info:
	verifica_on = 0
	meuEmail = ''
	serverIp = '10.3.1.18'
	serverPort = 54319
	
	comando_login = "Con"
	comando_signin = "Sin"
	
	comando_truco = "Truco"
	comando_seis = "Seis"
	comando_envia = "Envia"
	
	""" Respostas """
	erro_pw = "erro_pw"
	erro_em = "erro_em"
	erro = "erro"
	sin_ok = "sin_ok"
	sin_erro_em = "sin_erro_em"
	sin_erro = "sin_erro"
	msg_ok = "ok"
	
	receiver_socket = socket(AF_INET, SOCK_DGRAM)
	receiver_socket.bind(('', serverPort))
	
	sender_socket = socket(AF_INET, SOCK_DGRAM)
	
	
def send_toServer(mensagem):
	Info.sender_socket.sendto(mensagem.encode("utf-8"), (Info.serverIp, Info.serverPort))
	
def receber_mensagem():
	message, clientAddress = Info.receiver_socket.recvfrom(2048)

	return message.decode("utf-8"), clientAddress
	
def send_to(mensagem,ip):
	Info.sender_socket.sendto(mensagem, (ip, Info.serverPort))

def close_sockets():
	Info.receiver_socket.close()
	Info.sender_socket.close()

def find_in_list(lista,chave):
	for l in lista:
		if(chave == l):
			return True
	return False
