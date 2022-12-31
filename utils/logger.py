import os
from datetime import datetime as dt

from requests import Response


class Logger:
    file_name = 'logs/log_' + dt.now().strftime('%m-%d-%Y_%H-%M-%S') + '.log'

    @classmethod
    def _write_log_to_file(cls, data: str):
        with (open(cls.file_name, 'a', encoding='utf-8')) as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(
        cls, url: str, 
        data: dict, 
        headers:dict, 
        cookies: dict, 
        http_method: str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')
        time = str(dt.now())

        data_to_add = f'\n------\n'
        data_to_add += f'Test: {testname}\n'
        data_to_add += f'Time: {time}\n'
        data_to_add += f'Request http_method: {http_method}\n'
        data_to_add += f'Request URL: {url}\n'
        data_to_add += f'Request data: {data}\n'
        data_to_add += f'Request headers: {headers}\n'
        data_to_add += f'Request cookies: {cookies}\n'
        data_to_add += '\n'

        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        headers_as_dict = dict(response.headers)
        cookies_as_dict = dict(response.cookies)

        data_to_add = f'Response code: {response.status_code}\n'
        data_to_add += f'Response text: {response.text}\n'
        data_to_add += f'Response headers: {headers_as_dict}\n'
        data_to_add += f'Response cookies: {cookies_as_dict}\n'
        data_to_add += f'------\n'

        cls._write_log_to_file(data_to_add)
