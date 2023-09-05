import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://playwright.dev")

        print(await page.title())

        await browser.close()


asyncio.run(main())