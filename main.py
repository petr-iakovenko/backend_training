import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from Config.Connection import prisma_connection
from get_crypto import info_binance
from dml_prisma import push_data_db, get_data_db


def init_app():
    app = FastAPI(
        title='ETL for testing',
        description='FastAPI Prisma',
        version='1.0.0'
    )

    @app.on_event('startup')
    async def startup():
        print('Start Server!')
        await prisma_connection.connect()

    @app.on_event('shutdown')
    async def shutdown():
        print('Shutdown Server!')
        await prisma_connection.disconnect()

    # для запросов в теле
    class SPostSymbol(BaseModel):
        symbol: str
        # user_token: str     # for validation

    @app.post('/')
    async def post_symbol(symbol: SPostSymbol):
        data_url = info_binance(symbol)
        await push_data_db(data_url)
        return data_url

    @app.get('/api/info')
    async def get_symbol(symbol):
        data = await get_data_db(symbol)
        return data

    return app


app = init_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8100, reload=True)