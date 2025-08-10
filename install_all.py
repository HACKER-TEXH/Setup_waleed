
import os
import subprocess
import sys

# ✅ Lightweight & essential modules only (no numpy, pandas, scikit-learn)
modules = [
    "requests", "bs4", "mechanize", "pycurl", "httpx", "certifi", "colorama", "fake_useragent",
    "rich", "urllib3", "setuptools", "idna", "soupsieve", "chardet", "html5lib", "lxml",
    "charset-normalizer", "termcolor", "progress", "tqdm", "tldextract", "dnspython",
    "python-dateutil", "pytz", "pyfiglet", "instaloader", "flask", "pycryptodome", "pillow",
    "six", "cython", "brotli", "pyopenssl", "psutil", "pyjwt", "cryptography", "telethon",
    "cloudscraper", "selenium", "schedule", "aiohttp", "beautifulsoup4", "python-dotenv",
    "retry", "requests-toolbelt", "asyncio", "simplejson", "urllib3[socks]"
]

# ✅ Write to requirements.txt
with open("requirements.txt", "w") as req_file:
    for module in modules:
        req_file.write(f"{module}\n")

print("\n📦 requirements.txt created successfully.\n")

# ✅ Install each module individually
for module in modules:
    try:
        __import__(module.split("[")[0])
        print(f"\033[1;92m[✓] Already Installed:\033[0m {module}")
    except ModuleNotFoundError:
        print(f"\033[1;93m[+] Installing:\033[0m {module}")
        subprocess.call([sys.executable, "-m", "pip", "install", module])

print("\n\033[1;92m✅ All modules installed. You can now use `pip install -r requirements.txt` later if needed.\033[0m")
