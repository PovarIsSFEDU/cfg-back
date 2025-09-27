# API Documentation for Configuration Management Application

This Django application provides a configuration management system with configuration creation/deployment capabilities.

## API Endpoints

### Configuration Management

#### POST /api/create/
Create a new configuration.

**Request Body:**
```json
{
  "name": "string",
  "description": "string",
  "files": ["string"],
  "meta_config": {
    "vcs_type": "github|gitlab",
    "temperature": "float"
  }
}
```

**Response:**
```json
{
  "message": "Configuration created successfully",
  "config_id": integer
}
```

#### POST /api/deploy/
Deploy a configuration (draft implementation).

**Response:**
```json
{
  "message": "Deploy endpoint - draft implementation"
}
```

#### POST /api/ask/
Ask questions about configurations.

**Request Body:**
```json
{
  "config_id": integer,
  "content": "string",
  "author": "user", // optional, defaults to "user"
  "files": ["string"] // optional
}
```

**Response:**
```json
{
  "message_id": integer,
  "author": "model",
  "content": "string",
  "files": ["string"],
  "created_at": "datetime",
  "meta_config": {
    "vcs_type": "github|gitlab",
    "temperature": "float"
  }
}
```

#### GET /api/all-configs/
Get list of all configurations.

**Response:**
```json
{
  "configs": [
    {
      "id": integer,
      "name": "string",
      "description": "string",
      "files": ["string"],
      "created_at": "datetime",
      "meta_config": {
        "vcs_type": "github|gitlab",
        "temperature": "float"
      },
      "messages": [
        {
          "id": integer,
          "author": "model|user",
          "content": "string",
          "files": ["string"],
          "created_at": "datetime"
        }
      ]
    }
  ]
}
```

#### GET /api/config-messages/{config_id}/
Get all messages for a specific configuration.

**Response:**
```json
{
  "config_id": integer,
  "config_name": "string",
  "meta_config": {
    "vcs_type": "github|gitlab",
    "temperature": "float"
  },
  "messages": [
    {
      "id": integer,
      "author": "model|user",
      "content": "string",
      "files": ["string"],
      "created_at": "datetime"
    }
  ]
}
```

#### POST /api/upload-file/
Upload a file to the server.

**Request Body (multipart/form-data):**
```
file: file_data
```

**Response:**
```json
{
  "message": "File uploaded successfully",
  "file_url": "url",
  "file_name": "string"
}
```

#### GET /media/uploads/{filename}/
Download a previously uploaded file.

**Response:**
File download

## Data Models

### Enums
- **VcsEnum**: `github`, `gitlab` 

### MetaConfig
- `vcs_type`: VcsEnum
- `temperature`: float

### NewConfig
- `name`: string
- `description`: text
- `files`: list of strings (JSON field)
- `meta_config`: MetaConfig (foreign key)
- `created_at`: datetime (auto-generated)

### Message
- `author`: "model" | "user"
- `content`: text
- `files`: list of strings (JSON field)
- `config`: NewConfig (foreign key)
- `created_at`: datetime (auto-generated)

## Requirements

- Django 5.2+
- Python 3.13+
- SQLite (default database)

## Setup

1. Create and activate virtual environment
2. Install Django: `pip install django`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`