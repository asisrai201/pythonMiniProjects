import random

questions = [
    "1. What country has the highest life expectancy?",
    "2. Where would you be if you were standing on the Spanish Steps?",
    "3. Which language has the more native speakers: English or Spanish?",
    "4. What is the most common surname in the United States?",
    "5. What disease commonly spread on pirate ships?",
    "6. Who was the Ancient Greek God of the Sun?",
    "7. What was the name of the crime boss who was head of the feared Chicago Outfit?",
    "8. What year was the United Nations established?",
    "9. Who has won the most total Academy Awards?",
    "10. What artist has the most streams on Spotify?"
]
options =[
    "A. Nepal B. UK C. Bangladesh D. Hongkong",
    "A.Rome B. Spain C. China D. India",
    "A. Roman B. Indian C. American D. Spanish",
    "A. Johnathan B. Smith C. Frank D. Stark",
    "A. Fever B. Common cold C. Scurvy D. Asthma",
    "A. Hercules B. Zeus C. Thor D. Apollo",
    "A. Dominique B. John C. Abraham D. Al Capone",
    "A. 1998 B. 1945 C. 1955 D. 1940",
    "A. Walt disney B. Marvel C. DC D. Panaroma",
    "A. Taylor swift B. Drake C. Ariana grande D. Eminem"
]
answer = ["D", "A", "D", "B","C", "D", "D", "B","A", "B"]
def ask_question():
    guessed_answer =[]
    count=0
    while count< 11:
        print(questions[count])
        print("______________________________________________")
        print(options[count])
        print("______________________________________________")
        answer = input("please type correct option")
        if answer.isalpha():
            answer = answer.capitalize()
            print("______________________________________________")
            if answer == "A" or answer== "B" or answer == "C" or answer == "D":
                print("You have selected option: ", answer)
                guessed_answer.append(answer)
                count += 1
            else:
                print("please choose one of the options A:B:C:D")
        else:
            print("please type valid option")
    return(guessed_answer)
def check_answer(guess):
    score=0
    for i in range(0,len(questions)):
        if guess[i] == answer[i]:
            score += 1
        else:
            score += 0
    return score
def display_score(total):
    percent= (total/10)*100
    percent= str(percent)
    print(f"your scored {percent}% in this quiz")
def main():
    guesses = ask_question()
    score = check_answer(guesses)
    display_score(score)
main()




