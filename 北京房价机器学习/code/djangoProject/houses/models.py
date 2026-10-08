from django.db import models


class House(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='唯一标识')
    community_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='小区名称')
    district = models.CharField(max_length=255, null=True, blank=True, verbose_name='所在区域')
    total_price = models.CharField(max_length=255, null=True, blank=True, verbose_name='总价')
    unit_price = models.CharField(max_length=255, null=True, blank=True, verbose_name='单价')
    house_layout = models.CharField(max_length=255, null=True, blank=True, verbose_name='房屋户型')
    floor_location = models.CharField(max_length=255, null=True, blank=True, verbose_name='所在楼层')
    building_area = models.CharField(max_length=255, null=True, blank=True, verbose_name='建筑面积')
    layout_structure = models.CharField(max_length=50, null=True, blank=True, verbose_name='户型结构')
    inner_area = models.CharField(max_length=255, null=True, blank=True, verbose_name='套内面积')
    building_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='建筑类型')
    orientation = models.CharField(max_length=255, null=True, blank=True, verbose_name='房屋朝向')
    building_structure = models.CharField(max_length=50, null=True, blank=True, verbose_name='建筑结构')
    decoration_condition = models.CharField(max_length=50, null=True, blank=True, verbose_name='装修情况')
    elevator_ratio = models.CharField(max_length=20, null=True, blank=True, verbose_name='梯户比例')
    has_elevator = models.CharField(max_length=255, null=True, blank=True, verbose_name='供暖方式')
    property_rights_years = models.CharField(max_length=255, null=True, blank=True, verbose_name='产权年限')
    listing_time = models.CharField(max_length=255, null=True, blank=True, verbose_name='挂牌时间')
    transaction_ownership = models.CharField(max_length=50, null=True, blank=True, verbose_name='交易权属')
    last_transaction = models.CharField(max_length=255, null=True, blank=True, verbose_name='上次交易信息')
    house_usage = models.CharField(max_length=255, null=True, blank=True, verbose_name='房屋用途')
    house_years = models.CharField(max_length=255, null=True, blank=True, verbose_name='房屋年限')
    property_ownership = models.CharField(max_length=50, null=True, blank=True, verbose_name='产权所属')
    mortgage_info = models.CharField(max_length=255, null=True, blank=True, verbose_name='抵押信息')
    house_certificate_info = models.CharField(max_length=255, null=True, blank=True, verbose_name='房本备件')

    class Meta:
        verbose_name = "房屋数据"
        verbose_name_plural = "房屋数据"
    # def unicode(self):
    #     return self.community_name
