import sys
import importlib
from datetime import datetime
import questions


def choose_category(categories):
    print("Виберіть категорію (або введіть 'вихід' для виходу):")
    for index, category in enumerate(categories):
        print(f"{index + 1}. {category}")
    choice = input("-----------------\nВведіть номер категорії: ")
    if choice.lower() == "вихід":
        exit_program()  # Викликати функцію виходу
    try:
        choice_index = int(choice) - 1
        if choice_index < 0 or choice_index >= len(categories):
            print("-----------------\nНекоректний вибір категорії\n-----------------")
            return None
        return categories[choice_index]
    except ValueError:
        print("-----------------\nНекоректний вибір категорії\n-----------------")
        return None


def choose_question(questions):
    print("-----------------\nВиберіть питання:")
    for index, question in enumerate(questions):
        print(f"{index + 1}. {question.get_question_text()}")
    choice = input("-----------------\nВведіть номер питання: ")
    try:
        choice_index = int(choice) - 1
        if choice_index < 0 or choice_index >= len(questions):
            print("-----------------\nНекоректний вибір питання\n-----------------")
            return None
        return questions[choice_index]
    except ValueError:
        print("-----------------\nНекоректний вибір питання\n-----------------")
        return None


def save_dialog(dialog, dialog_file):
    for entry in dialog:
        role = entry["role"]
        message = entry["message"]
        dialog_file.write(f"{role}: {message}\n")
    dialog_file.write("\n")


def get_available_categories():
    available_categories = []
    classes = [cls for cls in questions.__dict__.values() if isinstance(cls, type)]
    categories = [cls.category for cls in classes if hasattr(cls, "category")]
    available_categories.extend(categories)
    return list(set(available_categories))


def load_questions_module(module_name):
    return importlib.import_module(module_name)


def exit_program():
    print("-----------------\nРадий був поспілкуватись, до зустрічі!")
    sys.exit()


def handle_numeric_input(question):
    while True:
        user_input = input("Введіть відповідь: ")
        current_dialog.append({"role": "Користувач", "message": user_input})

        try:
            if question.input_count == 1:
                answer = question.answer_question(int(user_input))
            else:
                arguments = list(map(int, user_input.split()))
                if len(arguments) != question.input_count:
                    print(f"-----------------\nНекоректний ввід. Будь ласка, введіть {question.input_count} числа.\n-----------------")
                    continue
                answer = question.answer_question(*arguments)

            return answer
        except ValueError:
            print("Некоректний ввід. Будь ласка, введіть цілі числа.")


def handle_text_input(question):
    user_input = input("Введіть відповідь: ")
    current_dialog.append({"role": "Користувач", "message": user_input})

    return question.answer_question(user_input)


# Основний код
questions_module = load_questions_module("questions")

categories = get_available_categories()  # Список доступних категорій
questions = [getattr(questions_module, question_name)() for question_name in dir(questions_module) if
             isinstance(getattr(questions_module, question_name), type) and
             hasattr(getattr(questions_module, question_name), "category")]

current_dialog = []
dialog_file = None


print(f"-----------------\nВітаю, мене звати чатбот. Ви можете задати питання з таких тем: {' '.join(categories)} \n-----------------")

while True:
    category = choose_category(categories)
    if category is None:
        continue

    filtered_questions = [question for question in questions if question.category == category]

    question = choose_question(filtered_questions)
    if question is None:
        continue

    print("-----------------\nЗадано питання:", question.get_question_text())
    current_dialog.append({"role": "Користувач", "message": question.get_question_text()})

    if not question.requires_input():
        answer = question.answer_question()
    else:
        if question.input_type == "numeric":
            answer = handle_numeric_input(question)
        elif question.input_type == "text":
            answer = handle_text_input(question)
        else:
            print("Некоректний тип вводу")
            continue

    print("Відповідь:", answer)
    current_dialog.append({"role": "Бот", "message": f"{answer}\n-----------------"})

    if dialog_file is None:
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f"dialogs/dialog-{current_time}.txt"
        dialog_file = open(filename, "a")  # Відкрити новий файл діалогу
        # dialog_file.write(f"=== {current_time} ===\n")

    choice = input("-----------------\nПродовжити? (так/ні): ")
    if choice.lower() == "вихід":
        exit_program()
    elif choice.lower() == "ні":
        save_dialog(current_dialog, dialog_file)
        exit_program()
    elif choice.lower() != "так" and choice.lower() != "ні":
        print("-----------------\nЯ не знаю такої команди\n-----------------")

if dialog_file is not None:
    dialog_file.close()  # Закрити файл діалогу, якщо він був відкритий
