import time 
import os 
import random
from questions import questions

def load_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    return 0

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def main():
    print("Welcome to the Quiz Game!")
    print("Select difficulty level: 1. Easy 2. Medium 3. Hard")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        selected_questions = questions["easy"]
    elif choice == '2':
        selected_questions = questions["medium"]
    elif choice == '3':
        selected_questions = questions["hard"]
    else:
        print("Invalid choice! Defaulting to Easy.")
        selected_questions = questions["easy"]

    random.shuffle(selected_questions)
    score = 0

    for q in selected_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYour final score is: {score}/{len(selected_questions)}")
    
    high_score = load_high_score()
    if score > high_score:
        print("Congratulations! You set a new high score!")
        save_high_score(score)
    else:
        print(f"The current high score is: {high_score}")
    
if __name__ == "__main__":
    main()