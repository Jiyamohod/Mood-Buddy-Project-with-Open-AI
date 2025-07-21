from django.db import models

# Create your models here.
class ChatEntry(models.Model):
    persona=models.CharField(max_length=50)
    user_message=models.TextField()
    bot_reply=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.persona} - {self.user_message[:30]}"