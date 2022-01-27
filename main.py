from alphabet import *

if __name__ == '__main__':
    test_EngAlphabet = EngAlphabet()
    test_EngAlphabet.print()
    print(test_EngAlphabet.letters_num())
    print(test_EngAlphabet.is_en_letter('F'))
    print(test_EngAlphabet.is_en_letter('Щ'))
    print(EngAlphabet.example())
