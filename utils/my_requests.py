import os

import allure
import requests

from utils.logger import Logger

from environment import ENV_OBJECT 


class MyRequests:
    @staticmethod
    def get(
        url: str,
        data: dict = None,
        headers: dict = None,
        cookies: dict = None
    ):
        with allure.step(f'GET request to URL "{url}"'):
            return MyRequests._send(url, data, headers, cookies, 'get')

    @staticmethod
    def post(
        url: str,
        data: dict = None,
        headers: dict = None,
        cookies: dict = None
    ):
        with allure.step(f'POST request to URL "{url}"'):
            return MyRequests._send(url, data, headers, cookies, 'post')

    @staticmethod
    def put(
        url: str,
        data: dict = None,
        headers: dict = None,
        cookies: dict = None
    ):
        with allure.step(f'PUT request to URL "{url}"'):
            return MyRequests._send(url, data, headers, cookies, 'put')

    @staticmethod
    def delete(
        url: str,
        data: dict = None,
        headers: dict = None,
        cookies: dict = None
    ):
        with allure.step(f'DELETE request to URL "{url}"'):
            return MyRequests._send(url, data, headers, cookies, 'delete')

    @staticmethod
    def _send(
            url: str,
            data: dict,
            headers: dict,
            cookies: dict,
            http_method: str
    ):
        url = ENV_OBJECT.get_base_url() + url

        headers = headers or {}
        cookies = cookies or {}

        Logger.add_request(url, data, headers, cookies, http_method)

        if http_method == 'get':
            response = requests.get(
                url=url,
                params=data,
                headers=headers,
                cookies=cookies
            )
        else:
            try:
                response = getattr(requests, http_method)(
                    url=url,
                    data=data,
                    headers=headers,
                    cookies=cookies
                )

            except:
                raise Exception(
                    f'Bad HTTP method "{http_method}" was received')

        Logger.add_response(response)
        return response
