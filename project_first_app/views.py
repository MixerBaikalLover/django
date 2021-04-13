from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Owner
import datetime
def index(request):
    return HttpResponse('.i.')

def detail(request, owner_id):
    try: #метод try-except - обработчик исключений
        p = Owner.objects.get(pk=owner_id)  #pk - автоматически создается в джанго для любой таблицы в моделе (оно есть у любого объекта из бд), poll_id будет передан функции при её вызове.
#переменной p присваивается объект, полученный в результате выполнения запроса аналогичного "select * from Poll where pk=poll_id"
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist") #исключение которое будет вызвано, если блок try вернет значение False (не будут найдены записи в таблице Poll)
    return render(request, 'detail.html', {'owner': p}) #данная строка рендерит хтмл страницу detail.html и передает в него объект "p", который в хтмл шаблоне будет называться "poll"
# create a function
def example_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)