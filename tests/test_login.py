import pytest
from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login.get_success_message()

def test_invalid_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login("tomsmith", "wrongpassword")
    assert "Your password is invalid!" in login.get_error_message()

def test_invalid_username(page):
    login = LoginPage(page)
    login.navigate()
    login.login("wronguser", "SuperSecretPassword!")
    assert "Your username is invalid!" in login.get_error_message()

def test_empty_credentials(page):
    login = LoginPage(page)
    login.navigate()
    login.login("", "")
    assert "Your username is invalid!" in login.get_error_message()