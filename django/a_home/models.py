from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    event_id = models.CharField(max_length=10, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=4)

    def save(self, *args, **kwargs):
        if not self.event_id:  # 만약 event_id가 설정되지 않았다면
            # Task 모델에서 가장 마지막 event_id를 가져와서 숫자를 추출
            last_event = Task.objects.all().order_by('id').last()
            if last_event:
                last_number = int(last_event.event_id.replace('event', ''))  # 'event' 문자열 제거 후 숫자 변환
                self.event_id = f'event{last_number + 1}'
            else:
                self.event_id = 'event1'  # 이전 이벤트가 없으면 'event1'로 설정
        super().save(*args, **kwargs)  # 모델 저장

    def __str__(self):
        return str(self.user) + ' - ' + str(self.title)
