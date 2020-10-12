# uvicorn server:app --host 0.0.0.0 --port 8000 --reload

import os
import time
import socket
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

THIS_DIR = os.path.dirname(__file__)
PUBLIC_DIR = os.path.join(THIS_DIR, 'public')
FILE_DIR = os.path.join(PUBLIC_DIR, 'files')
app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse("index.html")

def calc_size(n):
    i, ext = 0, ' KMGTP'
    while n > 1024:
        n /= 1024
        i += 1
    return f"{n:0.2f} {ext[i]}b"

@app.get("/files/")
async def get_files():
    files = []
    for f in os.listdir(FILE_DIR):
        stats = os.stat(os.path.join(FILE_DIR, f))
        files.append({
            "file": f,
            "url": "/files/" + f,
            "size": calc_size(stats.st_size),
            "date": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
        })
    return files

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    filepath = os.path.join(FILE_DIR, file.filename)
    if os.path.isfile(filepath):
        os.remove(filepath)
    with open(filepath, 'ab') as f:
        for chunk in iter(lambda: file.file.read(10000), b''):
            f.write(chunk)
    return {"filename": file.filename}

app.mount("/", StaticFiles(directory=PUBLIC_DIR), name="public")

@app.on_event("startup")
async def startup_event():
    os.makedirs(FILE_DIR, exist_ok=True)
    ip = socket.gethostbyname(socket.gethostname())
    print('[Visit url]', f'http://{ip}:8000')
