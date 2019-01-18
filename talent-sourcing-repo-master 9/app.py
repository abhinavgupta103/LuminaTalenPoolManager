# import necessary libraries
import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/employee_attrition.sqlite"

db = SQLAlchemy(app)

#Reflect the table with all of the columns corresponding to each Belly Button collection event.
class Employees(db.Model):
    __tablename__ = 'employees'
    db.reflect()

@app.before_first_request
def setup():
    # Connect the samples_metadata table to our server (the other ones should be created already)
    db.create_all()

@app.route("/")
def index():
    """Return the dashboard hompage"""
    #Homepage with Plotly visualizations
    return render_template('index.html')

@app.route("/jobsummary")
def jobsummary():
    """Return second page that has a summary of job statistics"""
    #Page 2 with dropdown and plotly summaries
    return render_template('jobs.html')

@app.route('/gender')
def gender():
    """Gender Statistics for Overall Data"""
    #Query database for all female employees
    results = db.session.query(Employees.Gender).\
        filter(Employees.Gender=="Female").all()
    #Query database for all male employees
    results1 = db.session.query(Employees.Gender).\
        filter(Employees.Gender=="Male").all()
    #create lists
    female = [result[0] for result in results]
    male = [result[0] for result in results1]
    #the length of the above lists is the number of males and females
    female_count = len(female)
    male_count = len(male)
    #Create and return trace
    gender_trace = {
        "labels": ["Female", "Male"],
        "values": [female_count, male_count],
        "type": "pie"
    }
    return jsonify(gender_trace)

@app.route('/jobrole')
def jobrole():
    """Number of employees in each job"""
    #Query database for all job roles
    results = db.session.query(Employees.JobRole).all()
    #Create a list of all job roles
    joblist = [result[0] for result in results]
    #Create a second list with all duplicates deleted
    jobroles = list(set(joblist))
    #Create a list to hold the employee counts for each job role
    jobcounts = []
    #Iterating through each job role in the unique jobs list
    for jobrole in jobroles:
        counter = 0
        #If the job role in the list matches the job role we are searching for, add one to counter
        for x in range(0, len(joblist)):
            if(str(joblist[x]) == str(jobrole)):
                counter=counter+1
        #Add the count of jobs in a given role to the jobcounts list
        jobcounts.append(counter)
    #Create and return trace
    jobs_trace = {
        "x": jobroles,
        "y": jobcounts,
        "type": "bar"
    }
    return jsonify(jobs_trace)

@app.route('/department')
def department():
    """Number of employees in each department"""
    #Same query method as used in the /jobroles route
    results = db.session.query(Employees.Department).all()
    deptlist = [result[0] for result in results]
    depts = list(set(deptlist))
    deptcounts = []
    for dept in depts:
        counter = 0
        for x in range(0, len(deptlist)):
            if(str(deptlist[x]) == str(dept)):
                counter=counter+1
        deptcounts.append(counter)
    
    depts_trace = {
        "x": depts,
        "y": deptcounts,
        "type": "bar"
    }
    return jsonify(depts_trace)

@app.route('/satisfaction')
def jobsatisfaction():
    """Job satisfaction by department"""
    #Query departments and create a list of unique departments
    results = db.session.query(Employees.Department).all()
    deptlist = [result[0] for result in results]
    depts = list(set(deptlist))
    #Create a list to hold average job satisfaction
    deptsatisfaction_list = []
    #Iterate through each department and calculate average satisfaction by department
    for dept in depts:
        results1 = db.session.query(Employees.JobSatisfaction).\
            filter(Employees.Department==str(dept)).all()
        satlist = [result[0] for result in results1]
        avg_satisfaction = sum(satlist)/len(satlist)
        deptsatisfaction_list.append(avg_satisfaction)
    print(len(depts))
    print(len(deptsatisfaction_list))
    #Return dictionary with departments as the x and average satisfaction as the y
    sats_trace = {
        "x": depts,
        "y": deptsatisfaction_list,
        "type": "bar"
    }
    return jsonify(sats_trace)

@app.route('/jobs/<jobrole>')
def jobstatistics(jobrole):
    """Job statistics by Job Title"""
    job_name = jobrole.replace("_", " ")

    #Query Gender based on Job Role
    results = db.session.query(Employees.Gender).\
        filter(Employees.JobRole==str(job_name)).\
        filter(Employees.Gender=="Male").all()

    male = [result[0] for result in results]
    male_count = len(male)

    results = db.session.query(Employees.Gender).\
        filter(Employees.JobRole==str(job_name)).\
        filter(Employees.Gender=="Female").all()

    female = [result[0] for result in results]
    female_count = len(female)
    #Variables for trace
    gender_counts = [male_count, female_count]
    gender_labels = ["Male", "Female"]

    #Query Age by job role
    results = db.session.query(Employees.Age).\
        filter(Employees.JobRole==str(job_name))
    #Separate into age ranges
    r1 = results.\
                filter(Employees.Age>=0).\
                filter(Employees.Age<20).all()
    r2 = results.\
                filter(Employees.Age>=20).\
                filter(Employees.Age<28).all()
    r3 = results.\
                filter(Employees.Age>=28).\
                filter(Employees.Age<36).all()
    r4 = results.\
                filter(Employees.Age>=36).\
                filter(Employees.Age<44).all()
    r5 = results.\
                filter(Employees.Age>=44).\
                filter(Employees.Age<52).all() 
    r6 = results.\
                filter(Employees.Age>=52).\
                filter(Employees.Age<=60).all()
    #Count number in each age range
    r1_count = len([result[0] for result in r1])
    r2_count = len([result[0] for result in r2])
    r3_count = len([result[0] for result in r3])
    r4_count = len([result[0] for result in r4])
    r5_count = len([result[0] for result in r5])
    r6_count = len([result[0] for result in r6])
    #Create trace values
    age_ranges = ["0-19", "20-27", "28-35", "36-43", "44-51", "52-60"]
    range_counts = [r1_count, r2_count, r3_count, r4_count, r5_count, r6_count]

    #Query Job Role by Department
    results = db.session.query(Employees.Department).\
        filter(Employees.JobRole==str(job_name)).all()
    deptlist = [result[0] for result in results]
    #List of only unique department entries
    depts = list(set(deptlist))
    print(len(depts))
    #List to hold counts
    deptcounts = []
    for dept in depts:
        counter = 0
        for x in range(0, len(deptlist)):
            if(str(deptlist[x]) == str(dept)):
                counter=counter+1
        deptcounts.append(counter)
    print(len(deptcounts))
    
    
    #Return dictionary with all job statistics
    job_graphs_trace = {
        "0": {
            "labels":  gender_labels,
            "values": gender_counts,
            "type": "pie"
        },
        "1": {
            "x": age_ranges,
            "y": range_counts,
            "type": "bar"
        },
        "2": {
            "labels": depts,
            "values": deptcounts,
            "type": "pie"
        }
    }
    return jsonify(job_graphs_trace)

#Run the app. debug=True is essential to be able to rerun the server any time changes are saved to the Python file
if __name__ == "__main__":
    app.run(debug=True, port=5043)