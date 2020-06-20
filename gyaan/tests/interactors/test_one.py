def my_func():
    return 2

def test_mything(snapshot):
    return_value = my_func()
    assert return_value == 2
    snapshot.assert_match(return_value, 'gpg_reponse')