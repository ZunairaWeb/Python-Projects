# def add_task(task, task_number):
#     for index in range(1, task_number + 1):
#         task_name = input("Enter your task: ")
#         task.append({'Task': task_name, 'Status': False})
#         print("Task Added!")
     
     
# def view_task(task):
#     if not task:
#         print("No tasks to show.")
#         return
#     print("\nTasks:")
#     for index, task_item  in enumerate(task):
#                 status = "Done" if task_item["Status"] else "Not Done"
#                 print(f"{index + 1}. {task_item['Task']} - {status}")
#     # for index, task_item in enumerate(task):
#     #     status = "Done" if task_item.get('Status') else "Not Done"
#     #     print(f"{index + 1}. {task_item.get('Task')} - {status}")
            

# def update_task(task,task_index):
    
#     if 0 <= task_index < len(task):
#         task[task_index]['Status'] = True
#         print("Task has been done")
#     else:
#         print("Task is not done yet")
        
        
# def delete_task(task, task_index):
#     if 0 <= task_index < len(task):
#         task.pop(task_index)  # Use pop() instead of popitem()
#         print("Task has been deleted successfully.")
#     else:
#         print("Invalid index. Task not deleted.")
# def exit_program():
#   pass



# def main():
#     task = []  # Initialize the task list outside the loop to persist tasks
    
#     while True: 
        
#         print("\nWelcome to To-do list!")
#         print("What would you like to do:")
#         print("1. Add a task")
#         print("2. View tasks")
#         print("3. Update a task")
#         print("4. Delete a task")
#         print("5. Exit")
#         user_input = int(input("Press any number (1-5) to continue: "))

#         if user_input == 1:
#             task_number = int(input("How many tasks do you want to enter: "))
#             add_task(task, task_number)  # Directly call add_task without reassigning
#         elif user_input == 2:
#             view_task(task)  # Directly call view_task without reassigning
#         elif user_input == 3:
#             task_index = int(input("Enter the task number to be select done:"))-1
#             update_task(task,task_index)
            
#         elif user_input == 4:
#             task_index = int(input("Enter the number you want to delete: ")) -1
#             delete_task(task, task_index)
#         elif user_input == 5:
#             print("Exiting the program. Goodbye!")
#             break
#         else:
#             print("Invalid input, please enter a valid number.")

# if __name__ == '__main__':
#     main()
#  Makke crud functions to  manage the tasks
task=[]

def add_task(task,task_number):
  for index in range(1,task_number+1):
    task_name = input("Enter name of task: ")
    task.append({'Task': task_name,'Status': False})
    print("Task Added Successfully")
  
def get_task(task):
  if not task:
    print("No Task")
    return
  print("\n Task: ")
  for index, task_item in enumerate(task):
    status = "Done" if task_item['Status'] else "Not done"
    print(f"{index + 1 }. {task_item['Task']} -{ [status]}")

    
def update_task(task,index_number):
  if 0 <= index_number < len(task):
    task[index_number]['Status'] = True
    print("Task Updated Successfully")
  else:
    print("TAsk not updated yet...")

  
def delete_task(task_index):
 if 0<=task_index < len(task):
   task.pop(task_index)
   print("Deleted Successfully")
 else:
   print("Task not deleted")




   
 
while True:

  print("Please Select the Tasks you wants to do?")
  print("1.Add a Task   ")
  print("2.Get a Task  ")
  print("3.Update a Task  ")
  print("4.Delete a Task   ")
  print("5.Exist  ")
  
  user_input = int(input("Enter any number to start the task list... "))
  if user_input == 1:
     task_number= int(input("Enter the task number you wanna add:  "))
     add_task(task,task_number)
    
  elif user_input ==2:
    get_task(task)
  
  elif user_input ==3:
    index_number = int(input("Enter the index number to update the task... "))-1
    update_task(task,index_number)
  elif user_input ==4:
    task_index = int(input("Enter the task number you wanna delete..  "))-1
    delete_task(task_index)
  elif user_input==5:
    break
  else:
    print("Enter the valid input")

