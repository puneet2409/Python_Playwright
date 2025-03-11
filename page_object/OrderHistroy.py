class OrderHistory:
    def __init__(self, page):
        self.page = page

    def history(self,getID):
        rowpos = self.page.locator("tr").filter(has_text=getID)
        rowpos.get_by_role("button", name="View").click()