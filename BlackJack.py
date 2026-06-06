print("Welcome to Black Jack Game :) ")

import random
def deal_cards():  #picks random cards
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def cal_scores(cards):  #calculates the score of each player
    if sum(cards) == 21 and len(cards) == 2: 
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):   #compare between players
    if u_score == c_score:
        return "Draw :) "
    elif c_score == 0:
        return "Lose, Opponent has BlackJack. "
    elif u_score == 0:
        return "Win, You have BlackJack. "
    elif c_score > 21:
        return "Opponent went over, You win..! "
    elif u_score > 21:
        return "You went over, You lose..!!"
    elif u_score > c_score:
        return "You win..!! "
    else:
        return "You Lose :) "


def play_game():  
    user_cards = [] 
    computer_cards = []
    user_score = -1   # we used this to overcome the error in next while loop
    computer_score = -1  #same as above comment
    is_game_over = False

    for _ in range(2):      # we want two cards for each
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    while not is_game_over:
        user_score = cal_scores(user_cards)
        computer_score = cal_scores(computer_cards)

        print(f"Your cards : {user_cards}, current score : {user_score}")
        print(f"Computer first card : {computer_cards[0]}")
        if user_score == 0 or computer_score ==0 or user_score > 21:   
            is_game_over = True
        else:    # This decides to continue or end the game
            user_should_deal = input("Type 'y' to get another card or 'n' to pass : ")
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score == 0 or computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = cal_scores(computer_cards)

    print(f"Your final hand : {user_cards}, final score : {user_score}")
    print(f"Computer's final hand : {computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score))  
while input("Do you want to play a game of Black Jack? Type 'y' or 'n' : ") == 'y':   # To restart the game
    print("\033c", end="")
    play_game()


