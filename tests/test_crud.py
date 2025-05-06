from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_adicionar_e_remover_item(driver):
    LoginPage(driver).fazer_login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    inventory.adicionar_item_ao_carrinho()
    inventory.ir_para_o_carrinho()

    assert cart.item_esta_no_carrinho()
    cart.remover_item()
