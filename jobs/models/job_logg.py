"""
This module defines the JobLog model for logging job-related activities.
"""
from __future__ import annotations

import uuid

from django.db import models

from accounts.models import User
from jobs.models import Job


class JobLog(models.Model):
    """
    Represents a log entry for a job, recording user interactions or events.

    Attributes:
        id (UUIDField): A unique identifier for the job log entry.
        user (ForeignKey): A foreign key linking to the User model,
                            representing the user who interacted with the job.
        job (ForeignKey): A foreign key linking to the Job model,
                            representing the job related to this log entry.
        created_at (DateTimeField): The date and time when the log entry was created.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
