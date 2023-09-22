from django.db import models

# Create your models here.


class Admin(models.Model):
    """管理员"""

    user = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.user


class Department(models.Model):
    """部门表"""

    department_name = models.CharField(verbose_name="部门名称", max_length=32)
    employees_num = models.IntegerField(verbose_name="员工人数")

    # 输出对象时，如果想要定制显示的内容，可以定义一个__str__方法
    def __str__(self):
        return self.department_name


class UserInfo(models.Model):
    """员工表"""

    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=63)
    age = models.IntegerField(verbose_name="年龄")
    create_time = models.DateField(verbose_name="入职时间")

    # 置空
    depart = models.ForeignKey(
        to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL
    )

    # 在Django中做约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )

    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class AjaxTask(models.Model):
    """任务"""

    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )

    level = models.SmallIntegerField(
        verbose_name="级别", choices=level_choices, default=1
    )
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")

    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)


class Parts(models.Model):
    """零件"""

    pid = models.CharField(verbose_name="零件编号", max_length=64)
    name = models.CharField(verbose_name="零件名称", max_length=32)
    unit = models.CharField(verbose_name="计量单位", max_length=32)
    amount = models.IntegerField(verbose_name="库存量")
    price = models.FloatField(verbose_name="单价")
    store = models.CharField(verbose_name="仓库存储位置", max_length=64)
    description = models.CharField(verbose_name="附加描述", max_length=128)

    def __str__(self):
        return self.name


class Sales(models.Model):
    """订单管理"""

    COMPANY = "公司"
    SMALL_BUSINESS = "小型企业"
    CONSUMER = "消费者"
    CUSTOMER_IN_CHOICES = [(COMPANY, "公司"), (SMALL_BUSINESS, "小型企业"), (CONSUMER, "消费者")]

    bid = models.CharField(verbose_name="订单号", max_length=64)
    name = models.ForeignKey(
        verbose_name="商品名称",
        to="Parts",
        to_field="id",
        on_delete=models.CASCADE,
    )
    sale_num = models.IntegerField(verbose_name="销售数量", default=0)
    profit = models.FloatField(verbose_name="销售利润")
    customer = models.CharField(
        verbose_name="采购方",
        choices=CUSTOMER_IN_CHOICES,
        max_length=64,
        default=SMALL_BUSINESS,
    )
    time = models.DateTimeField(auto_now=True)
