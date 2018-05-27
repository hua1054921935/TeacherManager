from django.contrib import admin

# Register your models here.
from .models import Teacher_work, Teacher_pingtai, Book_level, Book_lixiang, Book_auth, Work_rate_jidian, Work_count, \
    Nature_keyan, Thesis_sci, Thesis_cscd, Thesis_ei, Intellectual, Nut_book_auth, Nut_book_concern, Nut_book_lixinag, \
    Country, Science



# 教学工作量
class Teacher_workAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'course_type', 'course_jidian', 'course_discript']
    fields = ('course_name', 'course_type', 'course_jidian', 'course_discript')

# 教研业绩量化
class Teacher_yanAdmin(admin.ModelAdmin):
    list_display = ['id', 'pro_name', 'pro_type', 'pro_jidian', 'pro_discript']
    fields = ('pro_name', 'pro_type', 'pro_jidian', 'pro_discript')

# 教学平台建设业绩量化表
class Teacher_pingtaiAdmin(admin.ModelAdmin):
    list_display = ['id', 'pro_level', 'pro_huozhun', 'pro_huozhunlast', 'pro_check','pro_check','pro_check_math']
    # fields = ('pro_level', 'pro_huozhun', 'pro_huozhunlast', 'pro_check','pro_check',)

# 教材业绩量化表
class Teacher_bookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_level', 'book_auth', 'book_lixiang']
    fields = ('book_level', 'book_auth', 'book_lixiang')

class Book_levelAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_level_name', 'book_jidian']
    fields = ('book_level_name', 'book_jidian')

class Book_authAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_auth_name', 'auth_jidian']
    fields = ( 'book_auth_name', 'auth_jidian')

class Book_lixiangAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_lixiang_name', 'book_lixiang_math']
    fields = ( 'book_lixiang_name', 'book_lixiang_math')

class Work_rate_jidianAdmin(admin.ModelAdmin):
    list_display = ['id', 'pro_name', 'scien_jiidans','teach_jiidans']
    fields = ('pro_name', 'scien_jiidans','teach_jiidans')

class Work_countAdmin(admin.ModelAdmin):
    list_display = ['id', 'usernum', 'count_jidians', 'rate_jidians']
    fields = ('name', 'usernum', 'count_jidians', 'rate_jidians')


# 自然科学类
# 1.自然科学 科研项目业绩量化
class Nature_keyanAdmin(admin.ModelAdmin):
    list_display = ['id', 'pro_level', 'pro_math', 'pro_jidian']
    fields = ('pro_level', 'pro_math', 'pro_jidian')

# 2.论文业绩量化表
class Thesis_sciAdmin(admin.ModelAdmin):
    list_display = ['id', 'sci_name', 'sci_jidian']
    fields = ('sci_name', 'sci_jidian')
class Thesis_cscdAdmin(admin.ModelAdmin):
    list_display = ['id', 'cscd_name', 'cscd_jidian']
    fields = ('cscd_name', 'cscd_jidian')
class Thesis_eiAdmin(admin.ModelAdmin):
    list_display = ['id', 'ei_name', 'ei_jidian']
    fields = ('ei_name', 'ei_jidian')


# 3.知识产权业绩量化表  intellectual property right

class IntellectualAdmin(admin.ModelAdmin):
    list_display = ['id', 'intellectual_name', 'intellectual_jidina']
    fields = ('intellectual_name', 'intellectual_jidina')

# 4.著作业绩量化表
# 出版社
class Nut_book_concernAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_concern_name', 'book_concern_jidian']
    fields = ('book_concern_name', 'book_concern_jidian')


class Nut_book_authAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_auth_name', 'book_auth_jidian']
    fields = ('book_auth_name', 'book_auth_jidian')


class Nut_book_lixinagAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_lixinag_name', 'book_lixinag_jidian']
    fields = ('book_lixinag_name', 'book_lixinag_jidian')

# 5.项目结业、评价业绩量化表
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'country_name']
    fields = ('country_name',)


class End_proAdmin(admin.ModelAdmin):
    list_display = ['id', 'end_pro_name']
    fields = ('end_pro_name')


class End_pingjiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pingjia_name']
    fields = ('pingjia_name')

# 6.科研奖励的业绩量化
class ScienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'reward_level','reward_level1','reward_jidian']
    fields = ('reward_level','reward_level1','reward_jidian')


class Reward_level1Admin(admin.ModelAdmin):
    list_display = ['id', 'reward_level1_name']
    fields = ('reward_level1_name')

# 7.科研平台业绩量化表
class Kaohe_levelAdmin(admin.ModelAdmin):
    list_display = ['id', 'kaohe_name','kaohe_math']
    fields = ('kaohe_name','kaohe_math')


class PingtaiAdmin(admin.ModelAdmin):
    list_display = ['id', 'pingtai_level', 'pingtai_huozhun','pingtai_yanshou']
    fields = ('pingtai_level', 'pingtai_huozhun','pingtai_yanshou')


# class Kaohe_levelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'kaohe_name', 'kaohe_math']
#     fields = ('kaohe_name', 'kaohe_math')
#
#
# class Kaohe_levelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'kaohe_name', 'kaohe_math']
#     fields = ('kaohe_name', 'kaohe_math')


admin.site.register(Teacher_work, Teacher_workAdmin)
admin.site.register(Teacher_pingtai, Teacher_pingtaiAdmin)
admin.site.register(Book_level, Book_levelAdmin)
admin.site.register(Book_lixiang, Book_lixiangAdmin)
admin.site.register(Book_auth, Book_authAdmin)
admin.site.register(Work_rate_jidian, Work_rate_jidianAdmin)
admin.site.register(Work_count, Work_countAdmin)
admin.site.register(Nature_keyan, Nature_keyanAdmin)
admin.site.register(Thesis_sci, Thesis_sciAdmin)
admin.site.register(Thesis_cscd, Thesis_cscdAdmin)
admin.site.register(Thesis_ei, Thesis_eiAdmin)
admin.site.register(Intellectual, IntellectualAdmin)
admin.site.register(Nut_book_auth, Nut_book_authAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Nut_book_lixinag, Nut_book_lixinagAdmin)
admin.site.register(Nut_book_concern, Nut_book_concernAdmin)
admin.site.register(Science, ScienceAdmin)