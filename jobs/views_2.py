"""
Applicant (Resource)

GET HTTP request
- singular
- plural
"""


from django.views.generic import ListView
from jobs.models import Applicant


class ApplicantList(ListView):
    model = Applicant

