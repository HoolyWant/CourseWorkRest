from rest_framework import serializers


class TimeLimitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if int(tmp_val) > 120:
            raise serializers.ValidationError("The limit can only be less than 120s.")



