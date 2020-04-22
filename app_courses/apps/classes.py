from aiohttp import web
from sqlalchemy.sql import text
import json
from .errors import DosntFoundQueryset, DosntValidId, DosntValidParameters

class AllView(web.View):
    model = None 

    async def post(self):
        data = await self.request.json()
        #data = {getattr(self.model,key): value for key, value in data.items()}
        data = {getattr(self.model, key): value for key, value in data.items()}
        queryset = await self.model.query.where(**data).gino.all() if len(data) else await self.model.query.gino.all()
        data = []
        for q in queryset:
            data.append(q.to_dict())
        return web.json_response({'data': data})

class CreateView(web.View):
    model = None

    async def post(self,):
        data = await self.request.json()
        try:
            queryset = await self.model.create(**data)
            return web.json_response(queryset.to_dict())
        except:
            return web.json_response({'error_state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})

class RemoveView(web.View):
    model = None 

    async def post(self):
        id_queryset = await self.request.json()
        if id_queryset:
            try:
                queryset = await self.model.get(id_queryset)
                data_json = queryset.to_dict()
                await queryset.delete()
                return web.json_response(data_json)
            except self.model.DoesNotExist:
                return web.json_response({'error_state': DosntFoundQueryset.ERROR, 'description': DosntFoundQueryset.DESCRIPTION })
        else:
            return web.json_response({'error_state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})


class EditeView(web.View):
    model = None 

    async def post(self,):
        data = await self.request.json()
        if data.get('id', False):
            try:
                id_queryset = data['id']
                del data['id']
                await self.model.update.values(**data).where(self.model.id == id_queryset).gino.status()                
                queryset = await self.model.get(id_queryset)
                return web.json_response(queryset.to_dict())
            except self.model.DoesNotExist:
                return web.json_response({'error_state': DosntFoundQueryset.ERROR, 'description': DosntFoundQueryset.DESCRIPTION })
        else:
            return web.json_response({'error_state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})
