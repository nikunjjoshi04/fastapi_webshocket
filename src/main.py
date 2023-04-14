from fastapi import FastAPI
from loguru import logger

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root() -> dict:
    logger.debug("LOG debug")
    logger.info("LOG info")
    logger.warning("LOG warning")
    logger.error("LOG error")
    return {"message": "Hello Nikka...!"}
