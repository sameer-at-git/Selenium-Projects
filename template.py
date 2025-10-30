import os
projects=[
    "01_basic_browser_automation",
    "02_form_filling_and_login_bot",
    "03_web_scraper_dynamic_pages",
    "04_product_price_tracker",
    "05_auto_job_application_bot",
    "06_youtube_playlist_downloader_gui"
    ]
for p in projects:
    os.makedirs(p,exist_ok=True)
    for f in [
        "main.py",
        "README.md"
        ]:
        open(os.path.join(p,f),"w").close()
print("All project folders and files created successfully.")
