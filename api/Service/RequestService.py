import requests


class RequestService:

    @staticmethod
    def executeRequest(method, url, headers, payload):
        http_response = None
        try:
            http_response = requests.request(
                "GET", url, headers=headers, data=payload)
            pass
        except Exception as e:
            print("Error during http request to " + url)
            raise e

        return http_response.json()
