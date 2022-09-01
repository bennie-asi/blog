from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.http import require_POST

from contact.forms import ContactForm


# Create your views here.
# @require_POST
def contact(request):
    if request.method == 'GET':
        return render(request,'contact/contact.html')
    form = ContactForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        contact = form.save(commit=False)
        contact.save()
        messages.add_message(request, messages.SUCCESS, '留言成功', extra_tags='success')
        return render(request, 'contact/contact.html', context=context)
    messages.add_message(request, messages.ERROR, '留言失败，请修改表单中的错误后重新提交', extra_tags='danger')
    return render(request, 'contact/preview.html', context=context)
