from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from api.modulos.basicApiView import *
from api.modulos.profissional.serializers import ProfissionalListSerializer, ProfissionalCreateSerializer
from core.models import UserProfile
from core.util.util_manager import get_user_type


class ProfissionalCreateView(IsAutenticatedCreateAPIView):
    serializer_class = ProfissionalCreateSerializer


class ProfissionalListView(IsAutenticatedListApiView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfissionalListSerializer


class ProfissionalGetView(IsAutenticatedApiView):
    def post(self, request):
        print(request.data)
        nomedeusuario = str()
        senha = str()
        try:
            nomedeusuario = request.data['usuario']
            senha= request.data['senha']
        except:
            return Response({"detail": "Usuário ou senha inválido"} , status=status.HTTP_401_UNAUTHORIZED)

        print(str(nomedeusuario) + " + " + str(senha))
        user = authenticate(username=nomedeusuario, password=senha)

        if user is None:
            return Response({"detail": "Usuário ou senha inválido"}, status=status.HTTP_401_UNAUTHORIZED)

        usuario = get_user_type(user)

        return Response(usuario.getJson(), status=status.HTTP_200_OK)

    # def get(self, request, format=None):
    #      print('get')
    #      print(request.data)
    #
    #      return Response({'ok': 'ok'}, status=status.HTTP_200_OK)

#
# # class AnalisyUpdateView(IsAutenticatedUpdateAPIView):
# #     serializer_class = AnalisyCreateSerializer

#class UsuarioTokenGetView(IsAutenticatedApiView):

    #def get(self, request, pk):
        #usuario = Usuario.objects.get(pk)
        #token = usuario.token()
        #return Response(token, status=status.HTTP_200_OK)
