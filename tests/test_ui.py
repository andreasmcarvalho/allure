from pages.login_page import LoginPage

def test_titulo_da_pagina(driver):
    login = LoginPage(driver)
    assert "Swag Labs" in driver.title
