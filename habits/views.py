from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.permissions import ViewSetPermission
from habits.serializers import HabitsSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (ViewSetPermission, )

    def perform_create(self, serializer):
        new_habit = serializer.save()
        if new_habit.is_pleasant and new_habit.reward and new_habit.linked:
            raise "The habit can't be pleasant, if you have reward or related habit"
        if not Habits.objects.get(pk=new_habit.linked_id).is_pleasant:
            raise "A related habit can only be pleasant"



class HabitsListAPI(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]

