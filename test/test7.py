
from django.conf import settings
settings.configure()

from django import template
t=template.Template(r'my name is {{name}}')
c=template.Context({r'name':r'haozi'})
print(t.render(c))