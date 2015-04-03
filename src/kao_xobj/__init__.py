
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

def xobj_setattr(obj, attrName, value):
    """ Set the value for the attr given following any .attrs """
    attrs = attrName.split('.')
    attrs, finalAttr = attrs[:-1], attrs[-1]
    
    parentObj = obj
    for attr in attrs:
        parentObj = getattr(parentObj, attr)
    setattr(parentObj, finalAttr, value)
    
def xobj_attrsetter(attrName):
    """ Set the value for the attr given following any .attrs """
    def setValue(obj, value):
        return xobj_setattr(obj, attrName, value)
    return setValue