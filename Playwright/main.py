from playwright.sync_api import sync_playwright
import time


def main():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False,
                args=['--start-maximized']
            )

            context = browser.new_context(no_viewport=True)
            page = context.new_page()
            page.goto('https://www.hashtagtreinamentos.com')
            page.locator('xpath=//*[@id="menu-item-30799"]/a').click()
            print('working')
            time.sleep(5)
    except Exception as e:
        print(f'{">"*20} {e} {"<"*20}')


if __name__ == '__main__':
    main()
