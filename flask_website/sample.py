
# from package/folder/module import Class
from flask import Flask
from flask import render_template, request

# instance name = class name
# __name__ -> represents the name of the application package and it is used by flask
#             to identify resources like templates, atatic assets, and others.
app = Flask(__name__)

# @app.route() -> maps the URL specific function: tells python where to go to: serves as traffic light in flask
@app.route('/')
def home():
  # return "Hello World"
  # full_name = "Mary"
  return render_template('index.html')

@app.route('/about')
def about():
  # return "This is my ABOUT PAGE"
  return render_template('about.html')

@app.route('/student')
def student():
  return render_template('student.html')

# methods=['POST', 'GET'] -> you have to put this in the route if data comes from form
@app.route('/display', methods=['POST', 'GET'])
def display():
  # if request.method == 'POST' -> this refers the method attribute in the form(html) make sure what you write in the form is the same with the route else there will be error
  if request.method == 'POST':
    # all date from request.form will be saved to the variable result
    # all value entered in the form is given to python variable result
    # equest.form ->this means the form in the student.html, get the data from the form in student.html
    result = request.form
    # dis = result -> pass all the data from result to disp(variable in your display.thml)
    return render_template('display.html', disp = result)

@app.route('/grades')
def grades():
  return render_template('grades.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
  if request.method == 'POST':
    result = request.form
    return render_template('result.html', disp = result)


# @app.route('/check')
# def check():
#   if 5 < 3:
#     return "False"
#   else:
#     return "True"

# @app.route('/loop')
# def loop():
#   sum = 0
#   for x in range(1,5):
#     sum += x
#   return str(sum)



# allows of prevents parts of code from being run when modules are imported
# it is used to execute/run parts of your code
# __name__ ->special variable that defines the name of the class or the current module or script that you are running
if __name__ == '__main__':
  app.run(debug=True)

