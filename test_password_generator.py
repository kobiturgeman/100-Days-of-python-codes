from password_generator import generate_password

def test_password_length():
    password = generate_password(4, 2, 3)
    assert len(password) == 4 + 2 + 3
