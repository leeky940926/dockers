from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SigUpnView(APIView):
    def perform_authentication(self, request):
        if not self.request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self, request, *args, **kwargs):

        self.request.session["test"]="gigi"
        print(self.request.session.get("test"))
        return Response(status=status.HTTP_200_OK)

