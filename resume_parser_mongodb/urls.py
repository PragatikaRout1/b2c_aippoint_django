"""
URL configuration for resume_parser_mongodb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resume_parser import views

from django.conf import settings
from django.conf.urls.static import static
from resume_parser.views import jd_upload

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('get_score/', views.resume_scoring, name='resume_scoring'),
    path('get_resume/', views.get_resume, name='get_resume'),  
    path('get_resume_count/', views.get_resume_count, name='get_resume_count'),
    path('new_jd/', views.score_resumes_by_new_jd, name='score_resumes_by_new_jd'),
    path('get_jd_score/', views.get_resume_by_jd, name='get_resume_by_jd'),
    path('new_resume/', views.score_resumes_by_new_resume, name='score_resumes_by_new_resume'),
    path('resume_upload_status/', views.get_resume_upload_status, name='get_resume_upload_status'),
    path('question_generation/', views.upload_data, name='upload_data'),
    path('get_interview/', views.get_interview_data, name='get_interview_data'),
    path('get_fiveinterview/', views.get_fiveinterview_data, name='get_fiveinterview_data'),
    path('get_all_interview_data/', views.get_all_interview_data, name='get_all_interview_data'),
    path('generate_feedback/', views.generate_feedback, name='generate_feedback'),
    path('extract_answer/', views.video_to_text, name='video_to_text'),
    path('generate_pdf/<str:ref_num>/', views.generate_pdf, name='generate_pdf'),
    path('update_answer/', views.update_answer_handler, name='update_answer'),
    path('generate-skills/', views.generate_skills, name='generate_skills'),
    path('get_skill_scores/', views.get_skill_scores, name='get_skill_scores'),
    path('extract-job-description/', views.extract_job_description, name='extract_job_description'),
    path("matching-resumes-count/", views.get_matching_resumes_count, name="get_matching_resumes_count"),
    path('matching-resumes/', views.get_matching_resumes, name='get_matching_resumes'),
    path("resume_scoring/", views.resume_scoring_for_jd, name="resume_scoring_for_jd"),
    path("count_scored_resumes_for_jd/", views.count_scored_resumes_for_jd, name="count_scored_resumes_for_jd"),

 
    path('extract-techskills-scores/', views.extract_techskills_scores, name='extract_techskills_scores'),
    # path("extract_top5_skills/", views.extract_top5_skills, name="extract_top5_skills"),
    path("extract_strengths_areas/", views.extract_strengths_areas_improvements, name="extract_strengths_areas_improvements"),
    path("extract_soft_skills/", views.extract_soft_skills, name="extract_soft_skills"),
    path('analyze_questions/', views.analyze_questions, name='analyze_questions'),
    path("warning_message_count/", views.warning_message_count, name="warning_message_count"),
    
    path('extract-techskills-scores-coding/', views.extract_techskills_scores_coding, name='extract_techskills_scores_coding'),
    path("extract_strengths_areas_coding/", views.extract_strengths_areas_improvements_coding, name="extract_strengths_areas_improvements_coding"),
    path("extract_soft_skills_coding/", views.extract_soft_skills_coding, name="extract_soft_skills_coding"),
    path('analyze_questions_coding/', views.analyze_questions_coding, name='analyze_questions_coding'),
    path('generate_feedback_coding/', views.generate_feedback_coding, name='generate_feedback_coding'),

    path('generate_job_description/', views.generate_job_description, name='generate_job_description'),
    path("jd_upload/", jd_upload, name="jd_upload"),
    # ne
    path('merge_videos/', views.merge_videos, name='merge_videos'),
    path('save_eye_tracking_results/', views.save_eye_tracking_results, name='save_eye_tracking_results'),
    path('save_noise_detection_results/', views.save_noise_detection_results, name='save_noise_detection_results'),
    path('save_voice_analysis_results/', views.save_voice_analysis_results, name='save_voice_analysis_results'),
    path('save_multiple_face_analysis/', views.save_multiple_face_analysis, name='save_multiple_face_analysis'),

    path('coding_questions/', views.coding_questions, name='coding_questions'),
    path('assess/', views.assess_code, name='assess_code'),
    path('check-analysis/', views.check_analysis, name='fetch_existing_analysis'),

    path('generate_analytics_pdf/', views.generate_analytics_pdf, name='generate_analytics_pdf'),
 
 

    
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)