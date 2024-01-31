from django.shortcuts import render

# Create your views here.
def go_display_hello(request):
    return render(request, 'display_hello.html')