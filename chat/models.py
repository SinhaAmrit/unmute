from django.db import models
from django.db.models import Model, Max, Count, Sum
from django.contrib.auth.models import User


class Messages(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="from_user")
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="to_user"
    )
    body = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def sender_message(from_user, to_user, body):
        sender_message = Messages(
            user=from_user,  # as you started the convocation
            sender=from_user,  # as you sent the first message
            recipient=to_user,  # because you are getting a message from me => to_user
            body=body,
            is_read=True,
        )
        sender_message.save()

        recipient_message = Messages(
            user=to_user,
            sender=from_user,
            recipient=from_user,
            body=body,
            is_read=True,
        )
        recipient_message.save()
        return sender_message

    def get_message(user):
        users = []
        messages = (
            Messages.objects.filter(user=user)
            .values("recipient")
            .annotate(last=Max("date"))
            .order_by("-last")
        )
        for message in messages:
            users.append(
                {
                    "user": User.objects.get(pk=message["recipient"]),
                    "last": message["last"],
                    "unread": Messages.objects.filter(
                        user=user, recipient__pk=message["recipient"], is_read=False
                    ).count(),
                }
            )
        return users
