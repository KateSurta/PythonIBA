import math
previousTicketStatus = False

for currentTicket in range(100000, 1000000):
    ticket = currentTicket
    #print(ticket)
    remainder = 0
    sumOfDigits = 0

    for y in range(1, 7):
        remainder = ticket % 10
        ticket = math.floor(ticket / 10)
        sumOfDigits = sumOfDigits + remainder

    if sumOfDigits % 7 == 0:
        currentTicketStatus = True
        #print(str(sumOfDigits) + " true")
    else:
        currentTicketStatus = False
        #print(str(sumOfDigits) + " false")

    if currentTicketStatus is True and previousTicketStatus is True:
        print("Удачные билеты: " + str(previousTicket) + " и " + str(currentTicket))

    previousTicket = currentTicket
    previousTicketStatus = currentTicketStatus

