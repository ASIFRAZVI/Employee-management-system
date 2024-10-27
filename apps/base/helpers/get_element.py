from django.db import models


def getObject(model: models.Model, id: str = None):
    if id is None:
        return model.objects.all()
    try:
        return model.objects.get(pk=id)
    except model.DoesNotExist:
        return None
