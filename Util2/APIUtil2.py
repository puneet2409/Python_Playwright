from playwright.sync_api import Playwright

orderplayload = {
  "orders": [
    {
      "country": "British Indian Ocean Territory",
      "productOrderedId": "67a8dde5c0d3e6622a297cc8"
    }
  ]
}

class API_Util2:
    def gettoken(self,playwright: Playwright,user_cred):
        val = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = val.post("/api/ecom/auth/login",
                 data={"userEmail": user_cred["userEmail"], "userPassword": user_cred["userPassword"]})
        assert response.ok
        resvale = response.json()
        print(resvale["token"])
        return resvale["token"]

    def CreateOrder(self,playwright: Playwright,user_cred):
        token2 = self.gettoken(playwright,user_cred)
        val = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = val.post("api/ecom/order/create-order",
                            data=orderplayload,
                            headers={
                                        "authorization":token2,
                                        "content-Type":"application/json"
                                     })

        resvalue = response.json()
        return resvalue["orders"][0]