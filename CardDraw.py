#! /usr/share/bin python3
import itertools, random, sys, os.path, codecs

show_deck_size = True

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

def init():
    print("╔═══╗    ╔╗          ╔╗ ╔╗     ")
    print("║╔═╗║    ║║         ╔╝╚╗║║     ")
    print("║║ ╚╝╔══╗║║ ╔══╗╔══╗╚╗╔╝║║ ╔══╗")
    print("║║ ╔╗║╔╗║║║ ║╔╗║║══╣ ║║ ║║ ║╔╗║")
    print("║╚═╝║║╚╝║║╚╗║╚╝║╠══║ ║╚╗║╚╗║║═╣")
    print("╚═══╝╚══╝╚═╝╚══╝╚══╝ ╚═╝╚═╝╚══╝")
    print("Submit q to quit\n")
    if os.path.isfile("./ColostleDeck.save"):
        answer = input("Continue last session? ")
        if answer in ["y","yes"]:
            save_load('load')
    else: 
        create_deck()

def main():
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

def create_deck():
    del deck[:]
    del discard[:]
    for card in cards:
        for suit in suits:
            deck.append(card+suit)

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

def save_load(state):
    # save
    if state == "save":
        with codecs.open('ColostleDeck.save', 'w', 'utf-8') as f:
            for i in deck:
                f.write('%s\n' %i)
        with codecs.open('ColostleDiscard.save', 'w', 'utf-8') as g:
            for x in discard:
                g.write('%s\n' %x)
    # load
    if state == "load":
        with codecs.open('ColostleDeck.save', 'r', 'utf-8') as h:
            for i in h.readlines():
                deck.append(i)
        with codecs.open('ColostleDiscard.save', 'r', 'utf-8') as d:
            for x in d.readlines():
                discard.append(x)
        os.remove('ColostleDeck.save')
        os.remove('ColostleDiscard.save')
    return

def quit():
    # quit
    print("")
    save = input("Want to save the deck? ")
    if save in ["y","yes"]:
        save_load('save')
    print("Thanks for playing")
    sys.exit()

if __name__ == "__main__":
    try:
        init()
        while True:
            main()
    except KeyboardInterrupt:
        quit()
