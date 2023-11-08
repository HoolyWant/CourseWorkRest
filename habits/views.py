from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.pagination import MyPagination
from habits.permissions import ViewSetPermission
from habits.serializers import HabitsSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (ViewSetPermission, )

    def perform_create(self, serializer):
        new_habit = serializer.save()
        if new_habit.is_pleasant and new_habit.reward is not None or new_habit.is_pleasant and new_habit.linked is not None:
            raise "The habit can't be pleasant, if you have reward or related habit"
        new_habit.user = self.request.user

        new_habit.save()

    def get_queryset(self):
        user = self.request.user
        return Habits.objects.filter(owner=user)


class HabitsListAPI(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]


