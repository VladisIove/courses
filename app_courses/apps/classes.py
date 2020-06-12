from aiohttp import web
from sqlalchemy.sql import text
from aiohttp.abc import AbstractAccessLogger
import json
import datetime 
from .errors import DosntFoundQueryset, DosntValidId, DosntValidParameters

class AllView(web.View):
    model = None 

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
        for q in queryset:
            data.append(q.to_dict())
        try:
            return web.json_response({'data': data})
        except:
            data = []
            dict_q = {}
            for q in queryset:
                for key in self.model.key_dict:
                    dict_q[key] = getattr(q, key) if type(getattr(q, key)) not in [type(datetime.datetime.now())] else str(getattr(q, key))
                data.append(dict_q)
            return web.json_response({'data': data})

class CreateView(web.View):
    model = None

    async def post(self,):
        data = await self.request.json()
        try:
            queryset = await self.model.create(**data)
            try:
                return web.json_response(queryset.to_dict())
            except:
                dict_q = {}
                for key in self.model.key_dict:
                    dict_q[key] = getattr(queryset, key) if type(getattr(queryset, key)) not in [type(datetime.datetime.now())] else str(getattr(queryset, key))
                return web.json_response(json.dumps(dict_q))
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
                try:
                    return web.json_response(data_json)
                except:
                    dict_q = {}
                    for key in self.model.key_dict:
                        dict_q[key] = getattr(queryset, key) if type(getattr(queryset, key)) not in [type(datetime.datetime.now())] else str(getattr(queryset, key))
                    return web.json_response(json.dumps(dict_q))
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
                try:
                    return web.json_response(queryset.to_dict())
                except:
                    dict_q = {}
                    for key in self.model.key_dict:
                        dict_q[key] = getattr(queryset, key) if type(getattr(queryset, key)) not in [type(datetime.datetime.now())] else str(getattr(queryset, key))
                    return web.json_response(json.dumps(dict_q))
            except self.model.DoesNotExist:
                return web.json_response({'error_state': DosntFoundQueryset.ERROR, 'description': DosntFoundQueryset.DESCRIPTION })
        else:
            return web.json_response({'error_state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})
