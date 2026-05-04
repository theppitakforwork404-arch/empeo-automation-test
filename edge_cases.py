import time
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # สร้างตัวเลขสุ่มจากเวลาปัจจุบัน เพื่อไม่ให้ข้อมูลซ้ำ
    timestamp = str(int(time.time()))
    unique_company = f"testcorp_{timestamp}"
    unique_email = f"me_{timestamp}@gmail.com"
    
    # 1. เข้าหน้าเว็บ
    page.goto("https://portal.uat.gofive.co.th/Register/empeo")
    
    # 2. กรอกข้อมูล
    page.get_by_test_id("input_radio_registration_company_others").click()
    page.get_by_test_id("input_textfield_input_register_company_name").fill(unique_company)
    
    # เลือกประเภทธุรกิจ
    page.get_by_test_id("dropdown_selection_registration_company_type").click()
    page.get_by_text("ค้าปลีก", exact=True).click()
    
    # เลือกจำนวนผู้ใช้งาน
    page.get_by_test_id("dropdown_selection_registration_user_amount").click()
    page.get_by_text(" 1-20 ", exact=True).click()
    
    # ข้อมูลส่วนตัว
    page.get_by_test_id("input_textfield_input_registration_email").fill(unique_email)
    page.get_by_test_id("input_textfield_input_register_first_name").fill("Theppitak")
    page.get_by_test_id("input_textfield_input_register_last_name").fill("meelek")
   
   # 🔥 EDGE CASE: จงใจกรอกเบอร์มือถือผิด (ใส่แค่ 3 ตัว)
    page.get_by_role("textbox", name="เบอร์มือถือ*").fill("080")
    
    # คูปองส่วนลด
    page.get_by_text("ใช้โค้ดส่วนลด").click()
    page.get_by_test_id("input_text_registration_coupon_code").fill("FREE15DAY")
    page.get_by_test_id("input_button_registration_btn_apply").click()
    
    # ยอมรับเงื่อนไขและสมัคร
    page.get_by_test_id("input_checkbox_registration_checkbox").check()
    page.get_by_test_id("button_submit_registration_try_for_free").click()
    
    # 3. ส่วนการจัดการ OTP
    print("Waiting for OTP screen...")
    page.wait_for_selector("[data-testid='input_text_registration_otp_Config']")
    
    page.get_by_test_id("input_text_registration_otp_Config").locator("input").first.press_sequentially("123456")
    
    # กดปุ่มยืนยัน
    page.get_by_role("button", name="ยืนยัน").click()
    
  
    page.wait_for_timeout(3000) 
    print("Test executed successfully up to OTP validation.")

    # ปิดเบราว์เซอร์
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)