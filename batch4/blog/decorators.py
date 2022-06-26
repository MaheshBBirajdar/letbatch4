from django.http import HttpResponse 

def allowed_user(allowed_roles=[]):  # allowd_rules = ["read"], ['write'], ['read', write]
	def decorator(view_func):
		def wrapper_func(request,*args,**kwargs):
			group = None 
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request,*args,**kwargs)
			else:
				return HttpResponse("<h1>You are Authorized</h1>")

		return wrapper_func

	return decorator