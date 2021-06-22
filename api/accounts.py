from flask import current_app as app
from sqlalchemy.sql import text
from sqlalchemy import distinct,func
import os, time,uuid,re
from time import gmtime, strftime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from models.model import * #Notification,Follows,Users,Story,Posts,Comments,Likes,flags_,Jobs,job_bid,Interests,Share
from flask import (Flask, g, render_template, flash, redirect, url_for, session,request, abort)
from flask_bcrypt import check_password_hash
from flask_login import(LoginManager, login_user, logout_user,login_required, current_user)
from flask_mysqldb import MySQL # sudo apt install default-libmysqlclient-dev  b4 installing flask-mysqldb
from flask_sqlalchemy import SQLAlchemy
from models.model import db
import urllib.request
from sqlalchemy import create_engine, exc,desc,or_,and_
from flask import Flask, request, redirect, jsonify,make_response,json,Blueprint
from werkzeug.utils import secure_filename
from flask_jwt_extended import ( JWTManager, jwt_required, create_access_token,get_jwt_identity)
import datetime
from flask_mail import Mail, Message
from . import mail
from random import *
#from twilio.rest import Client, TwilioException

otp = randint(000000,999999) 
    
current_time = time.localtime()
sasa=time.strftime('%a, %d %b %Y %H:%M:%S GMT', current_time)

accounts_bp = Blueprint('accounts', __name__)

"""

----------------------------- index ---------------------------

"""
@accounts_bp.route('/', methods=('GET', 'POST'))
def index():
        if request.method == 'GET':
          
          return render_template('dashboard.html')



"""

----------------------------- login ---------------------------

"""
@accounts_bp.route('/login', methods=('GET', 'POST'))
def login():
        
         return render_template('login.html')