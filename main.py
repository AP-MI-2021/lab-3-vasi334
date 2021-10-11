"""
Problema 1
"""


def patrat_perfect(n) -> bool:
    j = 1
    verificare = False

    while j * j <= n and not verificare:
        if n % j == 0 and n // j == j:
            verificare = True
        j += 1

    return verificare


def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:

    longest_list = 0
    actual_list = 0
    start = 0
    end = 0
    false_start = 0
    false_end = 0

    for index in range(0, len(lst)):
        if index == 0:
            if patrat_perfect(lst[index]):
                actual_list += 1
        elif index == len(lst) - 1:
            if patrat_perfect(lst[index]) and patrat_perfect(lst[index - 1]):
                actual_list += 1
                false_end = index
                if actual_list > longest_list:
                    longest_list = actual_list
                    start = false_start
                    end = false_end
            elif not patrat_perfect(lst[index]):
                if actual_list > longest_list:
                    longest_list = actual_list
                    start = false_start
                    end = false_end
            elif patrat_perfect(lst[index]) and actual_list == 0:
                start = index
                end = index
        elif patrat_perfect(lst[index]) and not patrat_perfect(lst[index - 1]):
            false_start = index
            actual_list += 1
        elif patrat_perfect(lst[index]) and patrat_perfect(lst[index - 1]):
            false_end = index
            actual_list += 1
        elif not patrat_perfect(lst[index]) and patrat_perfect(lst[index - 1]):
            if actual_list > longest_list:
                longest_list = actual_list
                start = false_start
                end = false_end
            actual_list = 0

    if start == 0 and end == 0:
        if patrat_perfect(lst[0]):
            return lst[start:end+1]
        else:
            return []
    elif end == 0:
        end = start

    return lst[start:end + 1]


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([9, 8, 9, 9, 16, 15]) == [9, 9, 16]
    assert get_longest_all_perfect_squares([7]) == []
    assert get_longest_all_perfect_squares([9]) == [9]
    assert get_longest_all_perfect_squares([1, 7, 25, 16, 4, 3]) == [25, 16, 4]
    assert get_longest_all_perfect_squares([2, 7]) == []
    assert get_longest_all_perfect_squares([2, 9]) == [9]
    assert get_longest_all_perfect_squares([9, 2]) == [9]


"""
Problema 11
"""


def numbers_of_1_in_binary(lst: list[int]) -> bool:
    count = 0
    while lst[0] != 0:
        if lst[0] % 2 == 1:
            count += 1
        lst[0] //= 2

    count_1 = 0
    for i in range(1, len(lst)):
        while lst[i] != 0:
            if lst[i] % 2 == 1:
                count_1 += 1
            lst[i] //= 2
        if count_1 != count:
            return False
        count_1 = 0

    return True


def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    subsecventa_maxima = []

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if numbers_of_1_in_binary(lst[i:j+1]) and len(lst[i:j+1]) > len(subsecventa_maxima):
                subsecventa_maxima = lst[i:j+1]

    return subsecventa_maxima


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([1, 2, 3, 1, 4, 2]) == [1, 4, 2]
    assert get_longest_same_bit_counts([5, 8, 5, 3, 1, 3, 5, 10, 2, 12]) == [3, 5, 10]
    assert get_longest_same_bit_counts([1]) == [1]
    assert get_longest_same_bit_counts([]) == []
    assert get_longest_same_bit_counts([3, 1, 2, 7]) == [1, 2]


"""
Problema 10
"""


def numere_pare(lista):

    for i in range(len(lista)):
        if lista[i] % 2 == 1:
            return False

    return True


def get_longest_all_even(lst: list[int]) -> list[int]:
    subsecventa_maxima = []

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if numere_pare(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventa_maxima):
                subsecventa_maxima = lst[i:j + 1]

    return subsecventa_maxima


def test_get_longest_all_even():
    assert get_longest_all_even([1, 2, 3, 1, 4, 2]) == [4, 2]
    assert get_longest_all_even([5, 8, 5, 3, 8, 6, 10, 2, 12]) == [8, 6, 10, 2, 12]
    assert get_longest_all_even([1]) == []
    assert get_longest_all_even([]) == []
    assert get_longest_all_even([3, 1, 2, 7]) == [2]


def main():
    user_choice = """
    Alegeti:
    1. Determinati cea mai lungă subsecvență cu proprietatea ca numerele sunt patrate perfecte
    
    2. Determinati cea mai lungă subsecvență cu proprietatea
    ca numerele au același număr de biți de 1 în reprezentarea binară
    
    3. Determinati cea mai lungă subsecvență cu proprietatea ca numerele sunt pare
    
    4. Iesire
    """

    a = input(user_choice)

    while a != '4':
        if a == '1':
            test_get_longest_all_perfect_squares()
        elif a == '2':
            test_get_longest_same_bit_counts()
        elif a == '3':
            test_get_longest_all_even()
        a = input(user_choice)


if __name__ == '__main__':
    main()
