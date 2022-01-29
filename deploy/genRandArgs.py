import random
from deploy.utils import str_to_felt, MAX_LEN_FELT

# Separating array values
SEP = {
    'NILE': ' ',
    'VOYAGER': ', '
}


def get_random_felt_array_string(length=100, range_min=1, range_max=4, dest='VOYAGER'):
    values = get_values_array(length, range_min, range_max)
    return get_string_from_felt_array(values, dest=dest)


def get_random_supplies(number, decimals=18, dest='VOYAGER'):
    values = [
        value * 10**(decimals+exp)
        for value, exp
        in zip(get_values_array(number, 1, 100),
               get_values_array(number, 1, 3))
    ]
    return get_string_from_felt_array(values, dest=dest)


def get_random_symbols(number, character_length, dest='VOYAGER'):
    if character_length > MAX_LEN_FELT:
        raise NotImplementedError(f'Strings must be <= {MAX_LEN_FELT} characters')
    strings = [
        ''.join([chr(value) for value in get_values_array(character_length, 65, 90)])
        for _ in range(number)
    ]
    array = [str_to_felt(string) for string in strings]
    return get_string_from_felt_array(array, dest=dest)


def get_values_array(length=100, range_min=1, range_max=4):
    return [random.randint(range_min, range_max) for _ in range(length)]


def get_string_from_felt_array(array, dest='VOYAGER'):
    return f'{len(array)} ' + SEP[dest].join(str(value) for value in array)


if __name__ == '__main__':
    print(get_random_felt_array_string(100))
