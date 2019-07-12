from dal import autocomplete
from django import forms

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Post, Tag


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.TextInput, label='desc', required=False)
    # content = forms.CharField(widget=CKEditorWidget(), label='content', required=True)
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='content', required=True)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='category',
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='tag',
    )

    class Meta:
        model = Post
        fields = ('category', 'tag', 'title', 'desc', 'content', 'status')
