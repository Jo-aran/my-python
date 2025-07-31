import random

number_to_guess = random.randint(1, 100)
tries = 0

print("🎲 숫자 맞추기 게임!")
print("1부터 100 사이의 숫자를 맞춰보세요.")

while True:
    user_input = input("당신의 추측: ")
    
    if not user_input.isdigit():
        print("숫자를 입력해주세요!")
        continue

    guess = int(user_input)
    tries += 1

    if guess == number_to_guess:
        print(f"정답입니다! {tries}번 만에 맞췄어요! 🎉")
        break
    elif guess < number_to_guess:
        print("너무 작아요!")
    else:
        print("너무 커요!")
