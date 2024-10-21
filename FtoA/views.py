from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from .models import selectionCount



def survey(request):
    context = {
        'startNode': 'F',
        'endNode': 'A',
        'nextUrl': 'F-B',
    }
    return render(request, 'final.html', context)


def increaseSelectValue(request, name):
    if request.method == 'POST':
        # key에 해당하는 변수가 없으면 생성하고, 있으면 가져옴
        value, created = selectionCount.objects.get_or_create(name=name)

        # 값 1 증가시키기
        value.value += 1
        value.save()
        
        # 다음으로 이동할 url
        redirect_url = reverse('FtoB:F_B')

        return JsonResponse({'success': True, 'redirectUrl': redirect_url, 'name': name, 'newValue': value.value})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})