from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from r4r.main.models import Case, Course, Prompt, Team, Rotation
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from r4r.main.mixins import IsStaffMixin
from r4r.main.serializers import (
    CourseDetailSerializer, CourseListSerializer, RotationSerializer,
    TeamSerializer, UserSerializer, CaseSerializer, PromptSerializer
)
from r4r.main.permissions import (
    IsSuperuserOrReadOnlyAuth, IsStaffOrReadOnlyAuth
)


class UserViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperuserOrReadOnlyAuth]

    @action(methods=['GET'], detail=True,
            permission_classes=[IsSuperuserOrReadOnlyAuth])
    def courses(self, request, pk=None):
        user = self.get_object()

        #  GET instructor courses
        courses = Course.objects.filter(instructors=user).distinct()
        #  ADD student courses
        courses.union(Course.objects.filter(pk__in=Rotation.objects.filter(
            pk__in=Team.objects.filter(members=user).distinct())))

        serializer = CourseListSerializer(
            courses, many=True, context={'request': request})
        return Response(serializer.data)


class CaseViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [IsStaffOrReadOnlyAuth]


class CourseViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsSuperuserOrReadOnlyAuth]

    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseListSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


class RotationViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    queryset = Rotation.objects.all()
    serializer_class = RotationSerializer
    permission_classes = [IsSuperuserOrReadOnlyAuth]


class PromptViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsStaffOrReadOnlyAuth]


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
