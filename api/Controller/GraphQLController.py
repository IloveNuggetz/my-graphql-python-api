from .BaseController import BaseController
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify, Blueprint
from api.queries import listPhilosophers_resolver, getPhilosopher_resolver
from api import app


class GraphQLController(BaseController):

    def __init__(self):
        print(self.__hash__())

    bp = Blueprint('graphql', __name__, url_prefix='/graphql')

    query = ObjectType("Query")
    query.set_field("listPhilosophers", listPhilosophers_resolver)
    query.set_field("getPhilosopher", getPhilosopher_resolver)

    type_defs = load_schema_from_path("schema.graphql")
    schema = make_executable_schema(
        type_defs, query, fallback_resolvers
    )

    def get_bp(self):
        print(self.__hash__())
        global bp
        return self.bp
        pass

    @bp.route("", methods=["GET"])
    def graphql_playground():
        return PLAYGROUND_HTML, 200

    @bp.route("", methods=["POST"])
    def graphql_server():
        global schema
        data = request.get_json()
        success, result = graphql_sync(
              GraphQLController.schema,
              data,
              context_value=request,
              debug=app.debug
              )
        status_code = 200 if success else 400
        return jsonify(result), status_code
