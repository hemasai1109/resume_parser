from genericpath import exists
import pandas as pd
import base64,random
import time,datetime
import en_core_web_sm
from pyresparser import ResumeParser
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import TextConverter
import io,random
import PyPDF2
import os
import csv
import textwrap


from PyPDF2 import PdfFileReader

pdfFileObj = open('example.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages=pdfReader.numPages
# n=0
# text=''
# for n in range(0,pages):
    
#     pageObj = pdfReader.getPage(n)
#     text += pageObj.extractText()
#     n=n+1
# print(text)
# pdfFileObj.close()

def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            print(page)
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    return text









# path = 'C:\pandu\SEMESTER II\Projects\RESUME PARSER\example.pdf'
path = input("Enter path  for Resume/CV")
data = ResumeParser(path).get_extracted_data()
# print(data)
cand_level = ''
if pages == 1:
    cand_level="Beginner"
elif pages==2:
    cand_level="Intermediate"
elif  pages>=3 :
    cand_level="Advanced"
    
    
print(f"You are at {cand_level} level")


ds_keyword = ['tensorflow','keras','pytorch','machine learning','deep Learning','flask','streamlit']
web_keyword = ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress','javascript', 'angular js', 'c#', 'flask']
android_keyword = ['android','android development','flutter','kotlin','xml','kivy']
ios_keyword = ['ios','ios development','swift','cocoa','cocoa touch','xcode']
uiux_keyword = ['ux','adobe xd','figma','zeplin','balsamiq','ui','prototyping','wireframes','storyframes','adobe photoshop','photoshop','editing','adobe illustrator','illustrator','adobe after effects','after effects','adobe premier pro','premier pro','adobe indesign','indesign','wireframe','solid','grasp','user research','user experience']


recommended_skills = []
i=0

for i in data['skills']:
    
    if i.lower() in ds_keyword:
        print(i.lower())
        reco_field = 'Data Science'
        print("\n Our analysis tells that You are looking for data science jobs")
        recommended_skills = ['Data Visualization','Predictive Analysis','Statistical Modeling','Data Mining','Clustering & Classification','Data Analytics','Quantitative Analysis','Web Scraping','ML Algorithms','Keras','Pytorch','Probability','Scikit-learn','Tensorflow',"Flask",'Streamlit']
        print("\n Our algorithm generated some skills for you :")
        for x in range(len(recommended_skills)):
            print(recommended_skills[x],)
    elif i.lower() in web_keyword:
        print(i.lower())
        reco_field = 'Web Development'
        print("\n Our analysis tells that You are looking for WebDeveloper jobs")
        recommended_skills = ['React','Django','Node JS','React JS','php','laravel','Magento','wordpress','Javascript','Angular JS','c#','Flask','SDK']
        print("\n Our algorithm generated some skills for you :")
        for x in range(len(recommended_skills)):
            print(recommended_skills[x],)
        
    elif i.lower() in android_keyword:
        print(i.lower())
        reco_field = 'Android Development'
        print("\n Our analysis tells that You are looking for Android Developer jobs")
        recommended_skills = ['Android','Android development','Flutter','Kotlin','XML','Java','Kivy','GIT','SDK','SQLite']
        print("\n Our algorithm generated some skills for you :")
        for x in range(len(recommended_skills)):
            print(recommended_skills[x],)
        
    elif i.lower() in ios_keyword:
        print(i.lower())
        reco_field = 'IOS Development'
        print("\n Our analysis tells that You are looking for IOS Developer jobs")
        recommended_skills = ['IOS','IOS Development','Swift','Cocoa','Cocoa Touch','Xcode','Objective-C','SQLite','Plist','StoreKit',"UI-Kit",'AV Foundation','Auto-Layout']
        print("\n Our algorithm generated some skills for you :")
        for x in range(len(recommended_skills)):
            print(recommended_skills[x],)
        
    elif i.lower() in uiux_keyword:
        print(i.lower())
        reco_field = 'UI-UX Development'
        print("\n Our analysis tells that You are looking for IOS Developer jobs")
        recommended_skills = ['UI','User Experience','Adobe XD','Figma','Zeplin','Balsamiq','Prototyping','Wireframes','Storyframes','Adobe Photoshop','Editing','Illustrator','After Effects','Premier Pro','Indesign','Wireframe','Solid','Grasp','User Research']
        print("\n Our algorithm generated some skills for you :")
        for x in range(len(recommended_skills)):
            print(recommended_skills[x],)
            
            
            
            
            
resume_text = pdf_reader(path)

# print(resume_text)
resume_score = 0
print("---------------Resume Analysis--------------")
if 'Objective' in resume_text:
    resume_score = resume_score+20
    print("[+] Awesome! You have added Objective")
else:
    print("[-] According to our recommendation please add your career objective, it will give your career intension to the Recruiters.")

if 'Declaration' in resume_text:
    resume_score = resume_score+20
    print("[+] Awesome! You have added Declaration")
else:
    print("[-] According to our recommendation please add Declaration✍. It will give the assurance that everything written on your resume is true and fully acknowledged by you")

if 'Hobbies' or 'Interests' in resume_text:
    resume_score = resume_score+20
    print("[+] Awesome! You have added your Hobbies⚽")
else:
    print("[-] According to our recommendation please add Hobbies⚽. It will show your persnality to the Recruiters and give the assurance that you are fit for this role or not.")

if 'Achievements' in resume_text:
    resume_score = resume_score+20
    print("[+] Awesome! You have added your Achievements🏅 ")
else:
    print("[-] According to our recommendation please add Achievements🏅. It will show that you are capable for the required position.")

if 'Projects' in resume_text:
    resume_score = resume_score+20
    print("[+] Awesome! You have added your Projects👨‍💻 ")
else:
    print("[-] According to our recommendation please add Projects👨‍💻. It will show that you have done work related the required position or not.")



print("Your resume writing score is " + str(resume_score))


# print(data)


if os.path.exists('C:\pandu\SEMESTER II\Projects\RESUME PARSER\export.csv'):
    pass
else:
    with open('export.csv', 'w') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(['Name','Email','Mobile','Skills','Experience','Resume Score'])

with open('export.csv','a',newline='') as outfile:
    writer=csv.writer(outfile)
    # key_list=list(data.keys())
    # limit = len(key_list)
    
    writer.writerow([data['name'],data['email'],data['mobile_number'],data['skills'],data['experience'],resume_score])




