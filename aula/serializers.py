from rest_framework import serializers
from .models import Aula, Ingrediente, AulaIngrediente
from django.db import transaction
from drf_writable_nested import WritableNestedModelSerializer

#from rest_framework.relations import PrimaryKeyRelatedField
#from django.db.models.query import queryset

class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingrediente
        fields = [
            'id_ingrediente',
            'nome_ingrediente',
            'quantidade_calorica_ingrediente',
            'aproveitamento_ingrediente',
            'quantidade_estoque_ingrediente',
            'quantidade_reservada_ingrediente',
            'valor_ingrediente',
            'motivo_retirada_estoque',
        ]




class AulaSerializer(WritableNestedModelSerializer):

    #assigned = serializers.SlugRelatedField(slug_field=Aula.AULA_FIELD, required=False)
    #ingredientes = serializers.PrimaryKeyRelatedField(many=True)
    #ingredientes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #ingredientes = PrimaryKeyRelatedField(many=True, queryset=Ingrediente.objects.all())
    #ingredientes = IngredienteSerializer(many=True, queryset=Ingrediente.objects.all())
    #ingredientes = IngredienteSerializer(many=True, queryset=Ingrediente.objects.all())
    #ingredientes = IngredienteSerializer(many=True)
    #ingredientes = AulaIngredienteSerializer(source='aulaingrediente_set', many=True,)
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Aula
        fields = [
            'id_aula',
            'data_aula',
            'descricao_aula',
            'aula_agendada',
            'aula_concluida',
            'periodo_aula',
            'ingredientes'
        ]




class AulaIngredienteSerializer(WritableNestedModelSerializer):
    #id_aula = AulaSerializer(many=True, read_only=True)
    #id_ingrediente = IngredienteSerializer(many=True, read_only=True)
    #id_aula = AulaSerializer(many=True)
    #ingredientes = IngredienteSerializer(source='ingrediente_set', many=True,)
    #id_ingrediente = serializers.ReadOnlyField(source='ingrediente.id_ingrediente')
    #nome_ingrediente = serializers.ReadOnlyField(source='ingrediente.nome_ingrediente')
    #quantidade_calorica_ingrediente = serializers.ReadOnlyField(source='ingrediente.quantidade_calorica_ingrediente')
    #aproveitamento_ingrediente = serializers.ReadOnlyField(source='ingrediente.aproveitamento_ingrediente')
    #quantidade_estoque_ingrediente = serializers.ReadOnlyField(source='ingrediente.quantidade_estoque_ingrediente')
    #quantidade_reservada_ingrediente = serializers.ReadOnlyField(source='ingrediente.quantidade_reservada_ingrediente')
    #valor_ingrediente = serializers.ReadOnlyField(source='ingrediente.valor_ingrediente')
    #motivo_retirada_estoque = serializers.ReadOnlyField(source='ingrediente.motivo_retirada_estoque')

    class Meta:
        model = AulaIngrediente
        fields = [
            
            'id_aula',
            'id_ingrediente',
            'quantidade_projetada_aula',
            'quantidade_utilizada_aula',
        ]



'''def create (self, validated_data):
    ingredientes = Ingrediente.objects.get(pk=validated_data.pop('ingredientes'))
    instance = Aula.objects.create(**validated_data)
    AulaIngrediente.objects.create(ingredientes=Ingrediente, Aula=Aula)
    return instance

    def to_representation(self, instance):
        representation = super(AulaSerializer, self).to_representation(instance)
        representation['AulaIngrediente'] = AulaIngredienteSerializer(instance.AulaIngrediente_set.all(), many=True).data
        return representation'''


'''def create(self, validated_data):
        order = Order.objects.get(pk=validated_data.pop('event'))
        instance = Equipment.objects.create(**validated_data)
        Assignment.objects.create(Order=order, Equipment=Equipment)
        return insance

    def to_representation(self, instance):
        representation = super(EquipmentSerializer, self).to_representation(instance)
        representation['assigment'] = AssignmentSerializer(instance.assigment_set.all(), many=True).data
        return representation '''

'''def create(self, validated_data):
         ingrediente_data = validated_data.pop('ingredientes')
         aula = Aula.objects.create(**validated_data)
         Ingrediente.objects.create(aula=aula, **ingrediente_data)
         return aula'''



'''class AulaIngredienteSerializer(serializers.ModelSerializer):

     Ingredientes = IngredienteSerializer(many=True, read_only=True)
     Aulas = AulaSerializer(many=True, read_only=True)
  
     class Meta:
         model = AulaIngrediente
         fields = [
             'Aulas',
             'Ingredientes',
             'quantidade_projetada_aula',
             'quantidade_utilizada_aula',
             ]'''


'''def create(self, validated_data):
    Ingredientes_data = validated_data.pop('Ingredientes')
    aula = Aulas.objects.all().create(**validated_data)
    Ingredientes.objects.create(Aulas=aulas, **Ingredientes_data)
    return aula




        

def update(self, instance, validated_data):
        instance.descricao_aula = validated_data.get('descricao_aula', instance.descricao_aula)
        instance.data_aula = validated_data.get('data_aula', instance.data_aula)
        instance.aula_agendada = validated_data.get('aula_agendada', instance.aula_agendada)
        instance.aula_concluida = validated_data.get('aula_concluida', instance.aula_concluida)
        instance.periodo_aula = validated_data.get('periodo_aula', instance.periodo_aula)
        instance.ingrediente = validated_data.get('ingredientes', instance.ingredientes)
        return instance'''



'''class AulaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    class Meta:
        model = Aula
        fields = [
            'id_aula',
            'data_aula',
            'descricao_aula',
            'aula_agendada',
            'aula_concluida',
            'periodo_aula',
            'ingredientes'
        ]'''



'''class AulaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaIngrediente
        fields = [
            'quantidade_projetada_aula',
            'quantidade_utilizada_aula',
        ]'''



'''@transaction.atomic 
def create (self, validated_data):
    aula = Aula.objects.create(**validated_data)
    if "ingredientes" in self.initial_data:
        ingredientes = self.initial_data.get("ingredientes")
        for Ingrediente in ingredientes:
            id = Ingrediente.get("id")
            nome_ingrediente = Ingrediente.get("nome_ingrediente")
            Ingrediente_instance = Ingrediente.objects.get(id=id)
            AulaIngrediente(aula=aula, Ingrediente=Ingrediente_instance, nome_ingrediente=nome_ingrediente).save()
    aula.save()
    return aula'''



'''def update(self, instance, validated_data):
        instance.nome_ingrediente = validated_data.get('nome_ingrediente', instance.nome_ingrediente)
        instance.quantidade_calorica_ingrediente = validated_data.get('quantidade_calorica_ingrediente', instance.quantidade_calorica_ingrediente)
        instance.aproveitamento_ingrediente = validated_data.get('aproveitamento_ingrediente', instance.aproveitamento_ingrediente)
        instance.valor_ingrediente = validated_data.get('valor_ingrediente', instance.valor_ingrediente)
        instance.motivo_retirada_estoque = validated_data.get('motivo_retirada_estoque', instance.motivo_retirada_estoque)
        if validated_data.get('quantidade_estoque_ingrediente') > 0:
            print("SOMANDO")
            instance.quantidade_estoque_ingrediente = validated_data.get('quantidade_estoque_ingrediente') + instance.quantidade_estoque_ingrediente
        elif validated_data.get('quantidade_estoque_ingrediente') < 0:
            instance.quantidade_estoque_ingrediente = instance.quantidade_estoque_ingrediente + validated_data.get('quantidade_estoque_ingrediente')
            if instance.quantidade_estoque_ingrediente < 0:
                print("Estoque negativo")
                raise serializers.ValidationError('O estoque não pode ser negativo')
            else:
                print("SUBTRAINDO")
        else:
            print("EDITANDO")
            quantidade_estoque_ingrediente = validated_data.get('quantidade_estoque_ingrediente', instance.quantidade_estoque_ingrediente)
        instance.save()
        return instance	'''