# coding: utf-8
from django.db import models


class KindPersonManager(models.Manager):
    def __init__(self, kind):
        super(KindPersonManager, self).__init__()
        self.kind = kind

    def get_query_set(self):
        qs = super(KindPersonManager, self).get_query_set()
        qs.filter(kind=self.kind)

        return qs
