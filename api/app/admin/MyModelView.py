from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, render_template
from werkzeug.security import generate_password_hash
from flask_admin import AdminIndexView
from dotenv import load_dotenv
import os
load_dotenv()

FLASK_BASE_URL = os.getenv('FLASK_BASE_URL')

class CustomModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)
    
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(f'{FLASK_BASE_URL}/login')
        # return render_template('admin/inaccessible.html')

class AdminModelView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(f'{FLASK_BASE_URL}/login')
        # return render_template('admin/inaccessible.html')