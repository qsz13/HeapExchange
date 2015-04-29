from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, View
from coin.models import Transfer


def deletetransaction(request):
    selected_transaction = Transfer.objects.get(pk=request.POST["transaction_id"])
    page_type = request.POST["transaction_type"]
    selected_transaction.delete()
    balance = request.user.balance.amount
    transactions = Transfer.objects.filter(Q(from_user=request.user) | Q(to_user=request.user))
    transaction_count = transactions.count()
    if page_type == "transaction_history":
        return render(request, 'coin/transaction_history.html', {"page_title": "transaction history",
                                                                 "balance": balance,
                                                                 "transaction_count": transaction_count,
                                                                 "transactions": transactions})
    elif page_type == "output_transaction":
        return render(request, 'coin/output_transaction.html', {"page_title": "output transaction",
                                                                "balance": balance,
                                                                "transaction_count": transaction_count,
                                                                "transactions": transactions})
    elif page_type == "input_transaction":
        return render(request, 'coin/input_transaction.html', {"page_title": "input transaction",
                                                               "balance": balance,
                                                               "transaction_count": transaction_count,
                                                               "transactions": transactions })







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
