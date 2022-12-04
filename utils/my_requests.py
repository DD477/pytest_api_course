import requests


class MyRequests:
    @staticmethod
    def get(
        url: str,
        data: dict = None,
        headers: dict = None,
        cookies: dict = None
    ):
        return MyRequests._send(url, data, headers, cookies, 'get')

    @staticmethod
    def post(
        url: str,
        data: dict = None,
        headers: dict = None,
        cookies: dict = None
    ):
        return MyRequests._send(url, data, headers, cookies, 'post')

    @staticmethod
    def put(
        url: str,
        data: dict = None,
        headers: dict = None,
        cookies: dict = None
    ):
        return MyRequests._send(url, data, headers, cookies, 'put')

    @staticmethod
    def delete(
        url: str,
        data: dict = None,
        headers: dict = None,
        cookies: dict = None
    ):
        return MyRequests._send(url, data, headers, cookies, 'delete')

    @staticmethod
    def _send(
            url: str,
            data: dict,
            headers: dict,
            cookies: dict,
            http_method: str
    ):
        url = f'https://playground.learnqa.ru/api/{url}'

        headers = headers or {}
        cookies = cookies or {}

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

        return response
