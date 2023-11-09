import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print(f"Буквы алфавита: {self.letters}")

    def letters_num(self):
        count_of_letters = 0
        for i in self.letters:
            if i.islower():
                count_of_letters += 1
        print(f"Количество букв в алфавите: {count_of_letters}")


class EngAlphabet(Alphabet):
    __leters_num = 26

    def __init__(self):
        super().__init__("En", list(string.ascii_letters))

    def is_en_letter(self, letter):
        if letter in self.letters:
            return True

    def letters_num(self):
        return self.__leters_num

    @staticmethod
    def example():
        return '''\nPython is a high-level general-purpose programming language with dynamic strict typing 
and automatic memory management, focused on improving developer productivity, code readability and quality, 
as well as ensuring the portability of programs written in it.\n'''


eng_alphabet = EngAlphabet()
eng_alphabet.print_alphabet()
print(f"Количестов букв алфавита: {eng_alphabet.letters_num()}")
print("\nПриндалежит ли буква 'A' алфавииу?\n", eng_alphabet.is_en_letter('A'))
print("\nМетод example() - статические метод, выводит текст на английском языке.\n", eng_alphabet.example())