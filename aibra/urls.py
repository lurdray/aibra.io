
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("main.urls")),
    path("app/", include("app_user.urls")),
    path("wallet/", include("wallet.urls")),
    path("job/", include("job.urls")),
    path("resume/", include("resume.urls")),
    path("quiz/", include("quiz.urls")),
    path("interview/", include("interview.urls")),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)