import random

MAX_SIDE = 6
MIN_SIDE = 1
MAX_BET = 100
MIN_BET = 1
number_of_faces = ['langur', 'burja','chidi', 'surat', 'paan', 'ita']
def deposit():
    while True:
        amount = input("enter the amount you want to deposit")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("enter amount greater than zero.")
        else:
            print("enter a amount in digits")
    return amount
def get_sides():
    while True:
        sides = input(f"enter the number of sides you want to choose to bet {MAX_SIDE}-{MIN_SIDE}")
        if sides.isdigit():
            sides = int(sides)
            if MAX_SIDE >= sides >= MIN_SIDE:
                break
            else:
                print("enter the valid number of sides.")
        else:
            print("enter the number of sides in digits")
    return sides
def get_bet():
    while True:
        bet = input(f"enter the amount of bet in each side {MAX_BET}-{MIN_BET}")
        if bet.isdigit():
            bet = int(bet)
            if MAX_BET >= bet >= MIN_BET:
                break
            else:
                print("enter a valid bet.")
        else:
            print("enter the bet amount in digits")
    return bet

def get_faces(s):
    sides= s
    face = []
    for _ in range(sides):
        while True:
            faces = input("type \ns for surat\nc for chidi\np for pan\ni for ita\nb for burja\nl for langur")
            if faces.isalpha():
                faces = str(faces)
                if faces =='s':
                    face.append('surat')
                    break
                elif faces == 'c':
                    face.append('chidi')
                    break
                elif faces == 'p':
                    face.append('paan')
                    break
                elif faces == 'i':
                    face.append('ita')
                    break
                elif faces == 'b':
                    face.append('burja')
                    break
                elif faces == 'l':
                    face.append('langur')
                    break
                else:
                    print("enter a valid bet.")
            else:
                print("enter the bet amount in valid letter")
    return face

def spin():
    my_list = []
    for _ in range(6) :
        random_face= random.choice(number_of_faces)
        my_list.append(random_face)
    print("the result after the spin is ", end="")
    return my_list

def check(balance,number_of_sides,bet_amount):
    while True:
        total_bet_amount = bet_amount * number_of_sides
        if total_bet_amount > balance:
            print(f"your current balance is not enough for the total amount of bet. your current balance is {balance}")
            bet_amount = get_bet()
        else:
            break
    print("your current balance is", balance)
    print("you chose " + str(number_of_sides) + " sides")
    print("your total amount of bet is $", total_bet_amount)
def display_faces(faces_afterspin):
    for i in range(6):
        if i < 5:
            print(faces_afterspin[i], end=":")
        else:
            print(faces_afterspin[i], end="")
def total_face_count(faces_after_spin):

    b_count = faces_after_spin.count('burja')
    if b_count < 2:
        b_count = 0
    l_count = faces_after_spin.count('langur')
    if l_count < 2:
        l_count = 0
    s_count = faces_after_spin.count('surat')
    if s_count < 2:
        s_count = 0
    c_count = faces_after_spin.count('chidi')
    if c_count < 2:
        c_count = 0
    p_count = faces_after_spin.count('paan')
    if p_count < 2:
        p_count = 0
    i_count = faces_after_spin.count('ita')
    if i_count < 2:
        i_count = 0
    return b_count,l_count,s_count,c_count,p_count,i_count
def winnings(bet_amt ,b_count ,l_count ,p_count ,i_count ,s_count ,c_count ,selected_faces ):
    intial_win = 0
    win = 0
    if 'langur' in selected_faces:
        if l_count >1:
            win = l_count*bet_amt+bet_amt
        else:
            win = l_count * bet_amt
    intial_win = intial_win+win
    win=0
    if 'burja' in selected_faces:
        if b_count >1:
            win = b_count * bet_amt + bet_amt
        else:
            win = b_count * bet_amt
    intial_win = intial_win+win
    win = 0
    if 'surat' in selected_faces:
        if s_count > 1:
            win = s_count * bet_amt + bet_amt
        else:
            win = s_count * bet_amt
    intial_win = intial_win+win
    win = 0
    if 'chidi' in selected_faces:
        if c_count >1:
            win = c_count * bet_amt + bet_amt
        else:
            win = c_count * bet_amt
    intial_win = intial_win+win
    win = 0
    if 'paan' in selected_faces:
        if p_count > 1:
            win = p_count * bet_amt + bet_amt
        else:
            win = p_count * bet_amt
    intial_win = intial_win+win
    win = 0
    if 'ita' in selected_faces:
        if i_count >1:
            win = i_count * bet_amt + bet_amt
        else:
            win = i_count * bet_amt
    intial_win = intial_win+win
    return intial_win
def main():
    balance = deposit()
    while True:
        number_of_sides = get_sides()
        bet_amount = get_bet()
        check(balance,number_of_sides,bet_amount)
        total_faces= get_faces(number_of_sides)
        for i in range(number_of_sides):
            print(total_faces[i])
        face_after_spin = spin()
        display_faces(face_after_spin)
        burja_count, langur_count, surat_count, chidi_count,paan_count, ita_count = total_face_count(face_after_spin)
        total_win = winnings(bet_amount,burja_count,langur_count,paan_count,ita_count,surat_count,chidi_count,total_faces)
        final_win= balance+total_win-bet_amount*number_of_sides
        print("\nyou won ", total_win)
        print("the current balance after the spin is", final_win)
        balance=final_win
        print("do you want to continue?")
        t = input("please enter q to quit and c to continue")
        if t == 'q':
            break
        if balance == 0:
            balance = deposit()
main()

