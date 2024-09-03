# Na hora de criar arquivos testes comecar por test_ para poder ser reconhecido como teste pelo pytest

import pytest
from playwright.sync_api import Playwright, Page, expect


class testSuite():
    @pytest.fixture(autouse=True)
    def setup(self, playwright: Playwright)test_primeiro_teste(pw: Playwright):
        browser = pw.chromium.launch(headless=False)
        contexto = browser.new_context()
        page = contexto.new_page()
        base_url = "https://automationexercise.com"
        page.goto(base_url) # O parametro do goto(metodo do playwright) será a base_url

        elemento_login = page.locator(".login-form h2") # o locator localiza partes da pagina

        expect(elemento_login).to_have_text("Login to your account")
