from aiohttp import web
import asyncio
from routes import setup_routes


def main():
    app = web.Application()
    setup_routes(app)
    web.run_app(app, host="0.0.0.0", port=8080)

    
if __name__ == "__main__": #create connection with web server
    main()
