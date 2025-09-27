from django.db import models
from django.utils import timezone


class OrchestrationEnum(models.TextChoices):
    DOCKER = 'docker', 'Docker'
    KUBER = 'kuber', 'Kubernetes'


class VcsEnum(models.TextChoices):
    GITHUB = 'github', 'Github'
    GITLAB = 'gitlab', 'Gitlab'


class LoggingEnum(models.TextChoices):
    METRICBEAT = 'metricbeat', 'Metricbeat'
    LOGSTASH = 'logstash', 'Logstash'
    GRAFANA = 'grafana', 'Grafana'


class MetaConfig(models.Model):
    vcs_type = models.CharField(max_length=20, choices=VcsEnum.choices)
    temperature = models.FloatField()

    def __str__(self):
        return f"MetaConfig: {self.vcs_type}"


class NewConfig(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    files = models.JSONField()  # список файлов в формате JSON
    meta_config = models.ForeignKey(MetaConfig, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Message(models.Model):
    AUTHOR_CHOICES = [
        ('model', 'Model'),
        ('user', 'User'),
    ]
    
    author = models.CharField(max_length=10, choices=AUTHOR_CHOICES)
    content = models.TextField()
    files = models.JSONField(default=list)  # список ссылок на файлы в формате JSON
    config = models.ForeignKey(NewConfig, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message by {self.author} on {self.config.name}"
