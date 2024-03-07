from cmath import log
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from chat.models import Messages


@login_required
def index(request):
    user = request.user
    messages = Messages.get_message(user=user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message["user"].username
        directs = Messages.objects.filter(user=request.user, recipient=message["user"])
        directs.update(is_read=True)

        for message in messages:
            if message["user"].username == active_direct:
                message["unread"] = 0

    context = {
        "messages": messages,
        "directs": directs,
        "user": user,
        "active_direct": active_direct,
    }
    return render(request, "chat/index.html", context)

@login_required
def Directs(request, username):
    user = request.user
    messages = Messages.get_message(user=user)
    active_direct = username
    directs = Messages.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)

    for message in messages:
        if message["user"].username == username:
            message["unread"] = 0
    context = {
        "messages": messages,
        "directs": directs,
        "user": user,
        "active_direct": active_direct,
    }
    return render(request, "chat/index.html", context)
