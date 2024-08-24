player_bid_dict = {}
input_bidders=True

while input_bidders:
    name=input("Enter your name: ")
    bid=int(input("Enter your bid: Rs"))
   
    player_bid_dict[name]=bid
    
    print("\n Are there any other bidders? (yes/no)")
    areMorePlayers=input()

    if areMorePlayers=="no" or areMorePlayers=="n":
        input_bidders=False
    elif areMorePlayers=="yes" or areMorePlayers=="y":
        print("\n" * 100)
        

max_bid=0
winner=""
for key in player_bid_dict:
    if player_bid_dict[key]>max_bid:
        max_bid=player_bid_dict[key]
        winner=key
print("\n"*100)
print("The Auction is over")
print(f"The Winner is {winner} with the bid amount of Rs.{max_bid} \n ")
print("Thank You for joining the Auction.")
    
