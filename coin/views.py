from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View


class CoinView(View):
    template_name = 'coin/coin.html'
    def get(self, request):
        balance = request.user.balance.amount

        return render(request, self.template_name,
                      {"balance": balance,})
