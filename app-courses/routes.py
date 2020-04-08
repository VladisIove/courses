

def setup_routes(app):
    '''
        app.router.add_get('name_something/', NameSomethingView, name='all_name_something')
        app.router.add_post('name_something/create/', NameSomethingCreate, name='new_name_something')
        app.router.add_post('name_somethind/<int:id>/', UpdateSomething, name='update_name_something')
        app.router.add_post('name_something/<int:id>/remove', RemoveNameSomething, name='remove_name_something')
    '''
