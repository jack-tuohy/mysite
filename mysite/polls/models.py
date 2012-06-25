"""
Models for the polls app.
"""

import datetime
from django.utils import timezone
from django.db import models


class Poll(models.Model):
    """
    Model for a poll object.
    """

    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def was_published_recently(self):
        """
        Indicates if the poll was published recently.
        """

        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    """
    Model for a choice within a poll.
    """
    
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice
