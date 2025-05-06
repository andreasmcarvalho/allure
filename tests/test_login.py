from pages.login_page import LoginPage

def test_login_com_sucesso(driver):
    login = LoginPage(driver)
    login.fazer_login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_login_com_erro(driver):
    login = LoginPage(driver)
    login.fazer_login("usuario_invalido", "senha_errada")
    assert "Epic sadface" in driver.page_source
