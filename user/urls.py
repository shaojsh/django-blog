from django.conf.urls import url, include
from .views import reg

urlpatterns = [
    # 配置多级路由
    url(r'^reg$', reg),
]