from handlers.converter import *
from handlers.db import *

def setup_routes(app):
    app.router.add_post("/database", insert_record), #adding urls...
    app.router.add_get("/convert", convert_data)