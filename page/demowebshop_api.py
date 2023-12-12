import json
import logging
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser

WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


class DemoWebshopAPI:

    @staticmethod
    @step('API Request')
    def api_request_post(url, **kwargs):
        result = requests.post(url=API_URL + url, **kwargs)
        DemoWebshopAPI.attach_request_info(result)

        return result

    @staticmethod
    @step('Attach Request Info')
    def attach_request_info(result):
        allure.attach(result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
        allure.attach(json.dumps(result.request.body, indent=4, ensure_ascii=True),
                      name="Request body", attachment_type=AttachmentType.JSON, extension="json")
        allure.attach(json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name="Response", attachment_type=AttachmentType.JSON, extension="json")

        logging.info(f'Request: {result.request.url}')
        logging.info(f'INFO Request body: {result.request.body}')
        logging.info(f'Request headers:  {result.request.headers}')
        logging.info(f'Response code: {result.status_code}')
        logging.info(f'Response: {result.text}')

    @staticmethod
    @step('Cookie from API')
    def get_and_set_cookie(response):
        with step('Get cookie from API'):
            cookie = response.cookies.get('Nop.customer')

        with step('Set cookie from API'):
            browser.open('/')
            browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
