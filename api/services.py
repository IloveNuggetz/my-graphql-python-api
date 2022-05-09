from .models import WikimediaProject
from .exceptions import WikimediaException
import requests
from flask import jsonify
import json


class GameService:
    def get_available_quote_categories():
        return None


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


class WikimediaService:

    def initAvailableProjects():
        # TODO: search for avaialable projects and endpoints automated
        endpoints = {
            "en": "en.wikiquote",
            "de": "de.wikiquote"
        }

        tracked_projects = []
        tracked_projects.append(WikimediaProject("wikiquote", endpoints))

        return tracked_projects

    tracked_projects = initAvailableProjects()

    endpoint_url = "https://wikimedia.org/api/rest_v1"
    path = "/metrics/pageviews/top/{project_id}/all-access/2022/03/all-days"

    def getMostViewedPages(self, language, target_project):
        project = self.tracked_projects[0]
        project_id = project.endpoints.get(language, None)

        request_url = self.endpoint_url + \
            self.path.format(project_id=project_id)

        response = None
        try:
            response = RequestService.executeRequest(
                "GET", "http://192.168.245.2/", {"User-Agent": "simon.1707@gmx.de", "Accept": "application/json"}, None)
            pass
        except Exception as e:
            raise WikimediaException(666, "Fetching most viewed pages failed")

        return response
