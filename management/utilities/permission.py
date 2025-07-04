from rest_framework.permissions import BasePermission



SuperAdmin=1
Admin=2


def IsAuthencticated(request):
    return bool(request.user and request.user.is_authenticated)

#super admin level permission 
def SuperAdminLevel(request):
    return bool(IsAuthencticated(request) and request.user.is_superuser)

#admin level permission 
def AdminLevel(request):
    return bool(IsAuthencticated(request) and request.user.role in [Admin,SuperAdmin])


#owner leve permission
def isOwner(request):
    if str(request.user.id)==str(request.data.get('user')):
        return True
    elif len(request.data)==0 and len(request.POST)==0:
        return True
    
    return False


class ExpenseIncomePermission(BasePermission):
    def  has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action in ['retrieve']:
            return isOwner(request)
        elif view.action in ['create','update']:
            return isOwner(request) 
        elif view.action in ['partial_update']:
            return view.get_object().user_id==request.user.id
        elif view.action in ['destroy']:
            return isOwner(request)
        return super().has_permission(request, view)
