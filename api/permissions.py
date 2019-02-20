from rest_framework.permissions import BasePermission

class IsAutherOrStaff(BasePermission):

	message = "You shall not pass!"
	
	def has_object_permission(self, request, view, obj):
		if obj.owner == request.user:
			return True
		return False
