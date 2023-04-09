from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Applicant
from django.contrib.auth.models import User


class Applicants(APIView):
    def get(self, request):
        applicants = Applicant.objects.all()
        applicants = {"name": applicant.name for applicant in applicants}
        return Response(applicants)

    def post(self, request):
        # TODO - write logic to take JSON input from `request.body`
        # TODO - write ORM query to insert record in the database
        resp = {"message": "success", "records": ""}
        return Response(resp)

    def delete(self, request):
        # TODO - write logic to take json input from `request.body`
        # TODO - write ORM query to delete record from database.
        pass


###############################################
# django default authentication system        #
###############################################

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        final = dict()
        for user in users:
            final[user.id] = {"first_name": user.first_name,
                              "email": user.email}

        return Response(final)
