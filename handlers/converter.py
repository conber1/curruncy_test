from aiohttp import web
import asyncio 
import aioredis

async def convert_data(request): #coroutine for converting data
    redis = await aioredis.create_redis_pool("redis://db") #connect with redis
    from_ = request.query["from"] #get from parametr
    to = request.query["to"] #get to parametr
    amount = request.query["amount"] #get amount parametr
    try: #if from and to param is not None ...
        from_ = await redis.get(f"{from_}", encoding="utf-8") #get element from redis database by from_ KEY
        to = await redis.get(f"{to}", encoding="utf-8") #get element from redis database by to KEY
        return web.json_response(dict(result=round((float(from_) / float(to)) * int(amount)))) #return result of converting
    except Exception as e: #if from or to parametr is None...
        return web.json_response(dict(result=None)) #return json with None response

