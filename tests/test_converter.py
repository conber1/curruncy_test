from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import aiohttp
from handlers.converter import convert_data
import aioredi
import asyncio
import json


class TestConverter(AioHTTPTestCase):

    async def get_application(self):

        app = aiohttp.web.Application()
        app.router.add_get("/convert", convert_data)
        return app

    @unittest_run_loop
    async def test_convert_data(self):
        redis = await aioredis.create_redis_pool("redis://db")
        params = {'from': 'USD', 'to': 'EUR', 'amount': '10'}
        await redis.set("USD", "30")
        await redis.set("EUR", "35")
        resp = await self.client.request(method="GET", path="/convert", params=params)
        foo = await resp.text()
        foo = json.loads(foo)
        assert str(foo.get("result")) == str(9)
        assert resp.status == 200
        redis.close()
        await redis.wait_closed()
