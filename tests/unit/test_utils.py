from app.utils import add_numbers, validate_user




def test_add_numbers_basic():
assert add_numbers(2, 3) == 5
assert add_numbers(-1, 1) == 0




def test_validate_user_good():
assert validate_user('alice', 'passw') is True




def test_validate_user_bad():
assert validate_user('a', 'bbb') is False
assert validate_user('bob', 'b') is False
assert validate_user('invalid user', 'password') is False