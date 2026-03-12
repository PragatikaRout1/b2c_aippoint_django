from mongoengine import Document, StringField, DictField, IntField, DateTimeField

import datetime

class ResumeCollection(Document):
    resume_name = StringField(max_length=100)
    resume_data = DictField()
    phone = StringField(max_length=100)
    projects = StringField(max_length=1000)
    name = StringField(max_length=100)
    email = StringField(max_length=100)
    education = StringField(max_length=1000)
    certificates = StringField(max_length=1000)
    work = StringField(max_length=1000)
    experiance = StringField(max_length=1000)
    experience = StringField(max_length=1000)
    file_name = StringField(max_length=1000)
    languages = StringField(max_length=100)
    location = StringField(max_length=100)
    skills = StringField(max_length=1000)
    experiance_in_number = StringField(max_length=1000)
    url = StringField(max_length=100)
    uploaded_by = StringField(max_length=100)
    req_no = StringField(max_length=100)
    reference_number = StringField(max_length=100)
    created_by= StringField(max_length=100)
    Resume_Category=StringField(max_length=100)
    job_role = StringField(max_length=100)
    domain_specific=StringField(max_length=100)


    def __str__(self):
        return self.resume_name

class Counter(Document):
    name = StringField(required=True, unique=True)
    value = IntField(default=0)

    def __str__(self):
        return self.name

class UploadedFiles(Document):
    file_name = StringField(max_length=1000)
    req_no = StringField(max_length=100)
    uploaded_by = StringField(max_length=100)
    duplicate = StringField(max_length=100)
    uploaded_on = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name
    
class UploadRecord(Document):
    ref_num = StringField(max_length=1000)
    input_type = StringField(max_length=1000)
    que_level = StringField(max_length=1000)
    len_que = StringField(max_length=1000)
    resumefile_name = StringField(max_length=1000)
    jdfile_name = StringField(max_length=1000)
    resume_name = StringField(max_length=100)
    resume_data = DictField()
    jd_data = DictField()
    phone = StringField(max_length=100)
    projects = StringField(max_length=1000)
    name = StringField(max_length=100)
    email = StringField(max_length=100)
    education = StringField(max_length=1000)
    certificates = StringField(max_length=1000)
    work = StringField(max_length=1000)
    experiance = StringField(max_length=1000)
    experience = StringField(max_length=1000)
    file_name = StringField(max_length=1000)
    languages = StringField(max_length=100)
    location = StringField(max_length=100)
    skills = StringField(max_length=1000)
    experiance_in_number = StringField(max_length=1000)

    def __str__(self):
         return self.name