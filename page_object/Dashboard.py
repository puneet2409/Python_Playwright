class Dashboard :
    def __init__(self,page):
        self.page = page

    def dashboard(self):
        self.page.get_by_role("button", name="  ORDERS").click()