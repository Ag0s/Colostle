#! /usr/share/bin python3
import itertools, random, sys

show_deck_size = False

cards = ["2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K"]

suits = ["♥", "♦", "♣", "♠"]

deck = []
discard = []

def draw_cards(draw_amount):
    cards = []
    for _ in itertools.repeat(None, draw_amount):
        if not len(deck) > draw_amount:
            create_deck()
            print("[*] The deck has been reshuffled")
        else:
            card = random.choice(deck)
            cards.append(card)
            deck.remove(card)
            discard.append(card)
    return cards

def create_deck():
    for card in cards:
        for suit in suits:
            deck.append(card+suit)
    del discard[:]
        
def main():
    create_deck()
    print("╔═══╗    ╔╗          ╔╗ ╔╗     ")
    print("║╔═╗║    ║║         ╔╝╚╗║║     ")
    print("║║ ╚╝╔══╗║║ ╔══╗╔══╗╚╗╔╝║║ ╔══╗")
    print("║║ ╔╗║╔╗║║║ ║╔╗║║══╣ ║║ ║║ ║╔╗║")
    print("║╚═╝║║╚╝║║╚╗║╚╝║╠══║ ║╚╗║╚╗║║═╣")
    print("╚═══╝╚══╝╚═╝╚══╝╚══╝ ╚═╝╚═╝╚══╝")
    print("Submit q to quit\n")
    while True:
        draw_amount = ""
        while draw_amount == "":
            if show_deck_size:
                draw_amount = input("Draw how many cards (%i left)? " % len(deck))
            else:
                draw_amount = input("Draw how many cards? ")
            if draw_amount == "q":
                quit()
        cards = draw_cards(int(draw_amount))
        print(*cards, sep = " ║ ")

def quit():
    # quit
    print("")
    print("Thanks for playing")
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit()
