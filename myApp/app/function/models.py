"""
Copyright 2024 (C) NetDB, NCKU - All Rights Reserved.
Unauthorized copying and sharing of this file, via any medium is strictly prohibited.
Contact: dcert-service@netdb.csie.ncku.edu.tw
"""
from django.db import models
from django.utils import timezone

# Create your models here.
class entries(models.Model):
    entry_id = models.AutoField(primary_key=True)
    guestname = models.CharField(max_length=255, blank=False, null=False)
    content = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.guestname
