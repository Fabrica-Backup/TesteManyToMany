from django.shortcuts import render


from .serializers import AulaSerializer, IngredienteSerializer, AulaIngredienteSerializer
from .models import Aula, Ingrediente, AulaIngrediente

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.relations import PrimaryKeyRelatedField
#from django.db.models.query import queryset


class CreateAula(APIView):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    #permission_classes = (IsAuthenticated,)
    

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAula(APIView):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        serializer = self.serializer_class(Aula.objects.all(), many=True)
        return Response(serializer.data)


class EditAula(APIView):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Aula.objects.get(id_aula=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(Aula.objects.get(id_aula=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAula(APIView):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Aula.objects.get(id_aula=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        Aula.objects.get(id_aula=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class CreateIngrediente(APIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    #permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListIngrediente(APIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    #permission_classes = (IsAuthenticated,)
    
    
    def get(self, request, format=None):
        serializer = self.serializer_class(Ingrediente.objects.all(), many=True)
        return Response(serializer.data)


class EditIngrediente(APIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Ingrediente.objects.get(id_ingrediente=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(Ingrediente.objects.get(id_ingrediente=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteIngrediente(APIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        serializer = self.serializer_class(Ingrediente.objects.get(id_ingrediente=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        Ingrediente.objects.get(id_ingrediente=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class CreateAulaIngrediente(APIView):
    queryset = AulaIngrediente.objects.all()
    serializer_class = AulaIngredienteSerializer
    #permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAulaIngrediente(APIView):
    queryset = AulaIngrediente.objects.all()
    serializer_class = AulaIngredienteSerializer
    #permission_classes = (IsAuthenticated,)
    
    
    def get(self, request, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.all(), many=True)
        return Response(serializer.data)


class EditAulaIngrediente(APIView):
    queryset = AulaIngrediente.objects.all()
    serializer_class = IngredienteSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAulaIngrediente(APIView):
    queryset = AulaIngrediente.objects.all()
    serializer_class = AulaIngredienteSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        AulaIngrediente.objects.get(id_aula_ingrediente=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''class CreateAulaIngrediente(APIView):
    serializer_class = AulaIngredienteSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAulaIngrediente(APIView):
    serializer_class = AulaSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.all(), many=True)
        return Response(serializer.data)


class EditAulaIngrediente(APIView):
    serializer_class = AulaSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAulaIngrediente(APIView):
    serializer_class = AulaIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        AulaIngrediente.objects.get(id_aula_ingrediente=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''


'''class CreateAulaIngrediente(APIView):
    serializer_class = AulaIngredienteSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ListAulaIngrediente(APIView):
    serializer_class = AulaIngredienteSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.all(), many=True)
        return Response(serializer.data)


class EditAulaIngrediente(APIView):
    serializer_class = AulaIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id))
        return Response(serializer.data)

    def put(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
''
class DeleteAulaIngrediente(APIView):
    serializer_class = AulaIngredienteSerializer

    def get(self, request, id, format=None):
        serializer = self.serializer_class(AulaIngrediente.objects.get(id_aula_ingrediente=id))
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        AulaIngrediente.objects.get(id_aula_ingrediente=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

