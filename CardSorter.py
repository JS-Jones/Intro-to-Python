''' Class Cards orgnaization made by Joshua Jones'''

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def bj_value(self):
        if self.rank > 10 and self.rank <= 13:
            return 10
        else:
            return self.rank
    
    def __repr__(self):
        wordsuit = ''
        numwords = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Jack', 12: 'Queen', 13: 'King'}
                    
        if self.suit == "c":
            wordsuit = "Clubs"
        elif self.suit == "d":
            wordsuit = "Diamonds"
        elif self.suit == "s":
            wordsuit = "Spades"
        else:
            wordsuit = "Hearts"

        sentence = numwords[self.rank] + " of " + wordsuit
        return sentence
    
    def __lt__(self, other):
        return self.rank < other.rank


def fullsuite(suite):
    suitenames = {'c': "Clubs", 'd': "Diamonds", 'h': "Hearts", 's': "Spades"}
    return(suitenames[suite])


def main():
    total = {"Clubs": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             "Diamonds": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             "Hearts": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             "Spades": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    #dictionary that stores count of cards
    sortedcards = []
    Clubs = []
    Diamonds = []
    Hearts = []
    Spades = []
    while True:
        rank = int(input("Enter rank, or 0 to stop: "))
        if rank == 0:
            
            print("\nYour sorted cards are")
            Clubs.sort()
            Diamonds.sort()
            Hearts.sort()
            Spades.sort()
            #sortedcards.sort()
            for item in Clubs:
                print(item)
            for item in Diamonds:
                print(item)
            for item in Hearts:
                print(item)
            for item in Spades:
                print(item)
                
            print("\nThe total number of cards of each rank are")
            for key, value in total.items():
                print(key+ ':', value)
            break
        else:
            suite = input("Enter suite: ")
            suitename = fullsuite(suite)
            total[suitename][rank] += 1
            if suite == "c":
                Clubs.append(Card(rank,suite))
            elif suite == "d":
                Diamonds.append(Card(rank,suite))
            elif suite == "h":
                Hearts.append(Card(rank,suite))
            elif suite == "s":
                Spades.append(Card(rank,suite))
            sortedcards.append(Card(rank,suite))
           # list that stores the cards
            
main()
            




        
