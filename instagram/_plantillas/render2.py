import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=b.new_page(viewport={"width":1080,"height":1080})
    for f in sys.argv[1:]:
        pg.goto(f"file://./{f}.html"); pg.wait_for_timeout(600); pg.screenshot(path=f"{f}.png")
    b.close()
