# "Крестики - нолики"
# Используются структурная и процедурные парадигмы. 

print()
print("---------", "Крестики-нолики", "---------")

board = list(range(1, 10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|",  board[1 + i * 3],
              "|",  board[2 + i * 3], "|")
        print("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        print()
        player_answer = input(f'Куда ставить {player_token} ? ')
        print()
        try:
            player_answer = int(player_answer)
        except:
            print("Некоректный ввод - попробуй ещё")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Клетка уже занята!")
        else:
            print("Введи число от 1 до 9")

def check_win(board):
    win_position = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_position:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def start_game(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(f'Выиграл игрок {tmp}')
                win = True
        if counter == 9:
            print("Ничья")
            win = True
    draw_board(board)

start_game(board)

