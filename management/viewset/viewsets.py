from rest_framework import viewsets
from ..models import ExpenseIncome
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from ..utilities.pagination import CustomPagination
from ..utilities.permission import ExpenseIncomePermission
from ..serializer.serializers import ExpenseIncomeListSerializer,ExpenseIncomeRetrieveSerializer,ExpenseIncomeWriteSerializer




class ExpenseIncomeViewset(viewsets.ModelViewSet):
    queryset=ExpenseIncome.objects.all().order_by('-id')
    serializer_class=ExpenseIncomeListSerializer
    permission_classes=[ExpenseIncomePermission]
    # pagination_class=CustomPagination


    def get_serializer_class(self):
        if self.action=='list':
            return ExpenseIncomeListSerializer
        elif self.action in ['create','partial_update','update']:
            return ExpenseIncomeWriteSerializer
        elif self.action == 'retrieve':
            return ExpenseIncomeRetrieveSerializer
        return super().get_serializer_class()
