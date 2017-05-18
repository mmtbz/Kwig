__author__ = 'Dave'
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):

    def __init__(self, for_field=None, *args, **kwargs):
        self.for_field=for_field
        super(OrderField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            # no current value
            try:
                qs = self.model.objects.all()
                # qs = self.model.objects.all()
                if self.for_field:
                    # filter by fields with the same field values
                    # for fields in "for_fields"
                    query = {field: getattr(model_instance, field) for field in self.for_field}
                    qs = qs.filter(**query)
                    # get order of the last item
                    last_item = qs.latest(self.attname)
                    value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(OrderField, self).pre_save(model_instance, add)