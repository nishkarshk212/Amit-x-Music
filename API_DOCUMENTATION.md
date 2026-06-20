# Xbit API Documentation

## Configuration
- **API Key**: `YT_API_KEY`
- **Base URL**: `https://tgapi.xbitcode.com`
- **Header**: `x-api-key: YOUR_API_KEY`

## ✅ Working Endpoints

### 1. Get Video/Song Info
**Endpoint**: `GET /info/{vid_id}`

**Python Example**:
```python
import requests

api_key = 'xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV'
vid_id = 'dQw4w9WgXcQ'
endpoint = f'https://tgapi.xbitcode.com/info/{vid_id}'

headers = {
    'x-api-key': api_key,
    'Content-Type': 'application/json'
}

response = requests.get(endpoint, headers=headers)
data = response.json()

if data.get('status') == 'success':
    print('Audio URL:', data.get('audio_url'))
    print('Video URL:', data.get('video_url'))
else:
    print('Error:', data.get('message'))
```

**Expected Response**:
```json
{
    "status": "success",
    "audio_url": "https://...",
    "video_url": "https://..."
}
```

### 2. Get Song Only
**Endpoint**: `GET /song/{vid_id}`

**Python Example**:
```python
import requests

api_key = 'xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV'
vid_id = 'dQw4w9WgXcQ'
endpoint = f'https://tgapi.xbitcode.com/song/{vid_id}'

headers = {
    'x-api-key': api_key,
    'Content-Type': 'application/json'
}

response = requests.get(endpoint, headers=headers)
data = response.json()

if data.get('status') == 'success':
    print('Audio URL:', data.get('audio_url'))
else:
    print('Error:', data.get('message'))
```

**Expected Response**:
```json
{
    "status": "success",
    "audio_url": "https://..."
}
```

## Test Scripts
1. `test_correct_api.py` - Tests the working endpoint
2. `full_api_test.py` - Comprehensive API testing
3. `test_api_simple.py` - Simple API tests

## Configuration Files
- `.env` - Environment variables
- `config.py` - Application configuration

## Notes
- API key must be passed via the `x-api-key` header
- Content-Type should be `application/json`
