import random

def get_user_choice():
    user_choice = input("Выберите: камень, ножницы, бумага, ящерица или спок? ").lower()
    while user_choice not in ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']:
        print("Неверный ввод. Пожалуйста, выберите камень, ножницы, бумагу, ящерицу или спок.")
        user_choice = input("Выберите: камень, ножницы, бумага, ящерица или спок? ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага', 'ящерица', 'спок'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif ((user_choice == 'камень' and computer_choice in ['ножницы', 'ящерица']) or
          (user_choice == 'ножницы' and computer_choice in ['бумага', 'ящерица']) or
          (user_choice == 'бумага' and computer_choice in ['камень', 'спок']) or
          (user_choice == 'ящерица' and computer_choice in ['бумага', 'спок']) or
          (user_choice == 'спок' and computer_choice in ['камень', 'ножницы'])):
        return "Вы выиграли!"
    else:
        return "Вы проиграли."

def game():
    print("Добро пожаловать в игру 'камень, ножницы, бумага, ящерица, спок'!")
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "Вы выиграли!":
            user_score += 1
        elif result == "Вы проиграли.":
            computer_score += 1
        if user_score == 3 or computer_score == 3:
            print("Победитель серии игр:")
            if user_score == 3:
                print("Вы!")
            else:
                print("Компьютер!")
            break
    play_again = input("Хотите сыграть еще раз? (да/нет) ").lower()
    if play_again != 'да':
        print("Спасибо за игру! До свидания.")

game()