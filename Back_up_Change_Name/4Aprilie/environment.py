from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
# setez o instanta a browserului

def after_all(context):
    context.browser.quit()