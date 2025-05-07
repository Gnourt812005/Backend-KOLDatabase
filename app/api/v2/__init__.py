from fastapi import APIRouter, Depends 
from pathlib import Path
import importlib
import pkgutil

router_v2 = APIRouter()

package_dir = Path(__file__).resolve().parent / "endpoints"
for _, module_name, _ in pkgutil.iter_modules([str(package_dir)]):
    module = importlib.import_module(f"app.api.v2.endpoints.{module_name}")
    if hasattr(module, "router"):
        router_v2.include_router(module.router ,tags=[module_name])