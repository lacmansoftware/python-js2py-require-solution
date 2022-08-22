__all__ = ['numar']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['numar'])
@Js
def PyJsHoisted_numar_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js(1.0)
PyJsHoisted_numar_.func_name = 'numar'
var.put('numar', PyJsHoisted_numar_)
pass
pass


# Add lib to the module scope
numar = var.to_python()