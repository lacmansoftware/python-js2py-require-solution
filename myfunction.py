__all__ = ['myfunction']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
from numar import numar
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['numar', 'myfunction'])
@Js
def PyJsHoisted_myfunction_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['b'])
    var.put('b', var.get('numar')())
    return var.get('b')
PyJsHoisted_myfunction_.func_name = 'myfunction'
var.put('myfunction', PyJsHoisted_myfunction_)
var.put('numar', numar.numar)
pass
pass


# Add lib to the module scope
myfunction = var.to_python()