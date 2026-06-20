import requests
import json
from urllib.parse import urljoin

def print_section(title):
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def print_result(success, message, data=None):
    status = "✅" if success else "❌"
    print(f"\n{status} {message}")
    if data:
        try:
            if isinstance(data, dict) or isinstance(data, list):
                print(f"   Response: {json.dumps(data, indent=2, ensure_ascii=False)[:1000]}")
            else:
                print(f"   Response: {str(data)[:1000]}")
        except:
            print(f"   Response: {str(data)[:1000]}")

def test_api(base_url, api_key, api_name):
    print_section(f"TESTING {api_name.upper()} API - {base_url}")
    
    # Common API endpoint patterns
    endpoints = [
        # Search endpoints
        {"path": "/search", "method": "GET", "params": {"q": "faded"}},
        {"path": "/api/search", "method": "GET", "params": {"q": "faded"}},
        {"path": "/api/v1/search", "method": "GET", "params": {"q": "faded"}},
        {"path": "/yt/search", "method": "GET", "params": {"q": "faded"}},
        {"path": "/youtube/search", "method": "GET", "params": {"q": "faded"}},
        {"path": "/music/search", "method": "GET", "params": {"q": "faded"}},
        
        # Song endpoints
        {"path": "/song", "method": "GET", "params": {"videoId": "dQw4w9WgXcQ"}},
        {"path": "/api/song", "method": "GET", "params": {"videoId": "dQw4w9WgXcQ"}},
        {"path": "/download", "method": "GET", "params": {"id": "dQw4w9WgXcQ"}},
        {"path": "/api/download", "method": "GET", "params": {"id": "dQw4w9WgXcQ"}},
        {"path": "/mp3", "method": "GET", "params": {"id": "dQw4w9WgXcQ"}},
        {"path": "/audio", "method": "GET", "params": {"id": "dQw4w9WgXcQ"}},
        
        # Video endpoints
        {"path": "/video", "method": "GET", "params": {"videoId": "dQw4w9WgXcQ"}},
        {"path": "/api/video", "method": "GET", "params": {"videoId": "dQw4w9WgXcQ"}},
        {"path": "/mp4", "method": "GET", "params": {"id": "dQw4w9WgXcQ"}},
        
        # Info endpoints
        {"path": "/info", "method": "GET", "params": {"videoId": "dQw4w9WgXcQ"}},
        {"path": "/api/info", "method": "GET", "params": {"videoId": "dQw4w9WgXcQ"}},
        {"path": "/details", "method": "GET", "params": {"id": "dQw4w9WgXcQ"}},
        
        # Health/check endpoints
        {"path": "/", "method": "GET", "params": {}},
        {"path": "/health", "method": "GET", "params": {}},
        {"path": "/ping", "method": "GET", "params": {}},
    ]
    
    # Different API key parameter names
    api_key_params = ["api_key", "key", "token", "apiKey", "apikey", "access_token"]
    
    working_endpoints = []
    
    for endpoint in endpoints:
        print(f"\n📍 Testing: {endpoint['method']} {endpoint['path']}")
        
        for key_param in api_key_params:
            try:
                url = urljoin(base_url, endpoint['path'])
                
                # Prepare request parameters
                params = endpoint['params'].copy()
                params[key_param] = api_key
                
                # Try GET request
                response = requests.request(
                    method=endpoint['method'],
                    url=url,
                    params=params,
                    timeout=15,
                    allow_redirects=True
                )
                
                if response.status_code == 200:
                    print_result(True, f"Success with param: {key_param}")
                    
                    # Try to parse response
                    try:
                        data = response.json()
                        print_result(True, "Valid JSON response", data)
                    except:
                        print_result(True, "Text response", response.text)
                    
                    working_endpoints.append({
                        "api": api_name,
                        "endpoint": endpoint['path'],
                        "method": endpoint['method'],
                        "key_param": key_param,
                        "status_code": response.status_code
                    })
                    break
                elif response.status_code != 404:
                    print_result(False, f"Status {response.status_code}: {response.text[:200]}")
                    
            except requests.exceptions.Timeout:
                print_result(False, "Request timeout")
            except requests.exceptions.ConnectionError:
                print_result(False, "Connection error")
            except Exception as e:
                print_result(False, f"Error: {str(e)}")
    
    return working_endpoints

if __name__ == "__main__":
    print_section("STARTING COMPREHENSIVE API TESTING")
    
    all_working = []
    
    # Test Xbit API
    xbit_working = test_api(
        "https://music.xbitcode.com",
        "xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV",
        "Xbit"
    )
    all_working.extend(xbit_working)
    
    # Test ARU API
    aru_working = test_api(
        "https://aruyt-production.up.railway.app",
        "ARU-LlmvFnOs1KeRAxphnXQmHpBA",
        "ARU"
    )
    all_working.extend(aru_working)
    
    # Summary
    print_section("SUMMARY OF WORKING ENDPOINTS")
    if all_working:
        for ep in all_working:
            print(f"✅ {ep['api']} - {ep['method']} {ep['endpoint']} (key param: {ep['key_param']})")
    else:
        print("❌ No working endpoints found")
        
    print("\n" + "="*70)
    print("  TESTING COMPLETE")
    print("="*70)
