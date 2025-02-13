# Django Logging Demo

This project demonstrates various logging concepts in Django using a simple Task Management API. It showcases both basic and advanced logging features, including structured JSON logging, custom formatters, and performance monitoring.

## Features

- REST API for Task Management using Django REST Framework
- Comprehensive logging setup with multiple handlers and formatters
- Custom decorator for performance logging
- JSON logging for better log aggregation
- Multiple log outputs (console, file, JSON file)
- Structured logging with context information

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd django-logging-demo
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create the logs directory:
```bash
mkdir logs
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Logging Features Demonstrated

### 1. Multiple Log Handlers
- Console output for development
- File-based logging for persistence
- JSON formatted logs for better parsing

### 2. Different Log Levels
- DEBUG: Detailed information for debugging
- INFO: General information about system operation
- WARNING: Warning messages for potential issues
- ERROR: Error messages for actual problems

### 3. Custom Logging Utilities
- Performance monitoring decorator (`@log_execution_time`)
- Structured logging with context information
- JSON formatting for machine-readable logs

### 4. Log Examples

Standard log entry:
```
INFO 2024-02-13 12:34:56,789 tasks 12345 67890 Retrieving all tasks
```

JSON log entry:
```json
{
    "asctime": "2024-02-13 12:34:56,789",
    "levelname": "INFO",
    "name": "tasks",
    "message": "Creating new task",
    "task_data": {
        "title": "Example Task",
        "priority": "HIGH"
    }
}
```

## API Endpoints

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a specific task
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task

## Git Setup

1. Initialize Git repository:
```bash
git init
```

2. Create .gitignore:
```bash
# .gitignore
*.pyc
__pycache__/
db.sqlite3
.env
venv/
logs/*.log
```

3. Make initial commit:
```bash
git add .
git commit -m "Initial commit: Task Management API with comprehensive logging"
```

## Contributing

Feel free to submit issues and enhancement requests!
