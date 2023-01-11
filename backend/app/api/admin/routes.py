from aiohttp.web import Application

from . import views

def setup_api_routes(application: Application):
    application.router.add_post('/api/v1/item', views.public_authorize_admin)