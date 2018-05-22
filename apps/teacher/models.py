from django.db import models

from apps.user.models import User


# Create your models here.
# 教学工作量
class Teacher_work(models.Model):
    course_name=models.CharField(max_length=50,verbose_name='课程名')
    course_type=models.CharField(max_length=50,verbose_name='课程类别')
    course_jidian=models.IntegerField(default=0,verbose_name='业绩点')
    course_discript=models.CharField(max_length=128,verbose_name='描述')
    class Meta:
        db_table = 'teacher_work'
        verbose_name = '教学工作量业绩'
        verbose_name_plural = verbose_name
# 教研业绩量化
class Teacher_yan(models.Model):
    pro_name = models.CharField(max_length=50, verbose_name='项目名')
    pro_type = models.CharField(max_length=50, verbose_name='项目类别')
    pro_jidian = models.IntegerField(default=0, verbose_name='业绩点')
    pro_discript = models.CharField(max_length=128, verbose_name='备注')
    class Meta:
        db_table = 'teacher_yan'
        verbose_name = '教研业绩'
        verbose_name_plural = verbose_name

# 教学平台建设业绩量化表
class Teacher_pingtai(models.Model):
    pro_level = models.CharField(max_length=50, verbose_name='项目级别')
    pro_huozhun = models.IntegerField(default=0, verbose_name='获准业绩点')
    pro_huozhunlast = models.IntegerField(default=0, verbose_name='获准后建设期年度考核业绩点')
    pro_check = models.CharField(max_length=128, verbose_name='考核等级')
    pro_check_math = models.CharField(max_length=128, verbose_name='考核等级')

    class Meta:
        db_table = 'teacher_pingtai'
        verbose_name = '教学平台建设业绩量化表'
        verbose_name_plural = verbose_name

# 教材业绩量化表
class Teacher_book(models.Model):
    Choice=((0,'国家级规划教材'),
            (1,'省级规划教材'),
            (2, '其他教材'),
            (3, '中文编写'),
            (4, '外文编写')
            )
    # book_level=models.SmallIntegerField(default=1,choices=Choice,verbose_name='1.教材级别系数、语言类别系数表')
    book_level=models.ForeignKey('Book_level',verbose_name='.教材级别系数、语言类别系数表')
    book_auth=models.ForeignKey('Book_auth',verbose_name='主编部分')
    book_lixiang=models.ForeignKey('Book_lixiang',verbose_name='立项系数')
    class Meta:
        db_table = 'teacher_book'
        verbose_name = '教材业绩量化表'
        verbose_name_plural = verbose_name


class Book_level(models.Model):
    book_level_name=models.CharField(max_length=50, verbose_name='等级名称')
    book_jidian=models.IntegerField(default=0, verbose_name='业绩点')
    class Meta:
        db_table = 'book_level'
        verbose_name = '教材级别系数、语言类别系数表'
        verbose_name_plural = verbose_name
class Book_auth(models.Model):
    book_auth_name = models.CharField(max_length=50, verbose_name='主编名称')
    auth_jidian = models.IntegerField(default=0, verbose_name='业绩点')

    class Meta:
        db_table = 'book_auth'
        verbose_name = '主编部分'
        verbose_name_plural = verbose_name
class Book_lixiang(models.Model):
    book_lixiang_name = models.CharField(max_length=50, verbose_name='立项名')
    book_lixiang_math = models.CharField(max_length=50, verbose_name='立项系数')

    class Meta:
        db_table = 'book_lixiang'
        verbose_name = '立项系数'
        verbose_name_plural = verbose_name



# 业绩表 没用了
class Teacher_count(models.Model):
    usernum=models.CharField(max_length=50,verbose_name='用户学号')
    count_jidian=models.IntegerField(default=0,verbose_name='个人业绩点')
    rate_jidian=models.ForeignKey('Rate_jidian',verbose_name='额定业绩点')
    class Meta:
        db_table = 'teacher_count'
        verbose_name = '教师业绩点统计'
        verbose_name_plural = verbose_name

class Rate_jidian(models.Model):
    name=models.CharField(max_length=50, verbose_name='职称名')
    scien_jiidan=models.IntegerField(default=0,verbose_name='教学业绩点')
    teach_jiidan = models.IntegerField(default=0, verbose_name='科研业绩点')
    class Meta:
        db_table = 'rate_jidian'
        verbose_name = '职称对应业绩点'
        verbose_name_plural = verbose_name


# 目前使用的是这个业绩表
class Work_count(models.Model):
    usernum=models.CharField(max_length=50,verbose_name='用户学号')
    count_jidians=models.IntegerField(default=0,verbose_name='个人业绩点')
    rate_jidians=models.ForeignKey('Work_rate_jidian',verbose_name='额定业绩点')
    class Meta:
        db_table = 'work_count'
        verbose_name = '业绩点统计'
        verbose_name_plural = verbose_name
# 目前使用的是这个业绩表
class Work_rate_jidian(models.Model):
    pro_name=models.CharField(max_length=50, verbose_name='职称名')
    scien_jiidans=models.IntegerField(default=0,verbose_name='教学业绩点')
    teach_jiidans = models.IntegerField(default=0, verbose_name='科研业绩点')
    class Meta:
        db_table = 'work_rate_jidian'
        verbose_name = '职称业绩点'
        verbose_name_plural = verbose_name


# 自然科学类
# 1.自然科学 科研项目业绩量化
class Nature_keyan(models.Model):
    pro_level=models.CharField(max_length=120,verbose_name='项目级别')
    pro_math=models.CharField(max_length=20,verbose_name='系数')
    pro_jidian=models.CharField(max_length=120,verbose_name='立项绩点')
    class Meta:
        db_table = 'nature_keyan'
        verbose_name = '自然科学 科研项目业绩量化'
        verbose_name_plural = verbose_name

