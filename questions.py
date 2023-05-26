import math
from datetime import datetime
import random

class AmpereFormula:
    category = "фізика"
    input_type = "numeric"
    input_count = 2

    def get_question_text(self):
        return "Введіть значення B та L для обчислення струму I за формулою Ампера:"

    def answer_question(self, b, l):
        if not all(isinstance(value, (int, float)) for value in [b, l]):
            return "Введіть числові значення для обчислення струму I."

        i = b * l
        return f"B = {b}, L = {l}. Значення I: {i}"

    def requires_input(self):
        return True


class BoyleMarriottLaw:
    category = "фізика"
    input_type = "numeric"
    input_count = 3

    def get_question_text(self):
        return "Обчислити P1 або V1?\n- Обчислити P1\n- Обчислити V1"

    def answer_question(self, choice, p2, v2):
        if not isinstance(choice, int) or choice not in [1, 2]:
            return "Введіть коректний номер варіанту."

        if not isinstance(p2, (int, float)) or not isinstance(v2, (int, float)):
            return "Введіть числові значення для P2 та V2."

        if choice == 1:
            v1 = float(input("Введіть значення V1: "))
            if not isinstance(v1, (int, float)):
                return "Введіть числове значення для V1."

            p1 = (p2 * v2) / v1
            return f"P2 = {p2}, V2 = {v2}, V1 = {v1}. Значення P1: {p1}"
        else:
            p1 = float(input("Введіть значення P1: "))
            if not isinstance(p1, (int, float)):
                return "Введіть числове значення для P1."

            v1 = (p2 * v2) / p1
            return f"P2 = {p2}, V2 = {v2}, P1 = {p1}. Значення V1: {v1}"

    def requires_input(self):
        return True


class PlankConstant:
    category = "фізика"

    def get_question_text(self):
        return "Вивести сталу Планка?"

    def answer_question(self):
        return "h = 6.62607015 × 10^(-34) J·s"

    def requires_input(self):
        return False

class CircleArea:
    category = "математика"
    input_type = "numeric"
    input_count = 1

    def get_question_text(self):
        return "Введіть радіус кола:"

    def answer_question(self, radius):
        if not isinstance(radius, (int, float)):
            return "Введіть число (радіус) для обчислення площі кола."

        area = math.pi * float(radius) * float(radius)
        return f"Площа кола з радіусом {radius}: {area:.2f}"

    def requires_input(self):
        return True


class FibonacciNumber:
    category = "математика"
    input_type = "numeric"
    input_count = 1

    def get_question_text(self):
        return "Введіть номер n і отримайте n-те число Фібоначчі:"

    def answer_question(self, n):
        if not isinstance(n, int) or n < 0:
            return "Введіть ціле додатнє число для визначення числа Фібоначчі."

        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

        return fib_sequence[n]

    def requires_input(self):
        return True


class SineCosine:
    category = "математика"
    input_type = "numeric"
    input_count = 1

    def get_question_text(self):
        return "Введіть кут в градусах і отримайте значення sin(x) та cos(x):"

    def answer_question(self, *args):
        if len(args) != 1 or not isinstance(args[0], (int, float)):
            return "Введіть число (градуси) для визначення значення sin та cos."

        angle = args[0]
        x = math.radians(angle)
        sin_value = round(math.sin(x), 4)
        cos_value = round(math.cos(x), 4)
        return f"sin({angle}°) = {sin_value}, cos({angle}°) = {cos_value}"

    def requires_input(self):
        return True


class IntersectionPoint:
    category = "математика"
    input_type = "numeric"
    input_count = 4

    def get_question_text(self):
        return "Знайти координати точки перетину двох прямих, заданих векторами (x1, y1) та (x2, y2):"

    def answer_question(self, *args):
        if len(args) != self.get_input_count():
            return f"Потрібно ввести {self.get_input_count()} числа."

        x1, y1, x2, y2 = args
        if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2]):
            return "Координати повинні бути числами."

        k1 = y1 / x1
        k2 = y2 / x2
        b1 = 0 if k1 == 0 else y1 / k1
        b2 = 0 if k2 == 0 else y2 / k2

        if x1 == x2 or k1 == k2:
            return "Прямі паралельні, немає точки перетину."

        x = (b2 - b1) / (k1 - k2)
        y = k1 * x

        return f"Координати точки перетину: ({x}, {y})"

    def requires_input(self):
        return True

    def get_input_count(self):
        return self.input_count


