
from flask import current_app as app
from flask import g , Flask, jsonify, url_for
import time
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from flask_login import UserMixin,LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


login_manager = LoginManager()
db = SQLAlchemy()
db.init_app(app)
login_manager.init_app(app)


class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    businessname = db.Column(db.VARCHAR(200))
    Student_id = db.Column(db.VARCHAR(200))
    Employee_id = db.Column(db.VARCHAR(200))
    present =db.Column(db.VARCHAR(200))
    Absent = db.Column(db.VARCHAR(200))     
    status = db.Column(db.Integer, default=0)
    content = db.Column(db.VARCHAR(2000), nullable=True)
    timestamp = db.Column(db.VARCHAR(200))
    






################################## businesss ###################################
#businesss Registration
class business_status:
    active:0
    deleted: 1
    blocked: 2

class business( db.Model, UserMixin):
    """ 
    business Model for storing business related details 
    """
  
    
    __tablename__ = "business"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    businessname = db.Column(db.VARCHAR(200))
    businessemail = db.Column(db.VARCHAR(200), unique=True, nullable=False)
    businesscontact = db.Column(db.VARCHAR(200), unique=True)
    businesscontact1 = db.Column(db.VARCHAR(200), unique=True)
    
    authenticated = db.Column(db.Boolean, default=False) 
    businesscategory = db.Column(db.VARCHAR(200))
    businesslocation = db.Column(db.VARCHAR(200))
    
    registered_on = db.Column(db.VARCHAR(200))
    last_seen  = db.Column(db.VARCHAR(200))
    admin1 = db.Column(db.VARCHAR(200))
    admin2  = db.Column(db.VARCHAR(200))
    admin3  = db.Column(db.VARCHAR(200))
    logo_url = db.Column(db.VARCHAR(200), nullable=True)

    status = db.Column(db.Integer, default=0)
    businessdsc = db.Column(db.VARCHAR(500))   
    is_active = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all businesss are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the business is authenticated."""
        return self.authenticated 

    def is_anonymous(self):
        """False, as anonymous businesss aren't supported."""
        return False

   

    @login_manager.user_loader
    def get_user(user_id):
        try:
           return Users.query.get(int(id))
        except:
           return None

    

    def to_json(self):
        if  not self.logo_url :
            logo_url =  ('static/images/default/default.jpg')
        elif  self.logo_url:
            logo_url =self.logo_url
        json_business = {  
            'logo': logo_url,
            'businessname':self.businessname,
            'businessemail':self.businessemail,
            'businessscontact':self.businesscontact,
            'businesslocation':self.businesslocation,
            'businessstype':self.businesstype,
            'businessscategory':self.businesscategory,
            'businessid':self.id,
            'registered_on': self.registered_on,
            'last_seen': self.last_seen,
            
            'business_profile': url_for('business.get_business',businessname = self.businessname),
            
            }

        return jsonify(json_business)
   



################################# Employees ###########################################################
#employee Registration
class user_status:
    active:0
    deleted: 1
    blocked: 2

