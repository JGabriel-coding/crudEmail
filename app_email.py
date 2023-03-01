from playwright.sync_api import Playwright, sync_playwright, expect
import asyncio
from playwright import async_api


async def createemail(name:str,password:str, playwright: Playwright) -> None:
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = context.new_page()
    await page.goto("https://www.weblink.com.br/cpanel-login")
    await page.wait_for_timeout(5000)

    
    await page.locator("input[name=\"email\"]").fill("seuEmailDoPipeRun")
    await page.locator("input[name=\"password\"]").fill("suaSenha")
    await page.locator("input[name=\"password\"]").press("Enter")
    await page.locator("#hpanel_tracking-home-manage_button").click()
    x = "referencia"
    if x == "referencia":
        await page.locator('#hpanel_tracking-home-manage_button').nth(0).click()
    else:
        await page.locator('#hpanel_tracking-home-manage_button').nth(1).click()
    
    await page.wait_for_timeout(2500)
    await page.locator("#hpanel_tracking_emails_add-account > div").nth(0).click()
    await page.wait_for_timeout(2500)
    await page.locator("#email-onboarding-email-account-name > div.field-holder > div > div.field__input > div > input[type=text]").fill(name)
    await page.locator("#email-onboarding-email-account-password > div.field-holder > div.field > div.field__input.field__input--icon-right > div > input[type=password]").fill(password)
    await page.locator("#hpanel_tracking-email-create-account-create_button").nth(0).click()
    await page.wait_for_timeout(2500)
    await page.locator("#hpanel_tracking-email-configure-account-complete_button").click()
    
    context.close()
    browser.close()
    
async def main(): 
   async with sync_playwright() as playwright:
        name = "UserAD"
        password = "Senha_Gerada"
        await createemail(name, password, playwright)
