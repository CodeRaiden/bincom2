from django.shortcuts import render
from bincomtest.models import AnnouncedLgaResults

def Showpoll(request):
 resultsdisplay=AnnouncedLgaResults.objects.all()
 return render(request, "page1.html",{'AnnouncedLgaResults': resultsdisplay})
 