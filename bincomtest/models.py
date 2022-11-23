# from django.db import connections
from django.db import models
# import datetime

# class PollingDetails(models.Model):
#  Iga_name = models.CharField(max_length=50)
#  party_abbreviation = models.CharField(max_length=3)
#  party_score = models.IntegerField()
#  entered_by_user = models.CharField(max_length=50)
#  date_entered = models.DateTimeField(default=datetime)
#  user_ip_address = models.CharField(max_length=50)
#  class Meta:
#   db_table="announced_lga_results"
class AnnouncedLgaResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'announced_lga_results'