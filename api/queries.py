from .models import Philosopher


def listPhilosophers_resolver(obj, info):
    try:
        philosophers = [philosopher.to_dict()
                        for philosopher in Philosopher.query.all()]
        print(philosophers)
        payload = {
            "success": True,
            "philosophers": philosophers
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def getPhilosopher_resolver(obj, info, wikidataUrl):
    try:
        philosopher = Philosopher.query.get(wikidataUrl)
        print(philosopher.to_dict())
        payload = {
            "success": True,
            "philosopher": philosopher.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Philosopher item matching {wikidataUrl} not found"]
        }
    return payload
