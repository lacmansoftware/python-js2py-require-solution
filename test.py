# translate js files to python code first
import js2py

js2py.translate_file('numar.js', 'numar.py')
js2py.translate_file('myfunction.js', 'myfunction.py')



# modify myfunction.py

# import and use
from myfunction import myfunction

print(myfunction.myfunction())
