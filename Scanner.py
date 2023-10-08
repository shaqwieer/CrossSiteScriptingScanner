import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from urllib.request import Request, urlopen


def get_forms(url):
    html = bs(requests.get(url).content, "html.parser")
    forms = html.find_all("form")
    result = {
                "url" : url,
                "forms": forms
            }
    return result


def xss(url,form,script):
    data ={}
    target_url = urljoin(url, form.attrs.get("action").lower())
    for input in form.find_all("input"):
        if input.attrs.get("name") and (input.attrs.get("type","text") == "text" or input.attrs.get("type","text") == "search"):
            data[input.attrs.get("name")]=script
    if form.attrs.get("method","get").lower()== "post":
        result = requests.post(target_url, data=data)
    else:
        result = requests.get(target_url, params=data)
    if script in result.content.decode():
        return script
    else:
        return False


def check_sqli_error(response):
    errors = {
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        # if you find one of these errors, return True
        if error in response.content.decode().lower():
            return True
    # no error detected
    return False


def sqli_url(url):
    for c in "\"'":
        new_url = f"{url}{c}"
        if check_sqli_error(requests.get(new_url)):
            return True


def sqli_forms(url,form):
    data = {}
    target_url = urljoin(url, form.attrs.get("action").lower())
    for c in "\"'":    
        for input in form.find_all("input"):
            if input.attrs.get("value") and (input.attrs.get("type","text") == "hidden" ):
                data[input.attrs.get("name")]=input.attrs.get("value") + c
            elif input.attrs.get("type") == "submit":
                data[input.attrs.get("name")]=f"test{c}"
        if form.attrs.get("method","get").lower()== "post":
            result = requests.post(target_url, data=data)
        else:
            result = requests.get(target_url, params=data)
        if check_sqli_error(result):
            return True
    



    