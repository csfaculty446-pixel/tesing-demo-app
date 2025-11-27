import re




def add_numbers(a, b):
return a + b




def validate_user(username, password):
# Very simple checks: username min 3 chars, password min 4 chars
if not isinstance(username, str) or not isinstance(password, str):
return False
if len(username) < 3 or len(password) < 4:
return False
# no spaces
if ' ' in username or ' ' in password:
return False
return True