class Employees( db.Model, UserMixin):
    """  
    user Model for storing user related details 
    """
  
    
    __tablename__ = "Employees"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    Employee_name = db.Column(db.VARCHAR(200))
    Employee_contact = db.Column(db.VARCHAR(300))
    Employee_id = db.Column(db.VARCHAR(300))
    Employee_email = db.Column(db.VARCHAR(300))
    Health_conditions = db.Column(db.VARCHAR(200))
    registered_on = db.Column(db.VARCHAR(200))
    last_seen  = db.Column(db.VARCHAR(200))
    Position = db.Column(db.String(300))
    Position1 = db.Column(db.String(300))
    Position2 = db.Column(db.String(300))
    Position3 = db.Column(db.String(300))
    Qualification = db.Column(db.String(300))
    Qualification1 = db.Column(db.String(300))
    Qualification2 = db.Column(db.String(300))
    Qualification3 = db.Column(db.String(300))
    image_url = db.Column(db.VARCHAR(200), nullable=True)
    status = db.Column(db.Integer, default=0)
    Position2 = db.Column(db.VARCHAR(300))
    Next_ofkin_name = db.Column(db.VARCHAR(200))
    Next_ofkin_contact = db.Column(db.VARCHAR(300))
    Next_ofkin_id = db.Column(db.VARCHAR(300))
    Next_ofkin_email = db.Column(db.VARCHAR(300))

    

    
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def load_user(id):
        return users(id)

  
     
    def to_json(self):
        if  not self.image_url :
            image_url =  ('static/images/default/default.jpg')
        elif  self.image_url:
             image_url =self.image_url
        json_student = {  
            'profile_image': image_url,
            'Employee_name':self.Employee_name,
            'Employee_email':self.Employee_email,
            'Employee_contact':self.Employee_contact,
            'Employee_name':self.Employee_name,
            'Employee_id':self.Employee_id,
            
            'Health_conditions':self.Health_conditions,
            'Position':self.Position,
            'Position1':self.Position1,
            'Position2':self.Position2,
            'Position3':self.Position3,

            'Qualification':self.Qualification,
            'Qualification1':self.Qualification1,
            'Qualification2':self.Qualification2,
            'Qualification3':self.Qualification3,
            
            'Next_ofkin_email':self.Next_ofkin_email,
            'Next_ofkin_contact':self.Next_ofkin_contact,
            'Next_ofkin_name':self.Next_ofkin_name,
            'Next_ofkin_id':self.Next_ofkin_id,

            

            'Employee_id':self.id,
            'registered_on': self.registered_on,
            'last_seen': self.last_seen,
            
            'Employee_profile': url_for('accounts.get_user',user_id = self.id),
            'status': 200
            }

        return jsonify(json_user)


################################## Students###################################
#users Registration
class user_status:
    active:0
    deleted: 1
    blocked: 2

class Students( db.Model, UserMixin):
    """  
    user Model for storing user related details 
    """
  
    
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    Student_name = db.Column(db.VARCHAR(200))
    D_O_B = db.Column(db.VARCHAR(200))
    Admission_no = db.Column(db.VARCHAR(200), unique=True)
    Class_admitted = db.Column(db.VARCHAR(200))
    Current_class = db.Column(db.VARCHAR(200))
    Health_conditions = db.Column(db.VARCHAR(200))
    registered_on = db.Column(db.VARCHAR(200))
    last_seen  = db.Column(db.VARCHAR(200))
    Position = db.Column(db.String(300))
    image_url = db.Column(db.VARCHAR(200), nullable=True)
    status = db.Column(db.Integer, default=0)

    Mother_name = db.Column(db.VARCHAR(300))
    Mother_contact = db.Column(db.VARCHAR(300))
    Mother_id = db.Column(db.VARCHAR(300))
    Mother_email = db.Column(db.VARCHAR(300))

    Father_name = db.Column(db.VARCHAR(300))
    Father_contact = db.Column(db.VARCHAR(300))
    Father_id = db.Column(db.VARCHAR(300))
    Father_email = db.Column(db.VARCHAR(300))

    Gurdian_name = db.Column(db.VARCHAR(300))
    Gurdian_contact = db.Column(db.VARCHAR(300))
    Gurdian_id = db.Column(db.VARCHAR(300))
    Gurdian_email = db.Column(db.VARCHAR(300))

    
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def load_user(id):
        return users(id)

  
     
    def to_json(self):
        if  not self.image_url :
            image_url =  ('static/images/default/default.jpg')
        elif  self.image_url:
             image_url =self.image_url
        json_student = {  
            'profile_image': image_url,
            'Student_name':self.Student_name,
            'D.O.B':self.D.O.B,
            'Health_conditions':self.Health_conditions,
            'Grade':self.Grade,
            'Class_admitted':self.Class_admitted,
            'Current_class': self.Current_class,

            'Gurdian_email':self.Gurdian_email,
            'Gurdian_contact':self.Gurdian_contact,
            'Gurdian_name':self.Gurdian_name,
            'Gurdian_id':self.Gurdian_id,

            'Father_email':self.Father_email,
            'Father_contact':self.Father_contact,
            'Father_name':self.Father_name,
            'Father_id':self.Father_id,


            'Mother_email':self.Mother_email,
            'Mother_contact':self.Mother_contact,
            'Mother_name':self.Mother_name,
            'Mother_id':self.Mother_id,

            'Student_id':self.id,
            'registered_on': self.registered_on,
            'last_seen': self.last_seen,
            
            'Student_profile': url_for('accounts.get_user',user_id = self.id),
            'status': 200
            }

        return jsonify(json_user)
    

    