class PointFinder:
    category = "математика"
    input_type = "numeric"
    input_count = 4

    def get_question_text(self):
        return "Введіть координати точки А (x1, y1), відстань між точками (d) та напрямок (азимут) від точки А до " \
               "точки В (θ), щоб знайти координати точки В (x2, y2):"

    def answer_question(self, x1, y1, d, theta):
        if not all(isinstance(i, (int, float)) for i in [x1, y1, d, theta]):
            return "Введіть числові значення для координат точки А, відстані та напрямку."

        theta = math.radians(theta)  # переводимо градуси в радіани

        x2 = x1 + d * math.cos(theta)
        y2 = y1 + d * math.sin(theta)

        return f"Координати точки В: ({x2}, {y2})"

    def requires_input(self):
        return True


class WordsWithLetter:
    category = "філологія"
    input_type = "text"
    input_count = 2

    def get_question_text(self):
        return "Введіть фразу та літеру, і отримайте список слів з введеної фрази, які містять задану літеру (після слів поставте пробіл, а після останнього слова введіть літеру)"

    def answer_question(self, *args):
        if len(args) != self.input_count or not all(isinstance(arg, str) for arg in args):
            return "Введіть рядок та літеру."

        phrase = args[0]
        letter = args[1]

        words_with_letter = [word for word in phrase.split() if letter in word]

        if not words_with_letter:
            return f"У введеній фразі немає слів, які містять літеру '{letter}'."
        else:
            return f"Слова з введеної фрази, які містять літеру '{letter}': {', '.join(words_with_letter)}"

    def requires_input(self):
        return True


class DigitWords:  # work
    category = "філологія"
    input_type = "text"
    input_count = 1


    def get_question_text(self):
        return "Введіть список слів та отримайте список слів, які складаються лише з цифр:"

    def answer_question(self, *words):
        digit_words = []
        for word in words:
            if word.isdigit():
                digit_words.append(word)
        return digit_words

    def requires_input(self):
        return True


class WordCount:
    category = "філологія"
    input_type = "text"
    input_count = 1

    def get_question_text(self):
        return "Введіть текст для підрахунку кількості слів:"

    def answer_question(self, *args):
        if len(args) == 0:
            return "Введіть рядок тексту."

        text = " ".join(args)
        words = text.split()
        return f"Слів у введеному тексті {len(words)}"

    def requires_input(self):
        return True


class RemoveExtraSpaces:
    category = "філологія"
    input_type = "text"
    input_count = 1

    def get_question_text(self):
        return "Введіть текст для видалення зайвих пробілів:"

    def answer_question(self, *args):
        if len(args) != 1 or not isinstance(args[0], str):
            return "Введіть текст у вигляді рядка."

        text = " ".join(" ".join(args[0].split()) for text in args)
        return text

    def requires_input(self):
        return True


class PresentSimpleVsPresentContinuous:
    category = "філологія"

    def get_question_text(self):
        return "Яка різниця між Present Simple та Present Continuous?"

    def answer_question(self):
        return "Present Simple - це час, що відповідає за регулярні дії або факти, що стосуються нашого життя взагалі.\nНаприклад: I walk to work every day (Я ходжу на роботу кожен день).\nPresent Continuous - це час, що відповідає за дії, які відбуваються зараз або навколо моменту говоріння.\nНаприклад: I am walking to work now (Я йду на роботу зараз)."

    def requires_input(self):
        return False


class SomeVsAny:
    category = "філологія"

    def get_question_text(self):
        return "Яка різниця між Some та Any?"

    def answer_question(self):
        return "Some - використовується в позитивних реченнях для позначення певної кількості або " \
               "кількох.\nНаприклад: Can I have some water? (Можна мені дати трохи води?).\nAny - використовується в " \
               "заперечних реченнях, питальних реченнях та в умовах. Він може означати будь-яку кількість або " \
               "жодної.\nНаприклад: I don't have any money (У мене немає жодних грошей), Do you have any questions? (" \
               "У вас є якісь запитання?). "

    def requires_input(self):
        return False


class GetUkrainianSong:
    category = "філологія"

    def __init__(self):
        self.songs = [
            "Червона рута",
            "Ой, на горі два дубки",
            "Колискова для Анни",
            "Сумна мелодія",
            "Ой, у лузі червона калина",
            "Їхали козаки",
            "В долині туманів",
            "Карпати, Карпати"
        ]

    def get_question_text(self):
        return "Назви будь яку українську пісню"

    def answer_question(self):
        return random.choice(self.songs)

    def requires_input(self):
        return False


