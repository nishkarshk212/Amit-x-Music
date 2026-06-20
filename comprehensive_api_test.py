import requests
import json
import time

def print_section(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def print_result(success, message, data=None):
    status = "✓" if success else "✗"
    print(f"\n{status} {message}")
    if data:
        print(f"\nResponse: {json.dumps(data, indent=2, ensure_ascii=False)[:1000]}")

def test_xbit_api():
    base_url = "https://music.xbitcode.com"
    api_key = "xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV"
    
    print_section("TESTING XBIT API")
    
    # Test 1: Search
    print_section("1. Search Endpoint")
    try:
        response = requests.get(
            f"{base_url}/search",
            params={"q": "Faded", "api_key": api_key},
            timeout=20
        )
        print_result(response.ok, f"Search (status: {response.status_code})", response.json() if response.ok else response.text)
        if response.ok:
            results = response.json()
            if results and "data" in results and len(results["data"]) > 0:
                first_video_id = results["data"][0]["videoId"]
                print(f"\n→ Found video ID: {first_video_id}")
    except Exception as e:
        print_result(False, f"Search failed: {e}")

    # Test 2: Song Info
    print_section("2. Song Info Endpoint")
    try:
        response = requests.get(
            f"{base_url}/info",
            params={"videoId": "dQw4w9WgXcQ", "api_key": api_key},
            timeout=20
        )
        print_result(response.ok, f"Song Info (status: {response.status_code})", response.json() if response.ok else response.text)
    except Exception as e:
        print_result(False, f"Song Info failed: {e}")

    # Test 3: Song Download
    print_section("3. Song Download Endpoint")
    try:
        response = requests.get(
            f"{base_url}/song",
            params={"videoId": "dQw4w9WgXcQ", "api_key": api_key},
            timeout=30
        )
        print_result(response.ok, f"Song Download (status: {response.status_code})", response.json() if response.ok else response.text)
    except Exception as e:
        print_result(False, f"Song Download failed: {e}")

    # Test 4: Video Download
    print_section("4. Video Download Endpoint")
    try:
        response = requests.get(
            f"{base_url}/video",
            params={"videoId": "dQw4w9WgXcQ", "api_key": api_key},
            timeout=30
        )
        print_result(response.ok, f"Video Download (status: {response.status_code})", response.json() if response.ok else response.text)
    except Exception as e:
        print_result(False, f"Video Download failed: {e}")

def test_aru_api():
    base_url = "https://aruyt-production.up.railway.app"
    api_key = "ARU-LlmvFnOs1KeRAxphnXQmHpBA"
    
    print_section("TESTING ARU API")
    
    # Test 1: Search
    print_section("1. Search Endpoint")
    try:
        response = requests.get(
            f"{base_url}/search",
            params={"q": "Faded", "api_key": api_key},
            timeout=20
        )
        print_result(response.ok, f"Search (status: {response.status_code})", response.json() if response.ok else response.text)
        if response.ok:
            results = response.json()
            if results and isinstance(results, list) and len(results) > 0:
                first_video_id = results[0].get("videoId")
                print(f"\n→ Found video ID: {first_video_id}")
    except Exception as e:
        print_result(False, f"Search failed: {e}")

    # Test 2: Song Info
    print_section("2. Song Info Endpoint")
    try:
        response = requests.get(
            f"{base_url}/info",
            params={"videoId": "dQw4w9WgXcQ", "api_key": api_key},
            timeout=20
        )
        print_result(response.ok, f"Song Info (status: {response.status_code})", response.json() if response.ok else response.text)
    except Exception as e:
        print_result(False, f"Song Info failed: {e}")

    # Test 3: Song Download
    print_section("3. Song Download Endpoint")
    try:
        response = requests.get(
            f"{base_url}/song",
            params={"videoId": "dQw4w9WgXcQ", "api_key": api_key},
            timeout=30
        )
        print_result(response.ok, f"Song Download (status: {response.status_code})", response.json() if response.ok else response.text)
    except Exception as e:
        print_result(False, f"Song Download failed: {e}")

    # Test 4: Video Download
    print_section("4. Video Download Endpoint")
    try:
        response = requests.get(
            f"{base_url}/video",
            params={"videoId": "dQw4w9WgXcQ", "api_key": api_key},
            timeout=30
        )
        print_result(response.ok, f"Video Download (status: {response.status_code})", response.json() if response.ok else response.text)
    except Exception as e:
        print_result(False, f"Video Download failed: {e}")

if __name__ == "__main__":
    print("=" * 70)
    print("  COMPREHENSIVE API TESTING")
    print("=" * 70)
    
    test_xbit_api()
    time.sleep(1)
    test_aru_api()
    
    print_section("TESTING COMPLETE")
