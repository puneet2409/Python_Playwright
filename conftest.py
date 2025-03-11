import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="session")

def user_cred(request):
    return request.param


@pytest.fixture()

def browserInstance(playwright,request):
    browsername = request.config.getoption("browser_name")
    if browsername == "chrome":
        brow = playwright.chromium.launch(headless=False)
    elif browsername == "firefox":
        brow = playwright.firefox.launch(headless=False)
    context = brow.new_context()
    page = context.new_page()
    yield page
    context.close()
    brow.close()
