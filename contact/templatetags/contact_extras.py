from django import template

from ..forms import ContactForm
from ..models import Contact

register = template.Library()


@register.inclusion_tag('contact/inclusions/_form.html', takes_context=True)
def show_contact_form(context, form=None):
    if form is None:
        form = ContactForm()
    return {'form': form}


@register.inclusion_tag('contact/inclusions/_list.html',takes_context=True)
def show_contact(context):
    contact_list = Contact.objects.all().order_by('-created_time')
    contact_count = contact_list.count()

    return {
        'contact_count': contact_count,
        'contact_list': contact_list,
    }
