#  APIの出力をJSON,XMLデータに変換
from rest_framework import serializers
from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match                     # 呼び出すモデル
        fields = ["id", "name", "team_num",
                  "entry_url", "date"]  # API上に表示するモデルのデータ項目

    def create(self, validated_data):
        print(validated_data)
        return Match(**validated_data)
