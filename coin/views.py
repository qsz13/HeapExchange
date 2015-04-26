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


class TransactionView(View):
    template_name = 'coin/transaction_history.html'

    def get(self, request):
        balance = request.user.balance.amount
        transactions = Transfer.objects.filter(Q(from_user=request.user) | Q(to_user=request.user))
        transaction_count = transactions.count()
        return render(request, self.template_name, {"page_title": "transaction history", "balance": balance,
                                                    "transaction_count": transaction_count,
                                                    "transactions": transactions})


class InputTransactionView(View):
    template_name = "coin/input_transaction.html"

    def get(self, request):
        balance = request.user.balance.amount
        transactions = Transfer.objects.filter(Q(to_user=request.user))
        transaction_count = transactions.count()
        return render(request, self.template_name, {"page_title": "input transaction", "balance": balance,
                                                    "transaction_count": transaction_count,
                                                    "transactions": transactions})


class OutputTransactionView(View):
    template_name = "coin/output_transaction.html"

    def get(self, request):
        balance = request.user.balance.amount
        transactions = Transfer.objects.filter(Q(from_user=request.user))
        transaction_count = transactions.count()
        return render(request, self.template_name, {"page_title": "output transaction", "balance": balance,
                                                    "transaction_count": transaction_count,
                                                    "transactions": transactions})
