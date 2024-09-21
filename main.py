import requests
import time
from datetime import datetime
from waybackpy import WaybackMachineSaveAPI
import hashlib

def scrape_and_archive():
    url = "https://0x6a4e.pro/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    last_signature = None
    
    while True:
        try:
            response = requests.get(url, headers=headers)
            content = response.text
            current_signature = hashlib.md5(content.encode()).hexdigest()
            print(current_signature)
            if current_signature != last_signature:
                print("-----------")
                print("last_signature: ", last_signature)
                print("current_signature: ", current_signature)
                print(f"Change detected at {datetime.now()}")
                last_signature = current_signature
                
                # Archive the page
                save_api = WaybackMachineSaveAPI(url, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
                archived_url = save_api.save()
                print(f"Archived at: {archived_url}")
                print("-----------")
            else:
                print(f"No change detected at {datetime.now()}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        time.sleep(30)

if __name__ == "__main__":
    scrape_and_archive()
