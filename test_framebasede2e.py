import json
import time

import pytest
from playwright.sync_api import Playwright

from page_object.OrderHistroy import OrderHistory
from page_object.Dashboard import Dashboard
from page_object.LoginPage import LoginPage
from Util2.APIUtil2 import API_Util2

with open('data/credentials.json') as f:
    test_data = json.load(f)
    user_cred_list = test_data['user_credentials']

@pytest.mark.parametrize('user_cred',user_cred_list)

def test_hybrid(playwright: Playwright,user_cred,browserInstance):
   # brow = playwright.chromium.launch(headless=False)
   # context = brow.new_context()
   # page = context.new_page()

    #Create Order
    test_API_Util2 = API_Util2()
    getID = test_API_Util2.CreateOrder(playwright,user_cred)

    #login into the application
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()

    loginPage.logged(user_cred["userEmail"],user_cred["userPassword"])


    #Goto Order History and check the order ID
   # print(getID)
    dash = Dashboard(browserInstance)
    dash.dashboard()

# Order History Page
    hist = OrderHistory(browserInstance)
    hist.history(getID)
    page = browserInstance
    result = page.locator(".tagline").text_content()
    assert result == "Thank you for Shopping With Us"
    time.sleep(5)
   # context.close()
   # brow.close()

















