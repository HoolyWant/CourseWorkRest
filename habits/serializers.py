from rest_framework import serializers

from habits.models import Habits
from habits.validators import TimeLimitValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = ['id', 'location', 'time', 'action', 'is_pleasant',
                  'linked', 'period', 'reward', 'limit', 'is_public', 'owner']
        validators = [
            TimeLimitValidator(field='limit'),
        ]
