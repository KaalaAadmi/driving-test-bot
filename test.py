import os
import sys
# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
username=os.getenv("USERNAME")
password=os.getenv("PASSWORD")

print(f"Username: {username}")
print(f"Password: {password}")

# Add a goal button: /html/body/app-root/app-portal-parent/div[2]/mat-drawer-container/mat-drawer-content/div/div/div/app-my-goals/div[4]/button
# sleep(5)
# View my goal: /html/body/app-root/app-portal-parent/div[2]/mat-drawer-container/mat-drawer-content/div/div/div/app-goals/div/mat-accordion/mat-expansion-panel[1]/div/div/div/div[1]/app-goal/mat-card/mat-card-content/button[2]
# sleep(2)
# book a test: /html/body/app-root/app-portal-parent/div[2]/mat-drawer-container/mat-drawer-content/div/div/div/app-my-goal/div[2]/div/div[6]/app-my-goal-step-full/mat-card/mat-card-content/div/div/div/div/button
# sleep(2)
# locations: /html/body/app-root/app-portal-parent/div[2]/mat-drawer-container/mat-drawer-content/div/div/div/app-booking/app-booking-new/div/div/mat-horizontal-stepper/div/div[2]/div[1]/form/div/app-booking-new-form/div/div[2]/div[3]/div[1]/app-booking-form-location/button/span[1]/div/div[2]
# sleep(2)
# More loacations: /html/body/div[2]/div[2]/div/div/div/button[5]
