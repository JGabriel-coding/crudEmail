from playwright.sync_api import Playwright, sync_playwright, expect
from fastapi import FastAPI
from app_email import createemail
app = FastAPI()


@app.get('/')
def root():
        return{"hello":"Wolrd"}

@app.post("/create-email")
async def read_root():
    with sync_playwright() as playwright:
        name = "userdoAD"
        password = "senha_Padrão"
        createemail(name, password, playwright)
    return {'enviar, dados completos da pessoa'}






