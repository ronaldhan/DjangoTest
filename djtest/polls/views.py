# Create your views here.
from django.shortcuts import render_to_response
from polls.models import Poll
from django.http import HttpResponse


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    # t = loader.get_template('polls/index.html')
    # c = Context({
    #     'latest_poll_list': latest_poll_list
    # })
    # output = ', '.join([p.question for p in latest_poll_list])
    # return HttpResponse(t.render(c))
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
    return HttpResponse("You're looking at he results of poll %s" % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s" % poll_id)