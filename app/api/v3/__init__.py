from fastapi import APIRouter, Depends 
from pathlib import Path
import importlib
import pkgutil

router_v3 = APIRouter()

package_dir = Path(__file__).resolve().parent / "endpoints"
for _, module_name, _ in pkgutil.iter_modules([str(package_dir)]):
    module = importlib.import_module(f"app.api.v3.endpoints.{module_name}")
    if hasattr(module, "router"):
        router_v3.include_router(module.router ,tags=[module_name])