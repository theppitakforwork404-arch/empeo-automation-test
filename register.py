from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # ตั้งค่า headless=False เพื่อให้อัดวิดีโอตอนรันได้ชัดเจน
    # (เปลี่ยนเป็น True ได้หากต้องการรันใน CI/CD)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    #  เข้าหน้าเว็บ
    page.goto("https://portal.uat.gofive.co.th/Register/empeo")
    
    #  กรอกข้อมูล
    page.get_by_test_id("input_radio_registration_company_others").click()
    
    page.get_by_test_id("input_textfield_input_register_company_name").fill("test")
    
    # เลือกประเภทธุรกิจ
    page.get_by_test_id("dropdown_selection_registration_company_type").click()
    page.get_by_text("ค้าปลีก", exact=True).click()
    
    # เลือกจำนวนผู้ใช้งาน
    page.get_by_test_id("dropdown_selection_registration_user_amount").click()
    page.get_by_text(" 1-20 ", exact=True).click()
    
    # ข้อมูลส่วนตัว
    page.get_by_test_id("input_textfield_input_registration_email").fill("me@gmail.com")
    page.get_by_test_id("input_textfield_input_register_first_name").fill("Theppitak")
    page.get_by_test_id("input_textfield_input_register_last_name").fill("meelek")
    page.get_by_role("textbox", name="เบอร์มือถือ*").fill("0967690708")
    
    # คูปองส่วนลด
    page.get_by_text("ใช้โค้ดส่วนลด").click()
    page.get_by_test_id("input_text_registration_coupon_code").fill("FREE15DAY")
    page.get_by_test_id("input_button_registration_btn_apply").click()
    
    # ยอมรับเงื่อนไขและสมัคร
    page.get_by_test_id("input_checkbox_registration_checkbox").check()
    page.get_by_test_id("button_submit_registration_try_for_free").click()
    
    # 4. ส่วนการจัดการ OTP (ด่านสุดท้าย)
    print("Waiting for OTP screen...")
    # รอให้ช่องกรอก OTP ปรากฏ
    page.wait_for_selector("[data-testid='input_text_registration_otp_Config']")
    
    # เนื่องจากเป็น 6 ช่องแยกกัน วิธีที่ดีที่สุดคือใช้ .type() ใส่เลข 123456 รวดเดียว
    page.get_by_test_id("input_text_registration_otp_Config").locator("input").first.type("123456")
    
    # กดปุ่มยืนยัน
    page.get_by_role("button", name="ยืนยัน").click()
    # 3. ตรวจสอบผลลัพธ์ (Assertion)
    expect(page.get_by_text("สมัครสมาชิกสำเร็จ")).to_be_visible(timeout=10000)

    # ปิดเบราว์เซอร์
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)