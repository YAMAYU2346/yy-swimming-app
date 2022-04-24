from fcntl import DN_DELETE
from .models import Match                       # モデル呼出
from rest_framework.generics import ListCreateAPIView    # API
from .serializers import MatchSerializer                # APIで渡すデータをJSON,XML変換

class api(ListCreateAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = Match.objects.all()

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = MatchSerializer

    # 認証
    permission_classes = []