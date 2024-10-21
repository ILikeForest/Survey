from django.shortcuts import render


def thank(request):
    return render(request, 'thanks.html')