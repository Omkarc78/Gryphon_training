# day5.py
# Rules:
# 1.It should read your name
# 2.It should ask a question like(what is the square of { number },number should be any number from 1-100)
# 3.If users answer is right then score increased by +10
# 4.If wrong answer score should decreased by -5
# 5.it should ask questions again and again but after answering to the question also after updating score
# 6.it should ask(do you want to continue) if not display "Looser"
# 7.it may ask ("what is the square root of a perfect square number 1-10000")
# 8.keep tracking the time at the time of giving the player name 
# 9.calculate the answering time for each queastion by player
# 10.If score reach 200 print you are winner
import random
import time
import excep

def select_num():
    return random.randint(1, 100)

def select_square_root_num():
    return random.choice([i * i for i in range(1, 101)])  # Perfect squares from 1 to 10000

user_name = input("Enter your name: ")
start_time = time.time()  # Rule 8: Track when player started
score = 0

while True:
    question_type = random.choice(["square", "squareroot"])

    if question_type == "square":
        num = select_num()
        print(f"\nWhat is the square of {num}?")
        correct_ans = num * num
    else:
        num = select_square_root_num()
        print(f"\nWhat is the square root of {num}?")
        correct_ans = int(num ** 0.5)

    question_start_time = time.time()  # Rule 9: Start timer for this question
    user_ans = excep.excep()
    question_end_time = time.time()

    time_taken = round(question_end_time - question_start_time, 2)

    if user_ans == correct_ans:
        score += 10
        print(f"Correct! (+10 points)")
    else:
        score -= 5
        print(f"Wrong! The correct answer was {correct_ans} (-5 points)")

    print(f"Time taken: {time_taken} seconds")
    print(f"{user_name}, your current score is: {score}")

    ch = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if ch != "yes":
        if score>=200:
            print("You are Winner")
            break
        else:
            print("You are looser")
            break
       
