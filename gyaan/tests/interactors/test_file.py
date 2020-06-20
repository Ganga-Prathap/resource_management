def add_two_numbers(number1, number2):
    sum = number1 + number2
    return sum

def test_add_two_number(snapshot):

    return_value = add_two_numbers(1, 2)

    snapshot.assert_match(return_value, 'gpg_reponse')