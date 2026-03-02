import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def context(request, browser):
    context = browser.new_context()
    tracing_option = request.config.getoption("tracing")
    if tracing_option != "off":
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    if tracing_option != "off":
        context.tracing.stop(path="test-results/trace.zip")
    context.close()

# The above fixture will save the trace for the entire test session. If you want to save a separate trace for each test, you can use the following fixture instead:
# @pytest.fixture
# def context(request, browser):
#     context = browser.new_context()
#     tracing_option = request.config.getoption("tracing")

#     if tracing_option != "off":
#         context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     yield context
#     if tracing_option != "off":
#         # Stop tracing and save to the specific file
#         test_name = request.node.name
#         context.tracing.stop(path=f"test-results/trace-{test_name}.zip")
#     context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()
