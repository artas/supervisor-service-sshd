from .views import frontend


def setup_rotes(app):
    app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('POST', '/start_service', frontend.index)
    app.router.add_route('POST', '/stop_service', frontend.index)
    app.router.add_route('POST', '/restart_service', frontend.index)
    app.router.add_route('POST', '/checkbox_status_on', frontend.index)
    app.router.add_route('POST', '/checkbox_status_off', frontend.index)
