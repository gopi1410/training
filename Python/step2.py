#Operators: calculate loan principal eligibility
#P= [((1+R)N -1)EMI]/[R*(1+R)N

print("Well lets get python to help you with that loan calculation.")
EMI = input("Now that you are a python programmer, how much can you afford as EMI on your car? ")
N = input("Nice! now tell me how many months you like to pay the EMI? ")
RPA = input("What's the bank interest rate? ")
EMI = int(EMI)
N = int(N)
RPA = float(RPA)
R = RPA/1200
print("Monthly rate {}".format(R))
P= (((1+R)*N -1)*EMI)/(R*(1+R)*N)
print("Well start dreaming about a car that costs Rs {}".format(P))
