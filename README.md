# AI Support Chat

A real-time AI-powered support chat application built with Django, WebSockets, and OpenAI integration.

## Features

- Real-time chat functionality using WebSockets
- AI-powered responses using OpenAI's API
- JWT-based authentication
- Asynchronous task processing with Celery
- Redis for message broker and caching
- Docker containerization for easy deployment
- RESTful API endpoints

## Tech Stack

- **Backend Framework**: Django 5.2
- **API Framework**: Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)
- **Real-time Communication**: Django Channels
- **Task Queue**: Celery
- **Message Broker**: Redis
- **AI Integration**: OpenAI API
- **Containerization**: Docker & Docker Compose
- **Database**: SQLite (configurable for production)

## Prerequisites

- Python 3.11+
- Docker and Docker Compose
- OpenAI API key

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Django settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database settings
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Redis settings
REDIS_HOST=redis
REDIS_PORT=6379

# Celery settings
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
CELERY_TIMEZONE=UTC
CELERY_TASK_TRACK_STARTED=True
CELERY_TASK_TIME_LIMIT=1800

# API Keys
OPEN_AI_TOKEN=your-openai-token-here

# JWT settings
JWT_ACCESS_TOKEN_LIFETIME=60
JWT_REFRESH_TOKEN_LIFETIME=1440
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-support-chat
```

2. Create and configure the `.env` file as shown above.

3. Build and start the Docker containers:
```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`

## Project Structure

```
ai_support_chat/
├── ai_support_chat/     # Main project directory
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL configuration
│   ├── asgi.py          # ASGI configuration
│   └── wsgi.py          # WSGI configuration
├── chat/               # Chat application
│   ├── models.py       # Chat models
│   ├── views.py        # Chat views
│   ├── urls.py         # Chat URLs
│   └── consumers.py    # WebSocket consumers
├── users/              # User management application
│   ├── models.py       # User models
│   ├── views.py        # User views
│   └── urls.py         # User URLs
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose configuration
└── .env               # Environment variables
```

## Services

The application consists of four main services:

1. **Web Service**: Runs the Django application with Daphne ASGI server
2. **Celery Worker**: Processes background tasks
3. **Celery Beat**: Handles scheduled tasks
4. **Redis**: Serves as message broker and cache

## API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/refresh/` - Refresh JWT token
- `POST /api/auth/logout/` - User logout

### Chat
- `GET /api/chat/` - Get chat history
- `POST /api/chat/` - Send message
- `WS /ws/chat/` - WebSocket connection for real-time chat

### User Management
- `GET /api/users/me/` - Get current user
- `PUT /api/users/me/` - Update user profile

## Development

To run the project in development mode:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in `.env`
2. Configure a production database (e.g., PostgreSQL)
3. Set up proper SSL/TLS certificates
4. Configure proper security headers
5. Use a production-grade ASGI server

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

