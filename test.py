from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://dexscreener.com"
    sb.uc_open_with_reconnect(url, 5)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.uc_gui_handle_captcha()
    print("Success! Website did not detect SeleniumBase!!!")
    selector = "body"
    try:
        text_content = sb.get_text(selector)
        print(f"Text content of selector '{selector}':\n{text_content}")
    except Exception as e:
        print(f"Error getting text content: {e}")
