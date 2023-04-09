from jobs.models import JobTitle, Portal
from jobs.serializers import JobTitleSerializer, PortalSerializer
from django.http import JsonResponse, HttpResponse


def jobtitle_list(request):

    if request.method == "GET":
        job_titles = JobTitle.objects.all()

        #############################################################
        # how to serialize multiple objects using DRF serializer?   #
        #############################################################
        job_titles = JobTitleSerializer(job_titles, many=True)

        # whenever data is in non-dict format we have to set `safe=False`
        return JsonResponse(job_titles.data, safe=False)

    elif request.method == "POST":
        pass


# TODO portals list
def portal_list(request):
    if request.method == "GET":
        portals = Portal.objects.all()
        portals_data = PortalSerializer(portals, many=True)
        return JsonResponse(portals_data.data, safe=False)
