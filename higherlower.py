import random
from art import logo, vs
from dictionary import data

def get_random_data():
    return random.choice(data)
    
        
        

def format_data(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name} a {description} from {country}"

def check_ans(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess=="a"
    else:
        return guess=="b"

def game():
    print(logo)
    score=0
    game_should_continue=True
    
    account_a=get_random_data()
    account_b=get_random_data()
    # if account_a==account_b:
    while game_should_continue:
        account_a = account_b
        account_b=random.choice(data)
        while account_a==account_b:
            account_b= get_random_data()
        print(f"compare A: {format_data(account_a)}")
        print(vs)
        print(f"compare B:{format_data(account_b)}")
        
        
        guess=input("who has more follower. Type 'A'or 'B'.").lower()
        a_follower_count=account_a["follower_count"]    
        b_follower_count=account_b["follower_count"]
        is_correct=check_ans (guess, a_follower_count, b_follower_count)
        
        if is_correct:
            score+=1
            print(f"you are right. Current score is {score}")
        else:
            game_should_continue=False
            print(f"that wrong. Final score is {score}")    
            
game()            
            
        
        
        
    
    

