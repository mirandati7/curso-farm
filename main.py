from fastapi import FastAPI

from api.v1.api import api_router

API_V1_STR = '/api/v1'

app = FastAPI(title="MVP FARM Product")
app.include_router(api_router, prefix=API_V1_STR)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9000, log_level="info", reload=True)