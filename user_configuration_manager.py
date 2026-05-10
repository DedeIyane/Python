test_settings = {'theme' : 'dark','notification' : 'enabled','volume' : 'high'}
def add_setting(settings, new_settings):
    key,value = new_settings
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else:
        settings[key] = value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'
    return add_setting

def update_setting(settings, new_settings):
    key,value = new_settings
    key = key.lower()
    value = value.lower()
    if key in settings.keys():
        settings[key] = value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(settings, key):
    new_key= key.lower()
    if new_key in settings.keys():
        del settings[new_key]
        return f'Setting \'{new_key}\' deleted successfully!'
    else:
        return 'Setting not found!'

def view_settings(settings):
    if not settings:
        return 'No settings available.'
    
    result = 'Current User Settings:\n'
    
    for key, value in settings.items():
        result += f'{key.capitalize()}: {value}\n'
    
    return result