class NounExplained:
    category = "філологія"

    def get_question_text(self):
        return "Що таке іменник?"

    def answer_question(self):
       return "іменник - це частка мови, що позначає назву предмета, явища, істоти або їх ознаку. Він може мати різні форми відмінювання, числа та роду, залежно від мови. У мовленні він використовується для найменування різних об'єктів та для створення складних речень."

    def requires_input(self):
        return False



class HighestMountains:
    category = "географія"

    def get_question_text(self):
        return "Назвіть 5 найвищих гір в світі та їхні висоти:"

    def answer_question(self):
        mountains = [
            {"name": "Еверест", "height": "8,848 м"},
            {"name": "Канченджанга", "height": "8,586 м"},
            {"name": "Лхотсе", "height": "8,516 м"},
            {"name": "Макалу", "height": "8,485 м"},
            {"name": "Чо-Ойю", "height": "8,188 м"},
        ]

        result = ""
        for mountain in mountains:
            result += f"{mountain['name']}: {mountain['height']}\n"
        return result

    def requires_input(self):
        return False


class Azimuth:
    category = "географія"
    input_type = "numeric"
    input_count = 4

    def get_question_text(self):
        return "Введіть координати точок A (x1, y1) та B (x2, y2), щоб знайти азимут від A до B:"

    def answer_question(self, *args):
        if len(args) != self.get_input_count():
            return f"Потрібно ввести {self.get_input_count()} числа."

        if not all(isinstance(coord, (int, float)) for coord in args):
            return "Координати повинні бути числовими значеннями."

        x1, y1, x2, y2 = args
        dx = x2 - x1
        dy = y2 - y1
        azimuth = math.degrees(math.atan2(dy, dx))

        return f"Азимут від точки A до точки B: {azimuth:.2f} градусів."

    def requires_input(self):
        return True

    def get_input_count(self):
        return self.input_count


class GetSeason:
    category = "географія"

    def get_question_text(self):
        return "Яка пора року зараз?"

    def answer_question(self):
        month = datetime.now().month
        if month in [12, 1, 2]:
            return "Зима"
        elif month in [3, 4, 5]:
            return "Весна"
        elif month in [6, 7, 8]:
            return "Літо"
        else:
            return "Осінь"

    def requires_input(self):
        return False


class DaysInYear:
    category = "географія"
    input_type = "numeric"
    input_count = 1

    def get_question_text(self):
        return "Введіть рік і отримайте кількість днів у цьому році:"

    def answer_question(self, year):
        if not isinstance(year, int) or year < 1:
            return "Введіть ціле додатнє число для визначення кількості днів у році."

        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return f"У {year} році є 366 днів."
        else:
            return f"У {year} році є 365 днів."

    def requires_input(self):
        return True


class UkrRegionsCount:
    category = "географія"

    def get_question_text(self):
        return "Скільки областей в Україні?"

    def answer_question(self):
        return "24 області і Автономна Республіка Крим"

    def requires_input(self):
        return False


class SpainCapital:
    category = "географія"

    def get_question_text(self):
        return "Яка столиця Іспанії?"

    def answer_question(self):
        return "Столиця Іспанії - Мадрид"

    def requires_input(self):
        return False


class HoursInDay:
    category = "географія"

    def get_question_text(self):
        return "Скільки годин в добі?"

    def answer_question(self):
       return "В добі 24 години"

    def requires_input(self):
        return False


class ContinentsCount:
    category = "географія"

    def get_question_text(self):
        return "Скільки є материків на Землі?"

    def answer_question(self):
       return "На Землі є 6 материків: Євразія, Австралія, Африка, Північна Америка, Південна Америка, Антарктида"

    def requires_input(self):
        return False


class SpringMonths:
    category = "географія"

    def get_question_text(self):
        return "Назви весняні місяці"

    def answer_question(self):
       return "Весняні місяці: березень, квітень, травень"

    def requires_input(self):
        return False


class CurrentTime:
    category = "час"

    def get_question_text(self):
        return "Отримайте поточний час:"

    def answer_question(self):
        return datetime.now().strftime("%H:%M:%S")

    def requires_input(self):
        return False














