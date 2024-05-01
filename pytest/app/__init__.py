import connexion
from connexion.middleware import MiddlewarePosition
from connexion.options import SwaggerUIOptions
from starlette.middleware.cors import CORSMiddleware

from .config import Config as config

def create_app():
    connexion_app = connexion.FlaskApp('__name__')
    flask_app = connexion_app.app

    flask_app.config.from_object(config)

    origins = "*"
    if flask_app.config.get("CORS_ORIGINS") is not None:
        origins = flask_app.config["CORS_ORIGINS"]

    connexion_app.add_middleware(
        CORSMiddleware,
        position=MiddlewarePosition.BEFORE_EXCEPTION,
        allow_origins=[origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    options = SwaggerUIOptions(
        swagger_ui=True,
        swagger_ui_template_arguments={"SwaggerUITitle": {}, "title": "Swagger UI"},
    )
    connexion_app.add_api(
        specification='./app/api-spec.yaml',
        base_path=None,
        swagger_ui_options=options,
        pass_context_arg_name="request",
    )

    return connexion_app

async def healthz_live():
    return {"response": "Healthy"}


async def get_salesforce_client(username, password):
    raise NotImplementedError

async def get_data(key):
    client = await get_salesforce_client(config.SF_USERNAME, config.SF_PASSWORD)
    try:
        result = await client.get_data(key)
    except IOError as e:
        return {"error": str(e)}
    return {"result": result}
