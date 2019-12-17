import string

values = {'var': 'foo'}

t = string.Template("""
Variable : $var
Escape   : $$
Variable in text   : ${var}iable
""")

print('template', t.substitute(values))
