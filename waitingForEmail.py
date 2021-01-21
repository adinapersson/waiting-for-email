def main():
    waitingForReplyFromSchibsted()

def waitingForReplyFromSchibsted():
    noEmailFromSchibsted= True
    while(noEmailFromSchibsted): 
        email = str(input("Receiving email from: "))
        if email == 'Schibsted':
            noEmailFromSchibsted = False
            print('Happy!')
        else:
            print('Wait!')

if __name__ == '__main__':
    main()