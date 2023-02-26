def up_the_letters():
    """
    Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами
    """
    user_input = input("Вам нужно тут что-то написать")
    up_words = user_input.upper()
    print(up_words)


def up_first_letters():
    """
     Функция, которая делает заглавными первые буквы каждого слова в строке, поступившей на вход функции
    """
    user_input = input("Вам опять нужно что-то написать")
    user_words = user_input.title()
    print(user_words)
