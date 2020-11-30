from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView


class IsAutenticatedListApiView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    pass
class IsAutenticatedCreateAPIView(CreateAPIView):
    # permission_classes = (IsAuthenticated,)
    pass

class IsAutenticatedUpdateAPIView(UpdateAPIView):
    # permission_classes = (IsAuthenticated,)
    pass

class IsAutenticatedApiView(APIView):
    # permission_classes = (IsAuthenticated,)
    pass

