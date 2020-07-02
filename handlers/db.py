from aiohttp import web
import asyncio 
import aioredis
import json

CURRENCIES = dict() #empty dictionary
ZERO = "0" #constant with ZERO value 

async def insert_record(request, CURRENCIES=dict()): #coroutine for inserting data to database
    redis = await aioredis.create_redis_pool("redis://db") #connect wit redis

    merge_param = request.query["merge"] #get merge param 0 or 1
        
    try: #code if json body request is not empty
        data = await request.json() #put json response data
        if merge_param != ZERO: #if merge param is 1...
            for key, value in dict(data).items(): #iterate data dictionary and set values from jsoon to database
                CURRENCIES[key] = value #add new element to dictionary
                await redis.set(str(key), data.get(key)) #set values from jsoon to database
        else: #if merge param is 0...
            for key, value in dict(CURRENCIES).items(): #iterate CURRENCIES dictionary
                await redis.set(str(key), ZERO) #set new ZERO data to redis database
            for key, value in dict(data).items(): #iterate data dictionary and set values from jsoon to database...
                await redis.set(str(key), data.get(key))
    except Exception as e: #code if json body request is empty...
        if merge_param == ZERO:
            for key, value in dict(CURRENCIES).items():
                CURRENCIES[key] = ZERO
                await redis.set(str(key), CURRENCIES[key])

    redis.close()
    await redis.wait_closed()
    return web.Response(text="Data successfully added!", status=200)



