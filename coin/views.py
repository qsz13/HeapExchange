from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View
from coin.models import Transfer


class CoinView(View):
    template_name = 'coin/coin.html'
    def get(self, request):
        balance = request.user.balance.amount
        transfers = Transfer.objects.filter(Q(from_user=request.user)|Q(to_user=request.user))
        return render(request, self.template_name,
                      {"balance": balance,"transfers":transfers})
