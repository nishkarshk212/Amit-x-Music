# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of AmitMusic
# Xbit API Integration

import requests
from typing import Optional, Dict, Any
from Amit import config, logger


class XbitAPI:
    """
    Xbit API Integration for YouTube Music streaming
    """
    
    def __init__(self):
        self.api_key = config.YT_API_KEY
        self.base_url = config.YTPROXY_URL
        self.headers = {
            'x-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        self.available = bool(self.api_key and self.base_url)
    
    def get_info(self, video_id: str) -> Optional[Dict[str, Any]]:
        """
        Get video/song info including both audio and video URLs
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Dictionary with status, audio_url, video_url if successful
        """
        if not self.available:
            logger.warning("Xbit API not configured - missing API key or URL")
            return None
        
        try:
            endpoint = f"{self.base_url}/info/{video_id}"
            logger.debug(f"Calling Xbit API: {endpoint}")
            
            response = requests.get(
                endpoint,
                headers=self.headers,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    logger.debug(f"Xbit API success for {video_id}")
                    return data
                else:
                    logger.error(f"Xbit API error: {data.get('message')}")
                    return None
            else:
                logger.error(f"Xbit API HTTP error: {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            logger.error("Xbit API request timeout")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Xbit API request error: {e}")
            return None
        except Exception as e:
            logger.error(f"Xbit API unexpected error: {e}")
            return None
    
    def get_song(self, video_id: str) -> Optional[Dict[str, Any]]:
        """
        Get song only (audio URL)
        
        Args:
            video_id: YouTube video ID
            
        Returns:
            Dictionary with status and audio_url if successful
        """
        if not self.available:
            logger.warning("Xbit API not configured - missing API key or URL")
            return None
        
        try:
            endpoint = f"{self.base_url}/song/{video_id}"
            logger.debug(f"Calling Xbit API: {endpoint}")
            
            response = requests.get(
                endpoint,
                headers=self.headers,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    logger.debug(f"Xbit API success for {video_id} (song only)")
                    return data
                else:
                    logger.error(f"Xbit API error: {data.get('message')}")
                    return None
            else:
                logger.error(f"Xbit API HTTP error: {response.status_code}")
                return None
                
        except requests.exceptions.Timeout:
            logger.error("Xbit API request timeout")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Xbit API request error: {e}")
            return None
        except Exception as e:
            logger.error(f"Xbit API unexpected error: {e}")
            return None


# Create singleton instance
xbit_api = XbitAPI()
