import unittest
from todo_app import app, tasks  # Assuming you have a separate todo_app.py file

class TestTodoAPI(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_all_tasks(self):
        response = self.client.get('/todo/api/v1/tasks')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['tasks'], list)

    def test_get_single_task(self):
        task_id = 1  # Assuming task 1 exists
        response = self.client.get(f'/todo/api/v1/tasks/{task_id}')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['task'], dict)
        self.assertEqual(data['task']['id'], task_id)

    def test_get_nonexistent_task(self):
        nonexistent_task_id = 999  # Assuming no task with this ID
        response = self.client.get(f'/todo/api/v1/tasks/{nonexistent_task_id}')
        self.assertEqual(response.status_code, 404)

    def test_create_task(self):
        new_task_data = {'title': 'Test Task', 'description': 'This is a test task'}
        response = self.client.post('/todo/api/v1/tasks', json=new_task_data)
        data = response.json
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(data['task'], dict)
        self.assertIn('id', data['task'])
        self.assertEqual(data['task']['title'], new_task_data['title'])
        self.assertEqual(data['task']['description'], new_task_data['description'])

    def test_create_task_missing_title(self):
        missing_title_data = {'description': 'This is a test task'}
        response = self.client.post('/todo/api/v1/tasks', json=missing_title_data)
        self.assertEqual(response.status_code, 400)

    def test_update_task(self):
        task_id = 1  # Assuming task 1 exists
        update_data = {'title': 'Updated Title'}
        response = self.client.put(f'/todo/api/v1/tasks/{task_id}', json=update_data)
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['task'], dict)
        self.assertEqual(data['task']['id'], task_id)
        self.assertEqual(data['task']['title'], update_data['title'])

    def test_update_nonexistent_task(self):
        nonexistent_task_id = 999  # Assuming no task with this ID
        update_data = {'title': 'Updated Title'}
        response = self.client.put(f'/todo/api/v1/tasks/{nonexistent_task_id}', json=update_data)
        self.assertEqual(response.status_code, 404)

    def test_delete_task(self):
        task_id = 1  # Assuming task 1 exists
        response = self.client.delete(f'/todo/api/v1/tasks/{task_id}')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['result'])

    def test_delete_nonexistent_task(self):
        nonexistent_task_id = 999  # Assuming no task with this ID
        response = self.client.delete(f'/todo/api/v1/tasks/{nonexistent_task_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