################################### events ########################################################
class Performance(db.Model):
   
    __tablename__ = 'performance'
    id = db.Column(db.Integer, primary_key=True)
    Asscessment = db.Column(db.VARCHAR(200))
    Student_id = db.Column(db.VARCHAR(200))

    Grade = db.Column(db.VARCHAR(200))
    Subject= db.Column(db.VARCHAR(200))
    Strand= db.Column(db.VARCHAR(200))
    Sub_strand = db.Column(db.VARCHAR(200))
    Score = db.Column(db.VARCHAR(200))
    Level = db.Column(db.VARCHAR(200))
    
    status = db.Column(db.Integer, default=0)
    timestamp =db.Column(db.VARCHAR(200))
    author_id = db.Column(db.VARCHAR(200))
   
    
    image_url = db.Column(db.VARCHAR(200))
    image_url1 = db.Column(db.VARCHAR(200))
    image_url2 = db.Column(db.VARCHAR(200)) 
    image_url3 = db.Column(db.VARCHAR(200))
    image_url4 = db.Column(db.VARCHAR(200))

    def performance_json(self):
         
        if self.status is not None:
            performance = Performance.query.filter_by(id = self.id).first()
            json_performance = {
                'performance_id':self.id,
                'Accesment_url': url_for('Accesment.get_accessment',acessment_id=self.id), 
                'Accesment':self.Asscessment,               
                'Grade' : self.Grade,                 
                'Subject' : self.Subject, 
                'Strand': self.Strand,
                'Sub_strand': self.Sub_strand,
                'Score':self.Score,
                'Level':self.Level,
                'image_url':self.image_url,
                'status': 200
            }
            return json_transaction
            




################################# transactions ###########################################################

class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    Transaction_id = db.Column(db.VARCHAR(200))
    Sent_from = db.Column(db.VARCHAR(200))
    Sent_to = db.Column(db.VARCHAR(200))
    Payment_method = db.Column(db.VARCHAR(200))
    Ammount = db.Column(db.VARCHAR(200))   
    Paid_for= db.Column(db.VARCHAR(200))
    Timestamp = db.Column(db.VARCHAR(200))
    Status = db.Column(db.Integer)

   
   
    def transaction_json(self):
         
         if self.Status is not None:
            transaction = Transactions.query.filter_by(id = self.Transaction_id).first()
            json_transaction = {
                'transaction_id':self.transaction_id,
                'transaction_url': url_for('Transactions.get_transaction',transaction_id=self.transaction_id),                
                'ammount' : self.Ammount,                 
                'paid_for' : self.paid_for, 
                'sent_to': self.sent_to,
                'Paid_from': self.Sent_from,
                'status': 200
            }
            return json_transaction
            
 

################################# Notifications ###########################################################
#drop column status from database

current_time = time.localtime()
sasa=time.strftime('%a, %d %b %Y %H:%M:%S GMT', current_time)

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.VARCHAR(200))
    student_id = db.Column(db.VARCHAR(200))
    timestamp = db.Column(db.VARCHAR(200), index=True, default=time)
    employee_id = db.Column(db.VARCHAR(200))
    message =db.Column(db.VARCHAR(400))
    data_url = db.Column(db.VARCHAR(200))
    user_data_url = db.Column(db.VARCHAR(200))
    status_code = db.Column(db.VARCHAR(200))
   
    def to_json(self):
         json_note = {
                "status": 200,
                "notification_id" : self.id,
                "message": self.message,
                "author_id" : self.author,
                "timestamp": self.timestamp,
                'data_url' : self.data_url,
                'user_url': url_for('accounts.get_user',user_id =self.user),
                "status_code" : self.status_code
                   }
         return json_note




