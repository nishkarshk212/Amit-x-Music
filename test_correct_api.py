import requests
import json

def test_xbit_api():
    print("=" * 70)
    print("  TESTING XBIT API - CORRECT ENDPOINTS")
    print("=" * 70)
    
    api_key = 'xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV'
    vid_id = 'dQw4w9WgXcQ'  # Rick Astley - Never Gonna Give You Up
    
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    # Test 1: Info endpoint
    print("\n1. Testing Info Endpoint:")
    endpoint = f'https://tgapi.xbitcode.com/info/{vid_id}'
    print(f"   {endpoint}")
    
    try:
        response = requests.get(endpoint, headers=headers, timeout=30)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n   Response:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
            if data.get('status') == 'success':
                print(f"\n   ✅ Success!")
                if 'audio_url' in data:
                    print(f"   Audio URL: {data['audio_url'][:100]}...")
                if 'video_url' in data:
                    print(f"   Video URL: {data['video_url'][:100]}...")
            else:
                print(f"\n   ❌ Error: {data.get('message')}")
        else:
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: Try to find search endpoint
    print("\n" + "=" * 70)
    print("2. Testing Search Endpoints:")
    print("=" * 70)
    
    search_endpoints = [
        f'https://tgapi.xbitcode.com/search',
        f'https://tgapi.xbitcode.com/yt/search',
        f'https://tgapi.xbitcode.com/api/search',
    ]
    
    for endpoint in search_endpoints:
        print(f"\n   Testing: {endpoint}")
        
        # Try with query params
        params_list = [
            {'q': 'faded'},
            {'query': 'faded'},
            {'search': 'faded'},
        ]
        
        for params in params_list:
            try:
                response = requests.get(endpoint, headers=headers, params=params, timeout=30)
                if response.status_code == 200:
                    print(f"   ✅ Success with params: {list(params.keys())}")
                    print(f"   Response: {response.text[:500]}")
                    break
                else:
                    print(f"   Status {response.status_code}")
            except Exception as e:
                print(f"   Error: {e}")
    
    # Test 3: Try other common endpoints
    print("\n" + "=" * 70)
    print("3. Testing Other Common Endpoints:")
    print("=" * 70)
    
    other_endpoints = [
        f'https://tgapi.xbitcode.com/song/{vid_id}',
        f'https://tgapi.xbitcode.com/video/{vid_id}',
        f'https://tgapi.xbitcode.com/download/{vid_id}',
    ]
    
    for endpoint in other_endpoints:
        print(f"\n   Testing: {endpoint}")
        try:
            response = requests.get(endpoint, headers=headers, timeout=30)
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                print(f"   Response: {response.text[:500]}")
        except Exception as e:
            print(f"   Error: {e}")

if __name__ == "__main__":
    test_xbit_api()
    print("\n" + "=" * 70)
    print("  TESTING COMPLETE")
    print("=" * 70)
