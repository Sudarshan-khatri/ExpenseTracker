from rest_framework.routers import DefaultRouter
from ..viewset.viewsets import ExpenseIncomeViewset


#create router 
expenseIncome_router=DefaultRouter()
expenseIncome_router.register('expenses',ExpenseIncomeViewset)