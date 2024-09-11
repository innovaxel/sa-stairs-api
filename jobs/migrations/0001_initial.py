# Generated by Django 4.0.4 on 2024-09-11 19:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=255)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ErrorCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JobAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('resource_id', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='WorkList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worklists', to='jobs.location')),
            ],
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('action', models.CharField(choices=[('in', 'Clock In'), ('out', 'Clock Out')], max_length=3)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('worklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.worklist')),
            ],
        ),
        migrations.CreateModel(
            name='JobSubmission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_submissions', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='JobLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobaddress'),
        ),
        migrations.AddField(
            model_name='job',
            name='chip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.chip'),
        ),
        migrations.AddField(
            model_name='job',
            name='customerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.customer'),
        ),
        migrations.AddField(
            model_name='job',
            name='worklistid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.worklist'),
        ),
        migrations.CreateModel(
            name='ErrorSubCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('error_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='jobs.errorcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('errorsubcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='errors', to='jobs.errorsubcategory')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='errors', to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported_errors', to='accounts.user')),
            ],
        ),
    ]
