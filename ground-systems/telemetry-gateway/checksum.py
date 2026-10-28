#checksum of sent message

c1 = message[0:k]
c2 = message[k:2*k]
c3 = message[2*k:3*k]
c4 = message[3*k:4*k]#message is split

sum = bin(int(c1, 2) + int(c2, 2) + int(c3, 2) + int(c4, 2))[2:]
#packets are converted to ints and added together, and then turned into binary

if(len(sum) > k):
    x = len(sum) - k