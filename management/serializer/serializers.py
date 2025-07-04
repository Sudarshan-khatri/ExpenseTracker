from rest_framework import serializers
from ..models import ExpenseIncome



#Make the list serializer that help to get all the data
class ExpenseIncomeListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseIncome
        fields='__all__'


#Retriece the data 
class ExpenseIncomeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseIncome
        fields=[ 'title','description','amount']

#write serializer
class ExpenseIncomeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseIncome
        fields='__all__'


    