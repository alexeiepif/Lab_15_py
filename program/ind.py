#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def morze_decorator(func):
    morze = {
        'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.',
        'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',
        'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--',
        'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...',
        'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
        'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--',
        'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-···-'
    }

    def wrapper(arg):
        arg = func(arg)
        return ' '.join([morze[char] for char in arg if char in morze])
    return wrapper


@morze_decorator
def process_string(s):
    s = ' '.join(s.lower().split())
    return s


if __name__ == "__main__":
    input_string = "ПрИвЕт   Мир    Я Алексей"
    output_string = process_string(input_string)
    print(f"{output_string = }")
