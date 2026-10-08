
from django.contrib import admin

from houses.models import House
admin.site.site_header = '房价机器学习后台'  # 设置header
admin.site.site_title = '房价机器学习后台'   # 设置title
admin.site.index_title = '房价机器学习后台'
# admin.site.register(House)
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'community_name', 'district', 'total_price','unit_price','house_layout','floor_location','building_area'
                    ,'layout_structure','inner_area','building_type','orientation','building_structure',
                    'decoration_condition','elevator_ratio','has_elevator','property_rights_years',
                    'listing_time','transaction_ownership','last_transaction','house_usage','house_years','property_ownership','mortgage_info','house_certificate_info')
    search_fields = ['community_name', 'district', 'total_price','unit_price','house_layout','floor_location','building_area'
                    ,'layout_structure','inner_area','building_type','orientation','building_structure',
                    'decoration_condition','elevator_ratio','has_elevator','property_rights_years',
                    'listing_time','transaction_ownership','last_transaction']