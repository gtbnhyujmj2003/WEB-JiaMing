"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app01 import views

# 當按下按鈕的時候 (或者其他的功能)
# 實際上按鈕是送出一個網址
# 當送出的網址符合下面的規則時
# (藉由views.py內的資料) 導到特定的網頁

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloA/', views.helloA),   # 也可以用路徑字串 "app01.views.helloA" 做出同樣效果
    path('helloB/', views.helloB),
    path('', views.index),
]
