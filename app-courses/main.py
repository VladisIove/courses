from gino import Gino 
from aiohttp import web
from routes import setup_routes
from migration import migration

db = Gino()
migration("localhost", "courses", "courses", "courses")
app = web.Application(middlewares=[db])
app['config'] = {'dsn': 'postgresql://courses:courses@localhost:5432/courses'} #postgresql://username:password@host:port/database
setup_routes(app)
web.run_app(app)