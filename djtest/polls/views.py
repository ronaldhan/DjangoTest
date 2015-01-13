# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello, this is the index page.")


def detail(request, poll_id):
    return HttpResponse("You're looking at he results of poll %s" % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s" % poll_id)