#!/usr/bin/env python3
"""
Test the Xbit API integration module
"""

import sys
import os

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def print_section(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_xbit_api():
    """Test the Xbit API integration"""
    print_section("Testing Xbit API Integration")
    
    try:
        from Amit.helpers import xbit_api
        print("✅ Successfully imported xbit_api module")
        
        # Check if API is available
        if xbit_api.available:
            print("✅ Xbit API is configured and available")
        else:
            print("❌ Xbit API not configured - missing API key or URL")
            return False
        
        # Test 1: Get info (audio + video)
        print_section("1. Testing get_info()")
        video_id = "dQw4w9WgXcQ"
        info = xbit_api.get_info(video_id)
        
        if info:
            print("✅ get_info() successful!")
            print(f"   Status: {info.get('status')}")
            if 'audio_url' in info:
                print(f"   Audio URL: {info['audio_url'][:100]}...")
            if 'video_url' in info:
                print(f"   Video URL: {info['video_url'][:100]}...")
        else:
            print("❌ get_info() failed")
        
        # Test 2: Get song only
        print_section("2. Testing get_song()")
        song = xbit_api.get_song(video_id)
        
        if song:
            print("✅ get_song() successful!")
            print(f"   Status: {song.get('status')}")
            if 'audio_url' in song:
                print(f"   Audio URL: {song['audio_url'][:100]}...")
        else:
            print("❌ get_song() failed")
        
        print_section("Integration Test Complete!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("\nMake sure you're running from the project root directory")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print_section("Xbit API Integration Test")
    success = test_xbit_api()
    sys.exit(0 if success else 1)
