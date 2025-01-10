""""
from django.shortcuts import render
from .models import Student


# Create your views here.
def index(request):
    data=Student.objects.all()
    stu_count=data.count()
    stu_fname_with_m=data.filter(fname__startswith='M')
    return render(request,'base.html',{'record':data, #pass the all data as record
                                                 'stu_count': stu_count,  # Pass total student count
                                                  'stu_fname_with_m': stu_fname_with_m }) #pass students whose name sstarts with M
 
"""


from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
import json

def index(request):
    data = Student.objects.all()
    stu_count = data.count()
    stu_fname_with_m = data.filter(fname__startswith='M')
    return render(request, 'base.html', {
        'record': data,
        'stu_count': stu_count,
        'stu_fname_with_m': stu_fname_with_m
    })

# New view to handle the user question
def get_semester(request):
    print("Request received") 
    if request.method == 'POST':
        # Get the question from the user
        data = json.loads(request.body)
        question = data.get('question', '').lower()
        print(f"Received question: {question}")  # Debug: Print the question

        # If the question asks for the semester of a student
        if 'semester' in question:
            student_name = question.split('semester of')[-1].strip()  # Extract name after "semester of"
            student = Student.objects.filter(fname__iexact=student_name).first()  # Case-insensitive match
            if student:
                response = {
                    'reply': f"{student.fname}'s semester is {student.semester}."
                }
            else:
                response = {
                    'reply': f"Sorry, I couldn't find a student named {student_name}."
                }

        # If the question asks for the total number of students
        elif 'total number of students' in question or 'how many students' in question:
            total_students = Student.objects.count()
            response = {
                'reply': f"There are a total of {total_students} students."
            }

        # If the question asks for students whose names start with a specific letter
        elif 'names of students starting with' in question:
            letter = question.split('starting with')[-1].strip()  # Extract letter
            students_with_letter = Student.objects.filter(fname__istartswith=letter)  # Case-insensitive startswith filter
            if students_with_letter.exists():
                names = ', '.join([student.fname for student in students_with_letter])
                response = {
                    'reply': f"Students whose names start with {letter.upper()}: {names}."
                }
            else:
                response = {
                    'reply': f"No students found with names starting with {letter.upper()}."
                }

        else:
            response = {
                'reply': "Sorry, I couldn't understand the question. Please ask about the semester, total students, or student names."
            }

        print(f"Sending response: {response['reply']}")  # Debug: Print the response
        return JsonResponse(response)  # Send the response back to the frontend
