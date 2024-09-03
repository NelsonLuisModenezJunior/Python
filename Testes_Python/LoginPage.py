class Login:
    def __init__(self, page):
        self.campo_email = ""
        self.campo_senha = ""
        self.botao_login = ""

    def realizar_login(self, email, senha):
        self.page.locator(self.campo_email).fill(email)
        self.page.locator(self.campo_senha).fill(senha)
        self.page.locator(self.botao_login).click()