"""DNS request, python 3.6"""

import socket

print("I'm going to give you the IP address you're looking for.")

def main():

    while True:
        try:
            print('Please write the address this way: "google.com", "wikipedia.org"')
            server_request = input("Which website ? ")
            server_ip = str(socket.gethostbyname(server_request))
            break
        except:
            print("Not correct, try again.")
    print("%s IP address is %s" % (str(server_request), server_ip))
    again = input("Fancy another one ? y/n : ")
    if again == "y":
        main()
    else:
        print("Exiting...")

main()
