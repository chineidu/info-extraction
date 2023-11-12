from api.v1.routes.health import root_router
from api.v1.routes.predict import pred_router

__all__: list[str] = ["pred_router", "root_router"]
