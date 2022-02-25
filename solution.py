from email import message
from http import client
from socket import *
import base64

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
mailserver = "smtp.163.com"
mailUser = 'msall'
mailFromAddress = 'mamadoudesall@gmail.com'
mailPassWord = '******'
mailToAddress = 'ms13592@nyu.edu'

msg = 'FROM: ' + mailFromAddress + '\r\n'
msg += 'TO: ' + mailToAddress +  '\r\n'
msg += 'Subject: ' + 'testing' +  '\r\n'
msg += "\r\n Keep on learning!"
endmsg = "\r\n.\r\n"

# Create socket called clientSocket and establish a TCP connection with mailserver and port
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('mailserver',25))
# Fill in end
recv = clientSocket.recv(1024)
recv = recv.decode()
#print(recv) #You can use these print statement to validate return codes from the server.
#if recv[:3] != '220':
# #    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
while True:
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024)
    recv = recv.decode()
    #print(recv)
    if recv[:3] == '250':
    #    print('250 reply not received from server.')
                break
loginCommand = 'auth login\r\n'
while True:
    clientSocket.send(loginCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
   # print(recv)
    if recv[:3] == '334':
        break
userCommand = base64.b64encode(mailUser.encode()) + b'\r\n'
while True:
    clientSocket.send(userCommand)
    recv = clientSocket.recv(1024)
    recv = recv.decode()
   # print(recv)
    if recv[:3] == '334':
        break                
passCommand = base64.b64encode(mailPassWord.encode()) + b'\r\n'
while True:
    clientSocket.send(passCommand)
    recv = clientSocket.recv(1024)
    recv = recv.decode()
   # print(recv)
    if recv[:3] == '235':
        break
    
    # Send MAIL FROM command and handle server response.
    # Fill in start
    MFCommand = 'MAIL From:<'+ mailFromAddress + '>\r\n'
    while True:
        clientSocket.send(MFCommand.encode())
        recv = clientSocket.recv(1024)
        clientSocket.send(MFCommand.encode())
        recv = clientSocket.recv(1024).decode()
        recv = recv.decode()
        #print(recv)
        if recv[:3] == '250':
            break
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    RTCommand = 'RCPT To: <'+ mailToAddress + '>\r\n'
    while True:
        clientSocket.send(RTCommand.encode())
        recv = clientSocket.recv(1024)
        recv = recv.decode()
        #print(recv)
        if recv[:3] == '250':
            break    
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    DATACommand = 'DATA\r\n'
    while True:
        clientSocket.send(DATACommand.encode())
        recv_data = clientSocket.recv(1024)
        recv = recv.decode()
        #print(recv)
        if recv[:3] == '354':
            break
    # Fill in end


    # Send message data.
    # Fill in start
    clientSocket.send(bytes(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    while True:
        clientSocket.send(bytes(msg.encode))
        recv = clientSocket.recv(1024)
        recv = recv.decode()
        #print(recv)
        if recv[:3] == '250':
            break

    # Fill in end


    # Send QUIT command and handle server response.
    # Fill in start
    QUITCommand = 'QUIT\r\n'
    while True:
        clientSocket.send(QUITCommand.endmsg())
        recv = clientSocket.recv(1024)
        recv = recv.base64.decode()
        #print(recv)
        if  recv[:3] == '221':
            break

    # Fill in end
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')