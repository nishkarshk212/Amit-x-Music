import requests
import json

def test_endpoints(base_url, api_key, api_name):
    print(f"\n{'='*70}")
    print(f"  TESTING {api_name.upper()} API")
    print(f"{'='*70}")
    
    # Common endpoint variations
    search_endpoints = [
        "/search",
        "/api/search",
        "/search.php",
        "/yt/search",
        "/music/search",
        "/api/v1/search",
        "/youtube/search",
    ]
    
    song_endpoints = [
        "/song",
        "/api/song",
        "/download",
        "/api/download",
        "/yt/song",
        "/music/song",
        "/mp3",
        "/audio",
    ]
    
    video_endpoints = [
        "/video",
        "/api/video",
        "/yt/video",
        "/music/video",
        "/mp4",
    ]
    
    info_endpoints = [
        "/info",
        "/api/info",
        "/song/details",
        "/video/details",
        "/yt/info",
    ]
    
    # Test search endpoints
    print(f"\n🔍 Testing Search Endpoints for {api_name}:")
    print("-" * 50)
    for endpoint in search_endpoints:
        try:
            url = f"{base_url}{endpoint}"
            print(f"\nTesting: {url}")
            
            # Try different parameter names
            params_list = [
                {"q": "faded", "api_key": api_key},
                {"query": "faded", "api_key": api_key},
                {"search": "faded", "api_key": api_key},
                {"q": "faded", "token": api_key},
                {"query": "faded", "token": api_key},
            ]
            
            for params in params_list:
                try:
                    response = requests.get(url, params=params, timeout=10)
                    if response.status_code == 200:
                        print(f"✅ SUCCESS! Status: {response.status_code}")
                        print(f"   Params used: {list(params.keys())}")
                        try:
                            data = response.json()
                            print(f"   Response: {json.dumps(data, indent=2, ensure_ascii=False)[:500]}")
                        except:
                            print(f"   Response: {response.text[:500]}")
                        break
                except Exception as e:
                    continue
                    
        except Exception as e:
            continue
    
    # Test song info/download endpoints with a known video ID
    print(f"\n🎵 Testing Song/Download Endpoints for {api_name}:")
    print("-" * 50)
    test_video_id = "dQw4w9WgXcQ"
    
    for endpoint in song_endpoints + info_endpoints:
        try:
            url = f"{base_url}{endpoint}"
            print(f"\nTesting: {url}")
            
            # Try different parameter variations
            params_list = [
                {"videoId": test_video_id, "api_key": api_key},
                {"id": test_video_id, "api_key": api_key},
                {"video": test_video_id, "api_key": api_key},
                {"videoId": test_video_id, "token": api_key},
                {"id": test_video_id, "token": api_key},
            ]
            
            # Also try URL path variations
            path_variations = [
                f"{endpoint}/{test_video_id}",
                f"{endpoint}?videoId={test_video_id}&api_key={api_key}",
            ]
            
            for params in params_list:
                try:
                    response = requests.get(url, params=params, timeout=10)
                    if response.status_code == 200:
                        print(f"✅ SUCCESS! Status: {response.status_code}")
                        print(f"   Params used: {list(params.keys())}")
                        try:
                            data = response.json()
                            print(f"   Response: {json.dumps(data, indent=2, ensure_ascii=False)[:500]}")
                        except:
                            print(f"   Response: {response.text[:500]}")
                        break
                except Exception as e:
                    continue
                    
            for path_var in path_variations:
                try:
                    response = requests.get(f"{base_url}{path_var}", timeout=10)
                    if response.status_code == 200:
                        print(f"✅ SUCCESS! Status: {response.status_code}")
                        print(f"   Path used: {path_var}")
                        try:
                            data = response.json()
                            print(f"   Response: {json.dumps(data, indent=2, ensure_ascii=False)[:500]}")
                        except:
                            print(f"   Response: {response.text[:500]}")
                        break
                except Exception as e:
                    continue
                    
        except Exception as e:
            continue

if __name__ == "__main__":
    # Test both APIs
    test_endpoints(
        "https://music.xbitcode.com",
        "xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV",
        "Xbit"
    )
    
    print("\n" * 3)
    
    test_endpoints(
        "https://aruyt-production.up.railway.app",
        "ARU-LlmvFnOs1KeRAxphnXQmHpBA",
        "ARU"
    )
