from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal, getcontext
import math
from mpmath import mp
import sys
from django.views.decorators.csrf import csrf_exempt
sys.set_int_max_str_digits(0)
getcontext().prec = 999999999
mp.dps = 999999999
# Create your views here.
def calculate_result(expression):
    try:
        expression = expression.replace('math.factorial', 'math.factorial')
        result = Decimal(eval(expression))
        return str(result)
    except Exception as e:
        return "Error"
@csrf_exempt
def index(request):
    result = None

    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        result = calculate_result(expression)
    return render(request, 'index.html', {'result': result})