from aiohttp import web

from .errors import DosntFoundQueryset, DosntValidId, DosntValidParameters

class AllView(web.View):
    model = None 

    async def get(self,):
        data = await self.request.query()
        queryset = await self.model.query.gino.filter_by(**data) if len(data) else await self.model.query.gino.all()
        data = []
        for q in queryset:
            data.append({key: value for (key, value) in vars(queryset).items if not key.startswith('_')})
        return web.json_response({'data': data})

class CreateView(web.View):
    model = None

    async def post(self,):
        data = await self.request.post() 
        try:
            queryset = await self.model.create(**data)
            return web.json_response({key: value for (key, value) in vars(queryset).items if not key.startswith('_')})
        except:
            return web.json_response('error_state': DosntValidParameters.error_state, 'description': DosntValidParameters.description)

class RemoveView(web.View):
    model = None 

    async def post(self, request):
        id_queryset = request.match_info.get('id', None)
        if id_queryset:
            try:
                queryset = await self.model.delete.where(self.model.id.is_(id_queryset))
                return web.json_response({key: value for (key, value) in vars(queryset).items if not key.startswith('_')})
            except self.model.DoesNotExist:
                return web.json_response({'error_state': DosntFoundQueryset.error_state, 'description': DosntFoundQueryset.description })
        else:
            return web.json_response({'error_state': DosntValidParameters.error_state, 'description': DosntValidParameters.description})


class EditeView(web.View):
    model = None 

    async def post(self,):
        id_queryset = request.match_info.get('id', None)
        if id_queryset:
            try:
                data = await self.request.post()
                queryset = await self.model.update.values(**data).where(self.model.id.is_(id_queryset))
                return web.json_response({key: value for (key, value) in vars(queryset).items if not key.startswith('_')})
            except self.model.DoesNotExist:
                return web.json_response({'error_state': DosntFoundQueryset.error_state, 'description': DosntFoundQueryset.description })
        else:
            return web.json_response({'error_state': DosntValidParameters.error_state, 'description': DosntValidParameters.description})
