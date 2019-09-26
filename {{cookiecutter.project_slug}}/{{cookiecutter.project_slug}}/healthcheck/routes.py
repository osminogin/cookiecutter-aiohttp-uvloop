from .views import PingCheckView


def register_routes(app):
    app.router.add_route('*', '/ping/', PingCheckView)
