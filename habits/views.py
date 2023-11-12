from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habits.models import Habits
from habits.pagination import MyPagination
from habits.serializers import HabitsSerializer


class HabitsViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        new_habit = serializer.save()
        if (new_habit.is_pleasant and new_habit.reward is not None or
                new_habit.is_pleasant and new_habit.linked is not None):
            raise "The habit can't be pleasant, if you have reward or related habit"
        new_habit.user = self.request.user

        new_habit.save()

    def get_queryset(self):
        user = self.request.user
        return Habits.objects.filter(owner=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id == instance.owner_id:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def perform_update(self, serializer):
        updated_habit = serializer.save()
        if updated_habit.owner == self.request.user:
            updated_habit.save()
        else:
            raise "You dont have permissions to do this"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.id == instance.owner_id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class HabitsListAPI(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
