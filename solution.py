from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
  msg = "\r\n Hi Alice, this is me."
  endmsg = "\r\n.\r\n"

 # Choose a mail server (e.g. Googlemail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
       # print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELLO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
       # print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM:<ms13592@nyu.edu>\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptToCommand = 'RCPT TO:<mamadoudesall@gmail.com>\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode)
    recv4 = clientSocket.recv(1024).decode
    # Fill in end

    # Send message data.
    # Fill in start
    msg ="\r\n Hi Alice, this is me."
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    endmsg = "\r\n.\r\n"
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.endcode())
    recv6 = clientSocket.recv(1024).decode()
    # Fill in end
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
