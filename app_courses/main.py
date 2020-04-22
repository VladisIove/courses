
from aiohttp import web
from routes import setup_routes
import logging
from migration import migration
from apps.init_db import db 

migration("localhost", "courses", "courses", "courses")
app = web.Application(middlewares=[db])
logging.basicConfig(level=logging.DEBUG)
app['config'] = { "gino":{'dsn': 'postgresql://courses:courses@localhost:5432/courses',
                 'user': 'courses',
                 'password': 'courses',
                 'database': 'courses',
                 'host': 'localhost',
                 'port': 5432} }#postgresql://username:password@host:port/database
db.init_app(app)
setup_routes(app)
web.run_app(app)