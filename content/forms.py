from django import forms
from .models import Todolist
#모델폼 : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성
class PostForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['title','image','description','write_time','finish_time']
    # Model Form 클래스에 구현되어있는 .save 메소드
    # def save(self, commit=True):
	# 	self.instance = Post(**self.cleaned_data)
	# 	if commit:
	# 		self.instance.save()
	# 	return self.instance

    
