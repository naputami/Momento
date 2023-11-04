from flask import render_template, redirect
from app.frontend import frontendBp
from dotenv import load_dotenv

import os
load_dotenv()

VUE_BASE_URL = os.getenv('VUE_BASE_URL')

@frontendBp.route("/login")
def login():
    return render_template('/auth/login.html')

@frontendBp.route("/backtoclient")
def back_to_client():
    return redirect(f'{VUE_BASE_URL}/home')
