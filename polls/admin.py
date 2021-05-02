from django.contrib import admin

from .models import Choice, Question

# StackedInline（下に積み上げる表示）
# class ChoiceInline(admin.StackedInline):
# TabularInline（表形式）
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 表示順の変更
    # fields = ['pub_date', 'question_text']

    # フィールドセット（fieldsとどちらかを定義可）
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # フィールドの値表示
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # フィルタ
    list_filter = ['pub_date']
    # 検索機能（Like検索）
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
