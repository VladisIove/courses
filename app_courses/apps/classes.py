from aiohttp import web
from sqlalchemy.sql import text
from aiohttp.abc import AbstractAccessLogger
import json
import datetime 
from .errors import DosntFoundQueryset, DosntValidId, DosntValidParameters

class MixinClearQueryView(web.View):
    model = None 

    def clear_query(self, q):
        clear_query = {}
        for key, value in q.to_dict().items():
            clear_query[key] = value if type(value) in [int, bool, float, object, dict, list, str, type(None), set, tuple] else str(value)
        return clear_query 
    

class AllView(MixinClearQueryView):

    async def post(self):
        data = await self.request.json()
        if len(data):
            q = self.model.query
            for key, value in data.items():
                q = q.where(getattr(self.model, key) == value)
            queryset = await q.gino.all()
        else :
            queryset = await self.model.query.gino.all()
        data = []
        for query in queryset:
            data.append(self.clear_query(query))
        return web.json_response({'data': data})

class CreateView(MixinClearQueryView):

    async def post(self,):
        data = await self.request.json()
        try:
            queryset = await self.model.create(**data)
            return web.json_response(self.clear_query(queryset))
        except:
            return web.json_response({'error_state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})

class RemoveView(MixinClearQueryView):

    async def post(self):
        id_queryset = await self.request.json()
        if id_queryset:
            try:
                queryset = await self.model.get(id_queryset)
                await queryset.delete()
                return web.json_response(self.clear_query(queryset))
            except self.model.DoesNotExist:
                return web.json_response({'error_state': DosntFoundQueryset.ERROR, 'description': DosntFoundQueryset.DESCRIPTION })
        else:
            return web.json_response({'error_state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})


class EditeView(MixinClearQueryView):

    async def post(self,):
        data = await self.request.json()
        if data.get('id', False):
            try:
                id_queryset = data['id']
                del data['id']
                await self.model.update.values(**data).where(self.model.id == id_queryset).gino.status()                
                queryset = await self.model.get(id_queryset)
                return web.json_response(self.clear_query(queryset))
            except self.model.DoesNotExist:
                return web.json_response({'error_state': DosntFoundQueryset.ERROR, 'description': DosntFoundQueryset.DESCRIPTION })
        else:
            return web.json_response({'error_state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})
