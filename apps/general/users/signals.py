from datetime import date
from PIL import Image


def optimize_image(sender, instance, **kwargs):
    if instance.avatar:
        avatar = Image.open(instance.avatar.path)
        avatar.save(instance.avatar.path, quality=20, optimize_image=True)


def user_directory_path(instance, filename):
    return "filer_public/avatar/{}-{}-{}/{}-{}".format(date.today().year, date.today().month, date.today().day, instance.full_name, filename)
