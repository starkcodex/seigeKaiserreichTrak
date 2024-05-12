from django.contrib.auth.models import User
from django.db import models



class Team(models.Model):

    ACTIVE = 'active'
    DELETED = 'deleted'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted')
    )


    title = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    # plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.CASCADE)
    # plan_end_date = models.DateTimeField(blank=True, null=True)
    # plan_status = models.CharField(max_length=20, choices=CHOICES_PLAN_STATUS, default=PLAN_ACTIVE)
    # stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    # stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title