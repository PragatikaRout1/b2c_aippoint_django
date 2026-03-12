from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
import moviepy.editor as mp 
import speech_recognition as sr 
from rest_framework_mongoengine import generics
from .models import ResumeCollection, UploadRecord
from .models import Counter
from .serializers import ResumeCollectionSerializer
from mongoengine import Q
from mongoengine.errors import ValidationError
from django.conf import settings
from django.db.models import Count
import logging
from pymongo import MongoClient
from django.shortcuts import render
import nltk
from django.utils.timezone import now, timedelta
from bson import ObjectId
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

# download pdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

import requests
import textwrap
from .tasks import calculate_score_new, celery_coding_question, celery_upload_interview_data, process_videos_task
import mysql.connector
from django.db import connection
from pymongo.collation import Collation

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ResumeCollectionSerializer
import google.generativeai as genai
import re
from .tasks import celery_upload_interview_data,get_matching_resumes_with_scores,process_job_description

logger = logging.getLogger(__name__)
import pymongo
import time
import os
import json
import base64
from .tasks import celery_upload_interview_data
from .tasks import celery_upload_file
from .tasks import update_answer
from docx import Document
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import tempfile
import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips
import io
import time
import shutil
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from moviepy.editor import VideoFileClip, concatenate_videoclips
logging.basicConfig(level=logging.INFO) 

import urllib.parse

# MongoDB credentials from environment variables
mongo_username = os.getenv("MONGO_USERNAME", "admin")
mongo_password = os.getenv("MONGO_PASSWORD", "")
if not mongo_password:
    password = os.getenv("MONGO_PASSWORD_PLAIN", "")
    mongo_password = urllib.parse.quote(password, safe='')

def validate_object_id(object_id):
    # Use a regular expression to check if the provided ID is a valid 24-character hex string
    if not re.match(r'^[0-9a-fA-F]{24}$', object_id):
        raise ValidationError("Invalid ObjectId format")

# Configure Google Generative AI
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key:
    genai.configure(api_key=google_api_key)

# Helper function to format text
def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Database connection
client = MongoClient(f"mongodb://{mongo_username}:{mongo_password}@192.168.0.16:27017/")
 
db = client["resume_parser"]

# Add any additional views as needed
def index(request):
    """Simple index view"""
    return JsonResponse({"message": "Resume Parser API is running"})

# Placeholder views for URL configuration
def upload_file(request):
    return JsonResponse({"message": "upload_file placeholder"})

def resume_scoring(request):
    return JsonResponse({"message": "resume_scoring placeholder"})

def get_resume(request):
    return JsonResponse({"message": "get_resume placeholder"})

def get_resume_count(request):
    return JsonResponse({"message": "get_resume_count placeholder"})

def score_resumes_by_new_jd(request):
    return JsonResponse({"message": "score_resumes_by_new_jd placeholder"})

def get_resume_by_jd(request):
    return JsonResponse({"message": "get_resume_by_jd placeholder"})

def score_resumes_by_new_resume(request):
    return JsonResponse({"message": "score_resumes_by_new_resume placeholder"})

def get_resume_upload_status(request):
    return JsonResponse({"message": "get_resume_upload_status placeholder"})

def upload_data(request):
    return JsonResponse({"message": "upload_data placeholder"})

def get_interview_data(request):
    return JsonResponse({"message": "get_interview_data placeholder"})

def get_fiveinterview_data(request):
    return JsonResponse({"message": "get_fiveinterview_data placeholder"})

def get_all_interview_data(request):
    return JsonResponse({"message": "get_all_interview_data placeholder"})

def generate_feedback(request):
    return JsonResponse({"message": "generate_feedback placeholder"})

def video_to_text(request):
    return JsonResponse({"message": "video_to_text placeholder"})

def generate_pdf(request, ref_num):
    return JsonResponse({"message": f"generate_pdf placeholder for {ref_num}"})

def update_answer_handler(request):
    return JsonResponse({"message": "update_answer_handler placeholder"})

def generate_skills(request):
    return JsonResponse({"message": "generate_skills placeholder"})

def get_skill_scores(request):
    return JsonResponse({"message": "get_skill_scores placeholder"})

def extract_job_description(request):
    return JsonResponse({"message": "extract_job_description placeholder"})

def get_matching_resumes_count(request):
    return JsonResponse({"message": "get_matching_resumes_count placeholder"})

def get_matching_resumes(request):
    return JsonResponse({"message": "get_matching_resumes placeholder"})

def resume_scoring_for_jd(request):
    return JsonResponse({"message": "resume_scoring_for_jd placeholder"})

def count_scored_resumes_for_jd(request):
    return JsonResponse({"message": "count_scored_resumes_for_jd placeholder"})

def jd_upload(request):
    return JsonResponse({"message": "jd_upload placeholder"})

def extract_techskills_scores(request):
    return JsonResponse({"message": "extract_techskills_scores placeholder"})

def extract_strengths_areas_improvements(request):
    return JsonResponse({"message": "extract_strengths_areas_improvements placeholder"})

def extract_soft_skills(request):
    return JsonResponse({"message": "extract_soft_skills placeholder"})

def analyze_questions(request):
    return JsonResponse({"message": "analyze_questions placeholder"})

def warning_message_count(request):
    return JsonResponse({"message": "warning_message_count placeholder"})

def extract_techskills_scores_coding(request):
    return JsonResponse({"message": "extract_techskills_scores_coding placeholder"})

def extract_strengths_areas_improvements_coding(request):
    return JsonResponse({"message": "extract_strengths_areas_improvements_coding placeholder"})

def extract_soft_skills_coding(request):
    return JsonResponse({"message": "extract_soft_skills_coding placeholder"})

def analyze_questions_coding(request):
    return JsonResponse({"message": "analyze_questions_coding placeholder"})

def generate_feedback_coding(request):
    return JsonResponse({"message": "generate_feedback_coding placeholder"})

def generate_job_description(request):
    return JsonResponse({"message": "generate_job_description placeholder"})

def merge_videos(request):
    return JsonResponse({"message": "merge_videos placeholder"})

def save_eye_tracking_results(request):
    return JsonResponse({"message": "save_eye_tracking_results placeholder"})

def save_noise_detection_results(request):
    return JsonResponse({"message": "save_noise_detection_results placeholder"})

def save_voice_analysis_results(request):
    return JsonResponse({"message": "save_voice_analysis_results placeholder"})

def save_multiple_face_analysis(request):
    return JsonResponse({"message": "save_multiple_face_analysis placeholder"})

def coding_questions(request):
    return JsonResponse({"message": "coding_questions placeholder"})

def assess_code(request):
    return JsonResponse({"message": "assess_code placeholder"})

def check_analysis(request):
    return JsonResponse({"message": "check_analysis placeholder"})

def generate_analytics_pdf(request):
    return JsonResponse({"message": "generate_analytics_pdf placeholder"})
