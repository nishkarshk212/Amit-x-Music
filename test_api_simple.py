import requests
import json

def test_xbit():
    print("=" * 70)
    print("  TESTING XBIT API")
    print("=" * 70)
    base_url = "https://music.xbitcode.com"
    api_key = "xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV"
    
    # Try simple endpoints
    endpoints = [
        "/",
        "/api/v1",
        "/yt",
        "/search",
        "/song",
        "/video",
        "/download",
    ]
    
    for ep in endpoints:
        url = f"{base_url}{ep}"
        print(f"\n→ Testing {url}")
        
        # Try with different key params
        for key_param in ["api_key", "key", "token"]:
            try:
                params = {"q": "faded", key_param: api_key}
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    print(f"   ✅ 200 OK with {key_param}")
                    print(f"   {response.text[:300]}")
                else:
                    print(f"   Status {response.status_code}")
            except Exception as e:
                print(f"   Error: {e}")


def test_aru():
    print("\n" + "=" * 70)
    print("  TESTING ARU API")
    print("=" * 70)
    base_url = "https://aruyt-production.up.railway.app"
    api_key = "ARU-LlmvFnOs1KeRAxphnXQmHpBA"
    
    # Try simple endpoints
    endpoints = [
        "/",
        "/api/v1",
        "/yt",
        "/search",
        "/song",
        "/video",
        "/download",
    ]
    
    for ep in endpoints:
        url = f"{base_url}{ep}"
        print(f"\n→ Testing {url}")
        
        # Try with different key params
        for key_param in ["api_key", "key", "token"]:
            try:
                params = {"q": "faded", key_param: api_key}
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    print(f"   ✅ 200 OK with {key_param}")
                    print(f"   {response.text[:300]}")
                else:
                    print(f"   Status {response.status_code}")
            except Exception as e:
                print(f"   Error: {e}")


def test_common_patterns():
    print("\n" + "=" * 70)
    print("  TESTING COMMON API PATTERNS")
    print("=" * 70)
    
    # Xbit API patterns
    print("\nXbit API Test Patterns:")
    patterns = [
        "https://music.xbitcode.com/api/search?query=faded&api_key=xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV",
        "https://music.xbitcode.com/v1/search?q=faded&key=xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV",
        "https://music.xbitcode.com/yt/search?query=faded",
    ]
    
    for url in patterns:
        try:
            response = requests.get(url, timeout=10)
            print(f"{url} → {response.status_code}")
            if response.status_code == 200:
                print(response.text[:200])
        except Exception as e:
            print(f"  Error: {e}")
    
    # ARU API patterns
    print("\nARU API Test Patterns:")
    patterns = [
        "https://aruyt-production.up.railway.app/api/search?query=faded&api_key=ARU-LlmvFnOs1KeRAxphnXQmHpBA",
        "https://aruyt-production.up.railway.app/v1/search?q=faded&key=ARU-LlmvFnOs1KeRAxphnXQmHpBA",
        "https://aruyt-production.up.railway.app/yt/search?query=faded",
    ]
    
    for url in patterns:
        try:
            response = requests.get(url, timeout=10)
            print(f"{url} → {response.status_code}")
            if response.status_code == 200:
                print(response.text[:200])
        except Exception as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    test_xbit()
    test_aru()
    test_common_patterns()
    print("\n" + "=" * 70)
    print("  TESTING COMPLETE")
    print("=" * 70)
