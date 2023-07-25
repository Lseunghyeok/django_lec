from django.db import models
from django.contrib.auth.models import User

class MainContent(models.Model):
    title=models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.title
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #자신과 다대일 관계인 객체를 만들려면 models.ForeignKey('self', on_delete=models.CASCADE) 사용
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE) #MainContent에 여러개의 Comment가 달릴 수 있는데 MainContent를 삭제하면 관련 모든 Comment 삭제
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True) #최초 시간을 저장
    modify_date = models.DateTimeField(auto_now=True) # 수정 시간을 저장
