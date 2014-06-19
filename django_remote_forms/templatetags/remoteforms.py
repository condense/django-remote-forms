import json
from django import template
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.functional import Promise
from django.utils.encoding import force_text

from django_remote_forms.forms import RemoteForm


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


register = template.Library()

@register.simple_tag
def remoteform(form):
    if form is not None:
        remote_form = RemoteForm(form)
        return json.dumps(remote_form.as_dict(), cls=LazyEncoder, indent=4)

