from django.forms import ModelForm
from .models import Question

# Create the form class.
class QuestionCategoryForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say somethings...'}
            )
        }

