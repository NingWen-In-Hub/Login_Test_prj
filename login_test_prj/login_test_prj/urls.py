from django.contrib import admin
from django.contrib.staticfiles.urls import static  # 本Ch11.1
from django.urls import path, include

from . import settings_common, settings_dev  # 本Ch11.1
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_test_app.urls')),
    path('accounts/', include('allauth.urls')),  # allauthデフォルトURL：本P218
    path('__debug__/', include(debug_toolbar.urls)),

]

#　開発サーバーでMEDIA_ROOT,MEDIA_URLを渡したdjango.contrib.staticfiles.urls.static関数から
#　返されたルーティングを追加する
urlpatterns +=static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)
