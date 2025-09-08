from playwright.sync_api import sync_playwright

def test_response(playwright: sync_playwright()):
    context = playwright.request.new_context()
    response = context.get("")