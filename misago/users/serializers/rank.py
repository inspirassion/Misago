from rest_framework import serializers

from misago.core.utils import format_plaintext_for_html
from misago.users.models import Rank


class RankSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Rank
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'title',
            'css_class',
            'is_default',
            'is_tab',
        ]

    def get_description(self, obj):
        if obj.description:
            return format_plaintext_for_html(obj.description)
        else:
            return ''
