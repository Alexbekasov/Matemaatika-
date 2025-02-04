import random

print("Выберите уровень сложности: ")
print("1 - Легко (+, -)")
print("2 - Средне (+, -, *)")
print("3 - Сложно (+, -, *, /, **)")

level = int(input("Введите номер уровня (1-3): "))
questions = int(input("Сколько примеров хотите решить? "))

correct = 0  

for _ in range(questions):
    num1 = random.randint(1, 100)  
    num2 = random.randint(1, 100)  
    
    if level == 1:
        operators = ["+", "-"]
    elif level == 2:
        operators = ["+", "-", "*"]
    else:
        operators = ["+", "-", "*", "/", "**"]

    op = random.choice(operators)

    if op == "/":
        num1 = num1 * num2  # Stobi delenie bilo celim

    question = f"{num1} {op} {num2}"
    answer = eval(question) 

    user_answer = float(input(f"Решите: {question} = "))

    if round(user_answer, 2) == round(answer, 2):
        print("Правильно!")
        correct += 1
    else:
        print("Ошибка. Правильный ответ:", round(answer, 2))

score = (correct / questions) * 100

if score < 60:
    grade = "Hinne 2"
elif score < 75:
    grade = "Hinne 3"
elif score < 90:
    grade = "Hinne 4"
else:
    grade = "Hinne 5"

print(f"Вы решили {correct} из {questions} примеров.")
print(f"Оценка: {grade}")

