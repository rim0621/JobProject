from fbchat import Client

def sendMSG(msg):

    fc = Client('id', 'passwd')
    friends = fc.searchForUsers('receiver')
    friend = friends[0]
    sent = fc.sendMessage(msg,
                          thread_id=friend.uid)
    if sent:
        print("Message sent successfully!")
