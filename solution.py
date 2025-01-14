from base64 import encode
from http import client
from socket import *



def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = 'Testing My SMTP Client Server\r\n'
    endmsg = 'QUIT\r\n'
   

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    target = "google.com"
    port = 443
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 1025))
    recv = clientSocket.recv(1024)
    #print(recv)
    #if recv[:3] == '220':
    #    print ('220 reply not received from server')
    # Fill in end

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024)
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = 'MAIL FROM:<mamadoudesall@gmail.com> \r\n'
    clientSocket.send(mailFrom.encode())
    recv = clientSocket.recv(1024).decode
    #print (recv)
    #if recv[:3] != '250':
        #print('250 reply not received from server.')  

    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    recptTo = 'RCPT TO:<ms13592@nyu.edu>\r\n'
    clientSocket.send(recptTo.encode())
    recv = clientSocket.recv(1024)
    #print(recv)
    #if recv[:3] != '250':
        #print('250 reply not recieved from server.')

    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv_data)
    #if recv_data[:3] != '354':
    #print('354 reply not recieved from server.')
    
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(bytes(msg.encode()))
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(bytes(endmsg.encode()))
    recv_msg = clientSocket.send(bytes(1024))
    #print (recv)
    #if recv[:3] != '250':
        #print('250 reply not received form server.')

    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'.encode()
    clientSocket.send(bytes(quitCommand))
    recv = clientSocket.recv(1024)
    #print(quitCommand)
    #if recv_quit[:3] != '221':
    #    print('221 reply not received from server.')
    

    # Fill in end
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')