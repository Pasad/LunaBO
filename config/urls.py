# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')), # 회원 정보 API 관련 URL 추가
    path('api/weather/', include('weather.urls')), # 날씨 API 관련 URL 추가
    path('api/board/', include('board.urls')), # 게시판 API 관련 URL 추가
    path('api/albums/', include('albums.urls')), # 앨범 API 관련 URL 추가
]

# 로컬 미디어 파일 접근 허용
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)