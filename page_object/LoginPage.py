class LoginPage :
    def __init__(self,page):
        self.page = page

    def navigate(self):
      self.page.goto("https://rahulshettyacademy.com/client")

    def logged(self,username,pwd):
        self.page.get_by_placeholder("email@example.com").fill(username)
        self.page.get_by_placeholder("enter your passsword").fill(pwd)
        self.page.get_by_role("button", name="Login").click()