# M. Steven Towns
#Assignment 8
#2/4/2014

encoder=True
while encoder:
    msg=raw_input('What do you want to encode?: ')
    shift=int(raw_input('what do you want to shift it by?: '))%26
    secret_msg=""
    for i in range(len(msg)):
        letter=msg[i]
        if letter.isalpha():
            if letter.isupper():
                if ord(letter)+shift>90:
                    new_letter=chr(ord(letter)+shift-26)
                elif ord(letter)+shift<65:
                    new_letter=chr(ord(letter)+shift+26)
                else:
                    new_letter=chr(ord(letter)+shift)
                secret_msg+=new_letter
            else:
                if ord(letter)+shift>122:
                    new_letter=chr(ord(letter)+shift-26)
                elif ord(letter)+shift<97:
                    new_letter=chr(ord(letter)+shift+26)
                else:
                    new_letter=chr(ord(letter)+shift)
                secret_msg+=new_letter
        else:
            secret_msg+=letter
    print secret_msg
    again=True
    while again:
        prompt=(raw_input("Do you want to encode another message?: ")).lower()
        if prompt=="no":
            encoder=False
            print "Good luck agent!"
            again=False
        elif prompt=="yes":
            print "Security protocol engaged!\nSecuring network."
            again=False
        else:
            again=True
            print "Try that again, I couldn't understand that."
