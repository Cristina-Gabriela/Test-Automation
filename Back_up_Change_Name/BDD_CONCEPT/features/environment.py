from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    print("Hello in this program")


def after_all(context):
    print("Goodbye !")


def before_all(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.quit()


def after_all(context):
    print("Driver all")


def before_all(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())


def after_all(context):
    context.browser.quit()

    