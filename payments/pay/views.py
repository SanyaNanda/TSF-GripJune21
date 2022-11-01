
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.template import Context

global amount
amount=2000

def home(request):
    if request.POST:
        name = request.POST['name']
        amount = request.POST['amount']
        client = razorpay.Client(
            auth=("rzp_test_7fI3qA1r1esYgj", "5O0PBDUszcp6F1UEJYY36cZY"))
        payment = client.order.create({'amount': amount, 
                                       'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

def mid(request):
    context={'amount':amount}
    return render(request, "mid.html",context)

@csrf_exempt
def success(request):
    return render(request, "success.html")