from ipywidgets import interact, widgets
from IPython.display import display

class Classroom:
  def __init__(self, name):
    self.name = name
    self.students = []
    self.assignments = []

class Student:
  def __init__(self, student_id):
    self.student_id = student_id

class Assignment:
  def __init__(self, details):
    self.details = details
    self.submitted = False

class VirtualClassroomManager:
  def __init__(self):
    self.classrooms = []

  def add_classroom(self, name):
    classroom = Classroom(name)
    self.classrooms.append(classroom)
    print(f"Classroom '{name}' has been created.")

  def add_student(self, student_id, class_name):
    for classroom in self.classrooms:
      if classroom.name == class_name:
        student = Student(student_id)
        classroom.students.append(student)
        print(f"Student '{student_id}' has been enrolled in '{class_name}'.")
        return
    print(f"Classroom '{class_name}' not found.")

  def schedule_assignment(self, class_name, assignment_details):
    for classroom in self.classrooms:
      if classroom.name == class_name:
        assignment = Assignment(assignment_details)
        classroom.assignments.append(assignment)
        print(f"Assignment for '{class_name}' has been scheduled.")
        return
    print(f"Classroom '{class_name}' not found.")

  def submit_assignment(self, student_id, class_name, assignment_details):
    for classroom in self.classrooms:
      if classroom.name == class_name:
        for student in classroom.students:
          if student.student_id == student_id:
            for assignment in classroom.assignments:
              if assignment.details == assignment_details:
                assignment.submitted = True
                print(f"Assignment submitted by Student '{student_id}' in '{class_name}'.")
                return
            print(f"Assignment '{assignment_details}' not found.")
            return
        print(f"Student '{student_id}' not found in '{class_name}'.")
        return
    print(f"Classroom '{class_name}' not found.")

# Initialize the manager
manager = VirtualClassroomManager()

# Create interactive widgets
command_widget = widgets.Dropdown(
    options=["add_classroom", "add_student", "schedule_assignment", "submit_assignment", "exit"],
    description="Command:"
)
student_id_widget = widgets.Text(description="Student ID:")
classroom_name_widget = widgets.Text(description="Classroom Name:")
assignment_details_widget = widgets.Text(description="Assignment Details:")

# Define an interactive function
def execute_command(command):
  if command == "add_classroom":
    manager.add_classroom(classroom_name_widget.value)
  elif command == "add_student":
    manager.add_student(student_id_widget.value, classroom_name_widget.value)
  elif command == "schedule_assignment":
    manager.schedule_assignment(classroom_name_widget.value, assignment_details_widget.value)
  elif command == "submit_assignment":
    manager.submit_assignment(student_id_widget.value, classroom_name_widget.value, assignment_details_widget.value)
  elif command == "exit":
    pass  # Exit the interactive loop

# Display interactive widgets and execute commands
interact(execute_command, command=command_widget)

# Display input widgets as needed
display(student_id_widget)
display(classroom_name_widget)
display(assignment_details_widget)
