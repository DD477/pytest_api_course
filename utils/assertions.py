from requests import JSONDecodeError, Response


class Assertions:
    @staticmethod
    def assert_response_in_json_format(
        response: Response,
    ):
        try:
            return response.json()
        except JSONDecodeError:
            assert False, (
                f'Response is not in JSON. Response text is "{response.text}"'
            )

    @staticmethod
    def assert_json_by_value(
        response: Response,
        name: str,
        expected_value: str,
        error_message: str
    ):
        response_as_dict = Assertions.assert_response_in_json_format(response)
        assert name in response_as_dict, (
            f'Response does not have a key {name}'
        )
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name: str):
        response_as_dict = Assertions.assert_response_in_json_format(response)
        assert name in response_as_dict, (
            f'Response does not have a key {name}'
        )

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        response_as_dict = Assertions.assert_response_in_json_format(response)
        for name in names:
            assert name in response_as_dict, (
                f'Response does not have a key {name}'
            )

    @staticmethod
    def assert_json_has_not_key(response: Response, name: str):
        response_as_dict = Assertions.assert_response_in_json_format(response)
        assert name not in response_as_dict, (
            f'Response JSON should not have a key {name}. But it is present'
        )

    @staticmethod
    def assert_code_status(response: Response, expected_code_status):
        assert response.status_code == expected_code_status, (
            f'Unexpected status code. Expected: {expected_code_status}. '
            f'Actual: {response.status_code}.'
        )
