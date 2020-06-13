from aiohttp import web 
from .views import AllFAQView, CreateFAQView, EditeFAQView, RemoveFAQView

urlpatterns = [
    web.post('/faqs', AllFAQView, name='all_faq'),
    web.post('/faqs/create', CreateFAQView, name='create_faq'),
    web.post('/faqs/edit', EditeFAQView, name='edit_faq'),
    web.post('/faqs/remove', RemoveFAQView, name='remove_faq'),
]