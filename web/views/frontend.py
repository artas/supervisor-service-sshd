from service.service import Service
from aiohttp_jinja2 import template
from service import check_service


@template('index.html')
async def index(request):
    service = Service()

    if request.method == 'POST' and request.path == '/start_service':
        service.service_start()
    elif request.method == 'POST' and request.path == '/stop_service':
        service.service_stop()
    elif request.method == 'POST' and request.path == '/restart_service':
        service.service_restart()
    elif request.method == 'POST' and request.path == '/checkbox_status_off':
        check_service.save_status(False)
    elif request.method == 'POST' and request.path == '/checkbox_status_on':
        check_service.save_status(True)

    status_checkbox = check_service.get_status_chekbox()
    stat = service.get_status()

    return {"satus": stat, "status_checkbox": status_checkbox}
