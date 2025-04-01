from appium.webdriver.common.appiumby import AppiumBy


class LocatorLogin:
    icon_account = (AppiumBy.ACCESSIBILITY_ID, "account")
    icon_login = (AppiumBy.IOS_PREDICATE, 'name == "Đăng nhập" AND label == "Đăng nhập" AND value == "Đăng nhập"')
    text_account = (AppiumBy.ACCESSIBILITY_ID, "Email/ Số điện thoại")
    txt_password = (AppiumBy.ACCESSIBILITY_ID, "Mật khẩu")
    btn_submit = (AppiumBy.IOS_PREDICATE, 'name == "ĐĂNG NHẬP" AND label == "ĐĂNG NHẬP" AND value == "ĐĂNG NHẬP"')
    btn_home_page = (AppiumBy.IOS_PREDICATE, 'name == "home"')
    btn_logout = (AppiumBy.ACCESSIBILITY_ID, 'Đăng xuất')
    popup_agree_logout = (AppiumBy.ACCESSIBILITY_ID, 'Đồng ý')