#there is a bid going on and the program must find the number of bidders, and how much they bid. Then it must state who has the highest bid and their bid value.

Num_bidders = int(input("Enter the number of bidders"))
if Num_bidders <=1 or Num_bidders >= 100:
  print("not valid")
  #figure out how to end 
winning_bid = 0
winning_bidder = ''
for i in range(Num_bidders):
  name_of_bidder = (input("Enter the name of the bidder"))
  dollars_bid = int(input("What is the amount of money ($) this person has bid:"))
  if dollars_bid > winning_bid:
    winning_bidder = name_of_bidder
    winning_bid = dollars_bid 
print(winning_bidder)
print(winning_bid)
