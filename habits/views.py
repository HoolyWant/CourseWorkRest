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
        if new_habit.is_pleasant and new_habit.reward and new_habit.linked:
            raise "The habit can't be pleasant, if you have reward or related habit"
        if not Habits.objects.get(pk=new_habit.linked_id).is_pleasant:
            raise "A related habit can only be pleasant"

    def get(self, request):
        queryset = Habits.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitsSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)



class HabitsListAPI(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]

class MyPagination(PageNumberPagination):
    page_size = 10  # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества элементов на странице
    max_page_size = 100  # Максимальное количество элементов на странице

# views.py
class MyView(APIView):
    pagination_class = MyPagination

    def get(self, request):
        queryset = MyModel.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = MySerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)