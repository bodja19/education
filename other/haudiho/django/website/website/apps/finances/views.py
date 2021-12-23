from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .models import People, NotMyMoney, MyMoney


def index(request):
    user = User.objects.all()
    return render(request, 'finances/login.html', {'users': user})

def get_money(request):
    user = User.objects.get(username='Bohdan')
    user = People.objects.get(debtor=user.id)
    all_money = MyMoney.objects.filter(money_id=user.id)
    print(all_money)
    return render(request, 'finances/test.html', {'all_money': all_money, 'user': user})

"""class RegisterUser(DataMixin, CreateView):
    
    
    form_class = UserCreationForm
    template_name = 'finances/login.html'
    succes_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(--kwargs)
        c_def = self.get_user_context(title='Реєстріція')
        return dict(list(context.items()) + list(c_def.items()))
"""