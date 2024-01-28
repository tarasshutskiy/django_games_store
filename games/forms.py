from django import forms
from users.models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Your comment'}),
        label='Comment'
    )

    class Meta:
        model = Comment
        fields = ['text']


class FeedbackForm(forms.Form):
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
