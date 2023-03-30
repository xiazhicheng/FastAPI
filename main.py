from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import uvicorn
import traceback
from loguru import logger
import pendulum
app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def main():
    now = pendulum.now().format('YYYY-MM-DD HH:mm:ss')
    return {"message": f"Hello {now}. Welcome to 土豆家!"}


@app.get("/path")
async def demo_get():
    some_file_path = './WechatIMG30149.jpeg'
    return FileResponse(some_file_path)



@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}




if __name__ == '__main__':
    try:
        uvicorn.run(app=app, host="0.0.0.0", port=8096)
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e