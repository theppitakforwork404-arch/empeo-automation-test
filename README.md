# Empeo Registration Automation Test
Automation script for registration flow using Playwright.

## Setup
1. Install requirements: `pip install playwright pytest`
2. Install browser drivers: `playwright install`

## How to Run
- Run the script: `python register.py`

## Test Case Design (Test Coverage)

| Test Case ID | Test Scenario | Steps to Reproduce | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Successful registration with valid data | 1. Go to registration page.<br>2. Fill valid & unique data (using timestamp).<br>3. Check T&C.<br>4. Click Submit. | System successfully accepts the data and redirects to the OTP verification screen. | ✅ Automated |
| **TC-02** | Promo code validation | 1. Click 'ใช้โค้ดส่วนลด'.<br>2. Input code `FREE15DAY`.<br>3. Click Apply. | The promo code is applied successfully to the registration flow. | ✅ Automated |
| **TC-03** | OTP verification flow | 1. Wait for OTP input container.<br>2. Input standard test OTP (`123456`).<br>3. Click Confirm. | System processes the OTP (Note: UAT environment catches the mock OTP). | ✅ Automated |
| **TC-04** | Form Validation (Data duplication prevention) | 1. Run script multiple times. | Script handles unique email/company name generation dynamically to prevent data duplication errors. | ✅ Automated |