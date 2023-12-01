
import art
#HINT: You can call clear() to clear the output in the console.

auctioneers = []
new_bidders = True
#Variable ertellt für die Funktion und Schleife

def add_new_auctioneer(new_name, new_bid):
    new_auctioneers = {} 
    new_auctioneers["Name"] = new_name
    new_auctioneers["bid"] = new_bid
    auctioneers.append(new_auctioneers)
#Funktion erstellt für das einfügen der eingegeben Daten in ein Dictionary
  
while(new_bidders):
  print(art.logo)
  new_name = input("What is your name? ")
  new_bid = input("What's your bid? $")
  add_new_auctioneer(new_name, new_bid)
  new = input("Is there a another bidder. 'yes' or 'no'?").lower()
  if new == "no":
    new_bidders = False
    clear()
  else:
    clear()
#Schleife zur Abfrage der Daten erstellt mit abbruchbedingung

max_bid = {
  "Name": " ",
  "bid": 0 
}
for val in auctioneers:
  if int(val["bid"]) > int(max_bid["bid"]):
    max_bid = val
#Eine For-Schleife erstellt mit Variablen in der zu lesende Schlüsselwörter schon zu finden sind um diese in der if-Abfrage nutzen zu können

print(f"{max_bid['Name']} wins the auction with {max_bid['bid']}$.")
  