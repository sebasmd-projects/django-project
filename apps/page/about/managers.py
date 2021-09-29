from django.db import models


class AboutModelManager(models.Manager):
    
    def about_manager(self):
        return self.all()