from random import randint

def generate_numbers():
    '(None) -> list'
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)
    
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    guess = []

    print('숫자 3개를 하나씩 차례대로 입력하세요.')
    for num in [1, 2, 3]:
        while True:
            user_input = int(input(f'{num}번째 숫자를 입력하세요:'))
            if user_input > 9 or user_input < 0:
                print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
                continue
            elif user_input in guess:
                print('중복되는 숫자입니다. 다시 입력하세요.')
                continue
            else:
                guess.append(user_input)
                break
    return guess

def get_score(guess, answer):
    '''(list, list) -> tuple'''
    strike_count = 0
    ball_count = 0

    for index in range(3):
        if guess[index] in answer:
            if guess[index] == answer[index]:
                strike_count += 1
            else:
                ball_count += 1
    return strike_count, ball_count

def main():
    ANSWER = generate_numbers()
    tries = 0

    while True:
        tries += 1
        guess = take_guess()
        s, b = get_score(guess, ANSWER)

        print(f'{s}S, {b}B\n')
        
        if s == 3:
            break

    print(f'축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.')

# game start
if __name__ == '__main__':
    main()







    

    
    






