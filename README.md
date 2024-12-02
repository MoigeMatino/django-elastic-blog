# Django Elastic Blog

A blog application built with Django and Elasticsearch for enhanced search capabilities.

## Tech Stack

- Python
- Django
- Elasticsearch
- Docker

## Project Structure

    django-elastic-blog/
    ├── blog/           # Blog application
    ├── core/           # Core application
    ├── search/         # Search functionality
    ├── .dockerignore
    ├── .gitignore  
    ├── Dockerfile
    ├── compose.yaml    # Docker compose configuration
    ├── manage.py
    └── requirements.txt

## Setup and Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/MoigeMatino/django-elastic-blog.git
   ```
2. Using Docker to run the application:
   ```bash
    docker-compose up --build
   ```
## Features

- Blog post management
- Elasticsearch integration for advanced search capabilities
- Containerized application using Docker

## Development

The project is structured as a Django application with three main components:
- Blog: Handles blog post functionality
- Core: Contains core application settings and configurations
- Search: Manages Elasticsearch integration and search features

## Requirements

Dependencies can be found in `requirements.txt`. The application is containerized using Docker for easy deployment and development.

## Contributing

Feel free to submit issues and pull requests.

   
