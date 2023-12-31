from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect
from werkzeug.security import generate_password_hash
from flask_admin import AdminIndexView


FLASK_BASE_URL = "http://localhost:8000"

class CustomModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(f'{FLASK_BASE_URL}/login')

class AdminModelView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(f'{FLASK_BASE_URL}/login')
