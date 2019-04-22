import numpy as np
import pyperclip


def get_cpf_digits():
    cpf_digits = 9
    return np.random.random_integers(0, 9, cpf_digits)


def get_last_digit_from_int(value):
    return int(repr(value)[-1])


def get_digit(arr, counter):
    arr_sum = 0
    for digit in arr:
        arr_sum += digit * counter
        counter -= 1
    div_rest = arr_sum % 11
    result = 11 - div_rest
    return get_last_digit_from_int(result)


def get_first_digit(arr):
    return get_digit(arr, 10)


def get_second_digit(arr):
    return get_digit(arr, 11)


def get_formatted_cpf(arr, first_digit, second_digit):
    formatted_cpf = ""
    counter = 1

    for digit in arr:
        formatted_cpf += str(digit)
        if counter % 3 == 0 and counter < len(arr):
            formatted_cpf += "."
        counter += 1
    formatted_cpf += "-"
    formatted_cpf += str(first_digit)
    formatted_cpf += str(second_digit)
    return formatted_cpf


def get_cpf():
    cpf_array = get_cpf_digits()
    digit_one = get_first_digit(cpf_array)
    cpf_with_first_digit = list(cpf_array)
    cpf_with_first_digit.append(digit_one)
    return get_formatted_cpf(cpf_array, digit_one, get_second_digit(cpf_with_first_digit))


def show_result(cpf_formatted):
    print("Fake CPF")
    pyperclip.copy(cpf_formatted)
    print(cpf_formatted)
    print("Copied to clipboard")


show_result(get_cpf())
