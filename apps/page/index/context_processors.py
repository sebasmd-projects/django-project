from . import models


def ctx_redes_sociales(request):
    ctx = {}
    enlaces = models.RedesSocialesModel.objects.all()
    for enlace in enlaces:
        ctx[enlace.key] = enlace.url
    return ctx


def ctx_typing(request):
    ctx = {}
    keys = models.TypingIndexModel.objects.all()
    for key in keys:
        ctx[key.typing_key] = key.typing_name
    return ctx


def ctx_title(request):
    ctx = {}
    keys = models.TitleModel.objects.all()
    for key in keys:
        ctx[key.title_key] = key.title
    return ctx


def ctx_app_name(request):
    ctx = {}
    keys = models.AppNameModel.objects.all()
    for key in keys:
        ctx[key.app_key] = key.title
    return ctx
