from aiohttp.web import Application

from . import views

def setup_api_routes(application: Application):
    application.router.add_post('/api/v1/item', views.public_proceed_item)
    application.router.add_post('/api/v1/send_message', views.public_send_message)