# 2.论文业绩量化表
class Thesis_sci(models.Model):
    sci_name=models.CharField(max_length=120,verbose_name='sci收录')
    sci_jidian=models.CharField(max_length=120,verbose_name='对应业绩点')
    class Meta:
        db_table = 'thesis_sci'
        verbose_name = 'sci区'
        verbose_name_plural = verbose_name

class Thesis_cscd(models.Model):
    cscd_name = models.CharField(max_length=120, verbose_name='cscd核心库')
    cscd_jidian = models.CharField(max_length=120, verbose_name='对应业绩点')

    class Meta:
        db_table = 'thesis_cscd'
        verbose_name = 'cscd区'
        verbose_name_plural = verbose_name

class Thesis_ei(models.Model):
    ei_name = models.CharField(max_length=120, verbose_name='ei收录')
    ei_jidian = models.CharField(max_length=120, verbose_name='对应业绩点')

    class Meta:
        db_table = 'thesis_ei'
        verbose_name = 'ei区'
        verbose_name_plural = verbose_name

# 3.知识产权业绩量化表  intellectual property right
class Intellectual(models.Model):
    intellectual_name=models.CharField(max_length=120,verbose_name='专利名称')
    intellectual_jidina=models.CharField(max_length=120,verbose_name='专利绩点')
    class Meta:
        db_table = 'intellectual'
        verbose_name = '知识产权'
        verbose_name_plural = verbose_name

# 4.著作业绩量化表
# 出版社
class Nut_book_concern(models.Model):
    book_concern_name=models.CharField(max_length=120,verbose_name='出版社级别名')
    book_concern_jidian=models.CharField(max_length=120,verbose_name='对应系数')
    class Meta:
        db_table = 'nut_book_concern'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

class Nut_book_auth(models.Model):
    book_auth_name=models.CharField(max_length=120,verbose_name='著书身份名')
    book_auth_jidian=models.CharField(max_length=120,verbose_name='对应业绩点')
    class Meta:
        db_table = 'nut_book_auth'
        verbose_name = '著书身份'
        verbose_name_plural = verbose_name

class Nut_book_lixinag(models.Model):
    book_lixinag_name=models.CharField(max_length=120,verbose_name='立项名')
    book_lixinag_jidian=models.CharField(max_length=120,verbose_name='对应系数')
    class Meta:
        db_table = 'nut_book_lixinag'
        verbose_name = '立项'
        verbose_name_plural = verbose_name


# 5.项目结业、评价业绩量化表
class Country(models.Model):
    country_name=models.CharField(max_length=120,verbose_name='组织单位名')
    class Meta:
        db_table = 'country'
        verbose_name = '组织单位'
        verbose_name_plural = verbose_name

class End_pro(models.Model):
    end_pro_name=models.CharField(max_length=120,verbose_name='结题等级')
    # end_pro_jidian=models.CharField(max_length=120,verbose_name='对应绩点')
    # end_pro_country=models.ForeignKey('Country',verbose_name='对应单位')
    class Meta:
        db_table = 'end_pro'
        verbose_name = '结题'
        verbose_name_plural = verbose_name

class End_pingjia(models.Model):
    pingjia_name=models.CharField(max_length=120,verbose_name='评价等级')
    # pingjia_jidian=models.CharField(max_length=120,verbose_name='对应绩点')
    # pingjia_country=models.ForeignKey('Country',verbose_name='对应单位')
    class Meta:
        db_table = 'end_pingjia'
        verbose_name = '评价'
        verbose_name_plural = verbose_name
class End_jidna(models.Model):
    country=models.ForeignKey('Country',verbose_name='组织单位')


# 6.科研奖励的业绩量化
class Science(models.Model):
    reward_level=models.ForeignKey('Country',verbose_name='奖励等级')
    reward_level1=models.ForeignKey('Reward_level1',verbose_name='奖励等级1')
    reward_jidian=models.CharField(max_length=120,verbose_name='奖励绩点')
    class Meta:
        db_table = 'science'
        verbose_name = '科研奖励'
        verbose_name_plural = verbose_name

class Reward_level1(models.Model):
    reward_level1_name=models.CharField(max_length=120,verbose_name='奖励等级1名')
    class Meta:
        db_table = 'reward_level1'
        verbose_name = '奖励等级1'
        verbose_name_plural = verbose_name


# 7.科研平台业绩量化表
class Kaohe_level(models.Model):
    # 考核验收等级
    kaohe_name=models.CharField(max_length=120,verbose_name='考核验收等级名')
    kaohe_math=models.CharField(max_length=120,verbose_name='考核验收系数')
    class Meta:
        db_table = ' kaohe_level'
        verbose_name = '考核验收等级'
        verbose_name_plural = verbose_name

class Pingtai(models.Model):
    pingtai_level=models.ForeignKey('Country',verbose_name='等级')
    pingtai_huozhun=models.CharField(max_length=120,verbose_name='获准绩点')
    pingtai_yanshou=models.CharField(max_length=120,verbose_name='验收绩点')

    class Meta:
        db_table = 'pingtai'
        verbose_name = '科研平台'
        verbose_name_plural = verbose_name



# 自然科学类


# class Work_jidian(models.Model):
#     user = models.ForeignKey('User',verbose_name='对应的人')
#     count_jidians = models.IntegerField(default=0, verbose_name='个人业绩点')
#     rate_jidians = models.ForeignKey('Work_rate_jidian', verbose_name='额定业绩点')
#
#     class Meta:
#         db_table = 'work_jidan'
#         verbose_name = '业绩点统计'
#         verbose_name_plural = verbose_name
#
