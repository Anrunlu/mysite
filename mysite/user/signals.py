from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.urls import reverse
from notifications.signals import notify

@receiver(post_save, sender=User)
def send_notification(sender, instance, **kwargs):
        # 发送站内消息
        if kwargs['created'] == True:
            verb = '注册成功，交流互鉴才能共赢，欢迎参与互动～'
            url = reverse('user_info')
            notify.send(instance, recipient=instance, verb=verb, action_object=instance, url=url)