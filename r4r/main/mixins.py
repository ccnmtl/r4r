from django.contrib.auth.mixins import UserPassesTestMixin


class IsSuperuserMixin(UserPassesTestMixin):
    """
    Only Superusers can access this
    """

    def test_func(self):
        return self.request.user.is_superuser


class IsStaffMixin(UserPassesTestMixin):
    """
    Only Staff can access this
    """

    def test_func(self):
        return self.request.user.is_staff
