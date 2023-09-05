from playwright.sync_api import sync_playwright


def before_scenario(context, _):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False, slow_mo=500
    )
    context.page = context.browser.new_page()


def after_scenario(context, _):
    context.browser.close()
    context.playwright.stop()