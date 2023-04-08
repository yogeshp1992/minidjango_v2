from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Applicant


class Applicants(APIView):
    def get(self, request):
        applicants = Applicant.objects.all()
        applicants = {"name": applicant.name for applicant in applicants}
        return Response(applicants)
