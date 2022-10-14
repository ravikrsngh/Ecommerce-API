from rest_framework import permissions



SAFE_METHODS = ['POST','PUT','DELETE']
class SafeMethodsRequestPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """
    def has_permission(self, request, view):
        if ((request.method in SAFE_METHODS and
            request.user and
            request.user.is_authenticated) or request.method=='GET' ):
            return True
        return True
