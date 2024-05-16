Designing a RESTful API with Python and Flask

*This is a flask API of a Todo list app*


Requirements:
- sudo apt-install python3
- pip install flask

-- This API was done on a Ubuntu-20.04

To run this application we have to execute app.py:
> chmod a+x app.py
> ./app.py

*Methods*

GET 	http://[hostname]/todo/api/v1/tasks 			Retrive a list of tasks
GET 	http://[hostname]/todo/api/v1/tasks/[task_id]		Retrive a task
POST	http://[hostname]/todo/api/v1/tasks			Creae a new task
PUT	http://[hostname]/todo/api/v1/tasks/[task_id]		Update an existing task
DELETE	http://[hostname]/todo/api/v1/tasks/[task_id]		Delete a task


*Usage*

Retrive a list of tasks		
> curl -i http://localhost:5000/todo/api/v1/tasks
Retrive a task
> curl -i http://localhost:5000/todo/api/v1/tasks/<task_id>
Creae a new task
> curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Any-Title"}' http://localhost:5000/todo/api/v1/tasks
Update an existing task
> curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1/tasks/<task_id>
Delete a task
> curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/api/v1/tasks/<task_id>
