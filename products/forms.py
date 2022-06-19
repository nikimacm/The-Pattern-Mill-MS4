from django import forms
from .models import Product, Category, Comment


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commenter_name', 'comment_body',)
        widgets = {
            'commenter_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment_body': forms.Textarea(attrs={'class': 'form-control'}),
        }
