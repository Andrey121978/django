from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):


    def clean(self):
        result = super().clean()
        main_count = 0
        unique_tags = set()
        tags_list = []
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data == {}:
                continue
            if form.cleaned_data['DELETE']:
                continue
                
            tag = form.cleaned_data['tag']
            if tag in tags_list:
                raise ValidationError('У вас дублируются теги')
            tags_list.append(tag)

            if form.cleaned_data['is_main']:
                main_count += 1

        if main_count > 1:
            raise ValidationError('Основным может быть только один раздел')


            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке

        return result  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
