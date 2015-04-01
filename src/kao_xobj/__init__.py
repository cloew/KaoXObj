
def xobj_getattr(obj, attrName):
    """ Return the value for the attr given following any .attrs """
    value = obj
    attrs = attrName.split('.')
    for attr in attrs:
        value = getattr(value, attr)
    return value
    
def xobj_attrgetter(attrName):
    """ Return the value for the attr given following any .attrs """
    def getValue(obj):
        return xobj_getattr(obj, attrName)
    return getValue