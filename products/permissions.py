from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.role == 'customer'
    
class IsSeller(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'seller'