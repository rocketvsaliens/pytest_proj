def get_val(collection, key, default='git'):
    """get value from dictionary by key"""
    if key in collection:
        return collection[key]
    else:
        return default

