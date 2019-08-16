from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



def validate_IMO(value):
    try:
        if type(value) is not int:
            raise Exception
        checkSum = value % 10
        rest = value // 10
        cond = 0
        for i in range(6):
            # the imo number must have 7 figures
            if i == 5 and rest == 0:
                raise Exception
            n = rest % 10
            cond += n * (7-i)
            rest = rest // 10
        if cond != checkSum:
            raise Exception
    except:
        raise ValidationError(
            _('%(value)s is not a valid IMO number'),
            params={'value': value},
            code='invalid',
        )
