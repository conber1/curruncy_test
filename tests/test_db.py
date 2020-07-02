from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import aiohttp
from handlers.db import insert_record
import aioredis
import socket
import asyncio



class TestDB(AioHTTPTestCase):

    async def get_application(self):
        app = aiohttp.web.Application()
        app.router.add_post('/database', insert_record)
        return app

    @unittest_run_loop
    async def test_insert_record(self):
        sem = asyncio.Semaphore(100)
        redis = await aioredis.create_redis_pool("redis://db")
        payload = {"EUR": "60", "USD": "50"}
        params = {'merge': '0'}
        resp = await self.client.request(method="POST", path="/database", params=params, json=payload)
        assert resp.status == 200
        assert await redis.get("USD", encoding="utf-8") == "50"
        assert await redis.get("EUR", encoding="utf-8") == "60"
        redis.close()
        await redis.wait_closed()


    

