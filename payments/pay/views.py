
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        client = razorpay.Client(
            auth=("rzp_test_7fI3qA1r1esYgj", "5O0PBDUszcp6F1UEJYY36cZY"))
        payment = client.order.create({'amount': amount, 
                                       'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

def mid(request):
    return render(request, "mid.html")

@csrf_exempt
def success(request):
    return render(request, "success.html")