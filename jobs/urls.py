from django.urls import path
from . import views
from . import views_2

"""
<home-url>/jobs/welcome/
<home-url>/jobs/portals/

# TODO
https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters
"""


urlpatterns = [

    path('welcome/', views.welcome),
    # keyword argument `name` is passed to path function
    # these are called as named URLs
    path("portals/", views.get_portal_details, name="portal_details"),
    path("jobtitles/", views.job_titles, name="jobtitle"),
    path("jobtitles/<int:job_id>/", views.get_job_description, name="jd"),
    path("welcomeview/", views.WelcomeView.as_view(), name="welcomeview"),

    path("v2/applicants/", views_2.ApplicantList.as_view(), name="applicant-list")
]
