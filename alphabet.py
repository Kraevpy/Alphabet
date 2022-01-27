import string


class Alphabet:
    '''Метод где определены два динамических свойства lang-язык,letters-список букв'''

    def __init__(self, language, list_letters):
        self.lang = language
        self.letters = list(list_letters)

    '''Выводим английский алфавит который взяли из модуля srting ,string.ascii_uppercase  '''

    def print(self):
        print(self.letters)

    '''Выводим с помощью функции len() длинну из колличества букв в алфавите letters <-- list(list_letters)'''

    def letters_num(self):
        len({self.letters})


class EngAlphabet(Alphabet):
    '''__letters_num = 26 приватно статическое свойство которое хранит количество букв в алфавите '''

    __letters_num = 26

    '''Тут вызывается родительский метод благодаря функции super(). получаем доступ 
    к свойству родительского класса, в качестве пораметров предается язык "English  "En" " и Алфавит 
    который я по условию задачи позаиствовал из модуля "string" --> "ascii_uppercase" <-- является английским алфавитом
    в верхнем регистре'''

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    '''функция принимает букву проверяет относится ли буква к английскому алфавиту приводя ее в верхний регистр т.к 
    "ascii_uppercase" нам
     предастовляет алфавит в верхнем регистре и пользователь может ввести в нижнем регистре'''

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return f'Буква {letter} относится к английскому алфавиту '
        return f'Буква {letter} не относится к английскому алфавиту '

    '''Возвращаем количество букв а алфавите, __letters_num это приватное статическое свойство которое хранит
     количество букв в алфавите '''

    def letters_num(self):
        return EngAlphabet.__letters_num

    '''@staticmethod <-- статический метод который просто возвращает пример текста на английском языке'''

    @staticmethod
    def example():
        return 'Ignat you will be a very good boss'
