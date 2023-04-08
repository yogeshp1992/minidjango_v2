from jobs.models import JobTitle


def jobtitle_list(request):

    if request.method == "GET":
        job_titles = JobTitle.objects.all()


        breakpoint()

    elif request.method == "POST":
        pass
