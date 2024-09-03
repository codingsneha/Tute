from django.db import models

class Tutorial(models.Model):
    transcript = models.FileField(upload_to='transcripts/')
    video = models.FileField(upload_to='videos/')
    final_video = models.FileField(upload_to='final_videos/', blank=True, null=True)
