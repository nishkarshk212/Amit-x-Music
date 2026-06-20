import requests
import time

# Test Xbit API
print('Testing Xbit API...')
print('=' * 50)
try:
    start_time = time.time()
    response = requests.get(
        'https://music.xbitcode.com/search', 
        params={'q': 'hello', 'api_key': 'xbit_40gZEycIlXXF38AlKKU4I96ZnNaiDFOV'},
        timeout=15
    )
    elapsed = time.time() - start_time
    
    print(f'Status Code: {response.status_code}')
    print(f'Response Time: {elapsed:.2f}s')
    
    if response.ok:
        print('✓ Xbit API works!')
        print(f'\nResponse preview:')
        print(response.text[:500])
    else:
        print(f'✗ Xbit API failed with status {response.status_code}')
        print(f'Response: {response.text}')
        
except Exception as e:
    print(f'✗ Xbit API error: {type(e).__name__}: {e}')

print('\n' + '=' * 50 + '\n')

# Test ARU API
print('Testing ARU API...')
print('=' * 50)
try:
    start_time = time.time()
    response = requests.get(
        'https://aruyt-production.up.railway.app/search', 
        params={'q': 'hello', 'api_key': 'ARU-LlmvFnOs1KeRAxphnXQmHpBA'},
        timeout=15
    )
    elapsed = time.time() - start_time
    
    print(f'Status Code: {response.status_code}')
    print(f'Response Time: {elapsed:.2f}s')
    
    if response.ok:
        print('✓ ARU API works!')
        print(f'\nResponse preview:')
        print(response.text[:500])
    else:
        print(f'✗ ARU API failed with status {response.status_code}')
        print(f'Response: {response.text}')
        
except Exception as e:
    print(f'✗ ARU API error: {type(e).__name__}: {e}')

print('\n' + '=' * 50)
print('API testing complete!')
