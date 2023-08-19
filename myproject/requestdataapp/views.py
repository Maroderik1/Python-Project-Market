from django.shortcuts import render

def process_get_view(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context = {
       "a": a,
       "b": b,
       "result": result
    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)