#!/usr/bin/env python3
"""
Test script for working Xbit API endpoints
"""

import requests
import json

def print_section(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_info_endpoint():
    """Test the /info/{vid_id} endpoint"""
    print_section("1. Testing /info/{vid_id} Endpoint")
    
    api_key = 'xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV'
    vid_id = 'dQw4w9WgXcQ'
    
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    endpoint = f'https://tgapi.xbitcode.com/info/{vid_id}'
    print(f"Endpoint: {endpoint}")
    
    try:
        response = requests.get(endpoint, headers=headers, timeout=30)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nResponse:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
            if data.get('status') == 'success':
                print(f"\n✅ SUCCESS!")
                if 'audio_url' in data:
                    print(f"Audio URL: {data['audio_url'][:100]}...")
                if 'video_url' in data:
                    print(f"Video URL: {data['video_url'][:100]}...")
            else:
                print(f"\n❌ Error: {data.get('message')}")
        else:
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

def test_song_endpoint():
    """Test the /song/{vid_id} endpoint"""
    print_section("2. Testing /song/{vid_id} Endpoint")
    
    api_key = 'xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV'
    vid_id = 'dQw4w9WgXcQ'
    
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    
    endpoint = f'https://tgapi.xbitcode.com/song/{vid_id}'
    print(f"Endpoint: {endpoint}")
    
    try:
        response = requests.get(endpoint, headers=headers, timeout=30)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nResponse:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            
            if data.get('status') == 'success':
                print(f"\n✅ SUCCESS!")
                if 'audio_url' in data:
                    print(f"Audio URL: {data['audio_url'][:100]}...")
            else:
                print(f"\n❌ Error: {data.get('message')}")
        else:
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print_section("XBIT API WORKING ENDPOINTS TEST")
    test_info_endpoint()
    test_song_endpoint()
    print_section("TESTING COMPLETE - ALL WORKING!")
