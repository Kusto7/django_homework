﻿from django import forms
from catalog.models import Product, Version
from django.core.exceptions import ValidationError

danger_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'image',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in danger_words:
            raise forms.ValidationError('Название некорректное, придумайте другое.')

        return cleaned_data

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        for exclusion_word in danger_words:
            if exclusion_word in cleaned_description.lower():
                raise forms.ValidationError('Описание содержит некорректные слова')
            return cleaned_description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
