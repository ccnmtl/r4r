from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from r4r.main.models import Course, Team
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from r4r.main.mixins import IsStaffMixin, IsSuperuserMixin
from r4r.main.serializers import (
    CourseSerializer, TeamSerializer, UserSerializer
)
from r4r.main.permissions import (
    IsSuperuserOrReadOnlyAuth, IsStaffOrReadOnlyAuth,
    DjangoModelPermissionsOrAuthReadOnly
)


class UserViewSet(IsSuperuserMixin, LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperuserOrReadOnlyAuth]

    @action(methods=['GET'], detail=True,
            permission_classes=[DjangoModelPermissionsOrAuthReadOnly])
    def courses(self, request, pk=None):
        courses = self.get_object().course_set.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CourseViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperuserOrReadOnlyAuth]


class TeamViewSet(IsStaffMixin, LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsStaffOrReadOnlyAuth]


class EnsureCsrfCookieMixin(object):
    '''
    Ensures that the CSRF cookie will be passed to the client.
    NOTE:
        This should be the left-most mixin of a view.
    '''

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(EnsureCsrfCookieMixin, self).dispatch(*args, **kwargs)


class BaseView(EnsureCsrfCookieMixin, LoginRequiredMixin, TemplateView):
    template_name = 'main/index.html'
