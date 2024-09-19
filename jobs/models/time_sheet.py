"""
Models for timesheet entries recording user actions.
"""
from __future__ import annotations

import uuid

from django.db import models


class Timesheet(models.Model):
    """
    Represents a timesheet entry for recording user actions (e.g., clocking in and out).

    Attributes:
        id (UUIDField): A unique identifier for the timesheet entry.
        user (ForeignKey): A foreign key linking to the User model.
        action (CharField): The action performed, either 'in'
        (clock in) or 'out' (clock out).
        timestamp (DateTimeField): The date and time when the action was recorded.
    """
    ACTION_CHOICES = [
        ('in', 'Clock In'),
        ('out', 'Clock Out'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('accounts.SimpleUser', on_delete=models.CASCADE)
    job_id = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=3, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField()

    def get_action_display(self):
        """
        Returns the human-readable display value of the action.
        """
        return dict(self.ACTION_CHOICES)[self.action]

    def __str__(self):
        return (
            f"Timesheet Entry: User ID {self.user_id}, "
            f"Action '{self.get_action_display()}' at {self.timestamp}"
        )
