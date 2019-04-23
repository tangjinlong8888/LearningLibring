from rest_framework import serializers

from good.models import Good


class GoodSerializers(serializers.ModelSerializer):

    class Meta:
        model = Good
        # exclude = ('create_time','title')
        exclude = ('id',)
