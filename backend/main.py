import argparse

import aiohttp_cors
from aiohttp import web
from aiohttp_jwt import JWTMiddleware

from data.config import DATABASE_URL, SECRET_KEY 


parser = argparse.ArgumentParser()
parser.add_argument('--host')
parser.add_argument('--port')


def setup_routes(application):
    from app.api.admin.routes import setup_api_routes
    setup_api_routes(application)
    setup_cors(application)

def setup_database(application):
    db.init_app(application, dict(dsn=DATABASE_URL))

def setup_app(application):
    # setup_database(application)
    setup_routes(application)

def setup_cors(application: web.Application):
    cors = aiohttp_cors.setup(application, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers='*',
                allow_headers='*'
            ),
        })
    for route in list(application.router.routes()):
        cors.add(route)



if __name__ == '__main__':
    from database.connection import db
    args = parser.parse_args()
    # app = web.Application(middlewares=[db, JWTMiddleware(
    #         SECRET_KEY, algorithms='HS256',
    #         whitelist=[r"/public*"],
    #         credentials_required=False,
    #         )
    #     ]
    # )
    app = web.Application(middlewares=[JWTMiddleware(
            SECRET_KEY, algorithms='HS256',
            whitelist=[r"/public*"],
            credentials_required=False,
            )
        ]
    )
    setup_app(app)
    web.run_app(app, host=args.host, port=args.port)
