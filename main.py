#!/usr/bin/env python3

import uvicorn
import fastapi

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {'sup':'m8'}

@app.get('/echo/{echo}')
def echo_test(echo: str):
    return {'echo':echo}

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
