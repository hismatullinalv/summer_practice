from django.db import models


class Vendors(models.Model):

    class Meta:
        db_table = "vendors"
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    name_vendor = models.TextField(verbose_name="Имя вендора")

    def __str__(self):
        return f"{self.id}"


class License(models.Model):

    class Meta:
        db_table = "license"
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"

    vendor_id = models.ForeignKey(Vendors, on_delete=models.RESTRICT, verbose_name="ID вендора")
    name_lic = models.TextField(verbose_name="Имя лицензии")

    def __str__(self):
        return f"{self.name_lic}"


class Dep(models.Model):

    class Meta:
        db_table = "dep"
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    num_dep = models.IntegerField(verbose_name="Номер отдела")

    def __str__(self):
        return f"{self.num_dep}"


class User(models.Model):

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    name_user = models.TextField(verbose_name="ФИО пользователя")
    dep_id = models.ForeignKey(Dep, on_delete=models.RESTRICT, verbose_name="ID отдела")

    def __str__(self):
        return f"{self.name_user} {self.dep_id}"


class PC(models.Model):

    class Meta:
        db_table = "pc"
        verbose_name = "ПК"
        verbose_name_plural = "ПК"

    num_pc = models.TextField(verbose_name="Номер компьютера")

    def __str__(self):
        return f"{self.num_pc}"


class Sessions(models.Model):

    class Meta:
        db_table = "sessions"
        verbose_name = "Сессия"
        verbose_name_plural = "Сессии"

    date_start = models.DateTimeField(verbose_name="Дата начала сессии")
    num_lic = models.IntegerField(verbose_name="Количество активных лицензий")
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="ID пользователя")
    pc_id = models.ForeignKey(PC, on_delete=models.RESTRICT, verbose_name="ID пк")
    lic_id = models.ForeignKey(License, on_delete=models.RESTRICT, verbose_name="ID лицензии")

    def __str__(self):
        return f"{self.date_start} {self.num_lic}"


