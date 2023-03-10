from aiohttp.web import Application

from . import views

def setup_api_routes(application: Application):
    application.router.add_post('/api/v1/items', views.public_proceed_items)
    application.router.add_post('/api/v1/send_message', views.public_send_message)
    application.router.add_post('/api/v1/send_message_own_commission', views.public_proceed_own_commission)