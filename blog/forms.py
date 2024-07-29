from django import forms
from .models import MessagePage, CommentPage


class MessagePageForm(forms.ModelForm):
    class Meta:
        model = MessagePage
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(MessagePageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': "col-sm-12"}),
        #     'email': forms.TextInput(attrs={'class': "col-sm-12"}),
        #     'subject': forms.TextInput(attrs={'class': "col-sm-12"}),
        #     'message': forms.Textarea(attrs={'class': "form-control"})
        # }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPage
        fields = ['name', 'email', 'website', 'comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class":"form-control"})
