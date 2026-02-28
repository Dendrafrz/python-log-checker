import os

def analyze_log(file_path):
    if not os.path.exists(file_path):
        print(f"[-] File {file_path} not found")
        return
    
    with open(file_path, 'r') as file:
        logs = file.readlines()
    print(f"[*] Menganalisis {len(logs)} row log...")


    #finding indication login failed attempt
    failed_attempts = [line.strip() for line in logs if "Failed password" in line]
    
    for attempt in failed_attempts:
        print(f"[!] failed: {attempt}")

if __name__ == "__main__":
    analyze_log("auth.log")