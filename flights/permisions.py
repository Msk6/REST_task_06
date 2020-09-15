from rest_framework import permissions
from django.utils import timezone
import datetime
class IsBookingOwner(permissions.BasePermission):
    message = 'OOOOOPS'

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.user:
            return True
        else:
            return False


class IsFar(permissions.BasePermission):
    message = 'Your booking not far enugh'

    def has_object_permission(self, request, view, obj):
        '''if (obj.date - timezone.now().date()).days > 3:
            return True
        else:
            return False'''

        if (obj.date - datetime.date.today()).days > 3:
            return True
        else:
            return False
