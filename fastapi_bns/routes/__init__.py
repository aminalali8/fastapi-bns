from fastapi import APIRouter
import os 

from .content import router as content_router
from .security import router as security_router
from .user import router as user_router

main_router = APIRouter()

main_router.include_router(user_router, prefix="/user", tags=["user"])
main_router.include_router(content_router, prefix="/content", tags=["content"])
main_router.include_router(security_router, tags=["security"])

try: print(os.environ['REGISTRAR_ID'])
except: os.environ['REGISTRAR_ID'] = 'REGISTRAR_ID_GOES_HERE'
    

@main_router.get("/")
async def index():
    return {"message": "Hello World! (From Registrar: " + os.environ['REGISTRAR_ID'] + ")"}
