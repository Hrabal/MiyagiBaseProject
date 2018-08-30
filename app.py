from vibora.blueprints import Blueprint
from vibora.responses import JsonResponse

from Miyagi.config import Config

frontend = Blueprint()


@frontend.route("/test", methods=['GET'])
async def home(config: Config):
    print(config)
    return JsonResponse({'1': 2})
