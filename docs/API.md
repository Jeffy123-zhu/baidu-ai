# API Documentation

## REST API Endpoints

### Health Check

```http
GET /
```

**Response:**
```json
{
  "service": "MediDoc AI",
  "version": "1.0.0",
  "status": "running"
}
```

### Upload Document

```http
POST /api/upload
Content-Type: multipart/form-data
```

**Parameters:**
- `file`: Medical document (PDF, JPG, PNG)

**Response:**
```json
{
  "success": true,
  "filename": "patient_record.pdf",
  "message": "File uploaded successfully"
}
```

### Run Diagnosis

```http
POST /api/diagnose
Content-Type: application/json
```

**Request Body:**
```json
{
  "document_id": "doc_12345",
  "patient_info": {
    "age": 65,
    "gender": "male"
  }
}
```

**Response:**
```json
{
  "diagnosis": "Preliminary analysis complete",
  "confidence": 0.89,
  "specialists_consulted": ["cardiology", "radiology"],
  "recommendations": [
    "Further cardiac examination recommended",
    "Follow-up in 2 weeks"
  ],
  "reports": {
    "professional": "...",
    "patient_friendly": "..."
  }
}
```

### Edge Device Status

```http
GET /api/edge/status
```

**Response:**
```json
{
  "offline_mode": true,
  "pending_sync": 3,
  "last_sync": "2025-11-26T10:30:00Z",
  "models_loaded": true
}
```

### Sync to Cloud

```http
POST /api/edge/sync
```

**Response:**
```json
{
  "synced": 3,
  "failed": 0,
  "pending": 0
}
```

## Python SDK Usage

```python
from medidoc import MediDocClient

# Initialize client
client = MediDocClient(api_key="your-api-key")

# Upload document
result = client.upload_document("patient_record.pdf")

# Run diagnosis
diagnosis = client.diagnose(result['document_id'])

print(diagnosis['recommendations'])
```

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid input |
| 401 | Unauthorized - Invalid API key |
| 404 | Not Found - Resource doesn't exist |
| 500 | Internal Server Error |
| 503 | Service Unavailable - System overloaded |
