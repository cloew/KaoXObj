
def xobj_getattr(obj, attrName, *args):
    """ Return the value for the attr given following any .attrs """
    checkExists = len(args) > 0
    value = obj
    attrs = attrName.split('.')
    for attr in attrs:
        if not checkExists or hasattr(value, attr):
            value = getattr(value, attr)
        else:
            return args[0]
    return value
    
def xobj_attrgetter(attrName):
    """ Return the value for the attr given following any .attrs """
    def getValue(obj, *args):
        return xobj_getattr(obj, attrName, *args)
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