from appium.webdriver.common.appiumby import AppiumBy


class LocatorOrderCod:
    search_text_field = (AppiumBy.IOS_PREDICATE, 'value == "Tìm kiếm"')
    search_button = (AppiumBy.IOS_PREDICATE, 'name == "search"')
    accept_product = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther')
    buy_product_button = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeButton[2]')
    cart_button = (AppiumBy.ACCESSIBILITY_ID, 'cartButton')
    proceed_to_order_button = (AppiumBy.IOS_PREDICATE, 'name == "TIẾN HÀNH ĐẶT HÀNG" AND label == "TIẾN HÀNH ĐẶT HÀNG" AND value == "TIẾN HÀNH ĐẶT HÀNG"')
    order_cod_button = (AppiumBy.IOS_PREDICATE, 'name == "Đặt hàng" AND label == "Đặt hàng" AND value == "Đặt hàng"')
    text_order_code = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, 'Mã đơn hàng:')]")
    back_home_button = (AppiumBy.IOS_PREDICATE, 'name == "Trang chủ" AND label == "Trang chủ" AND value == "Trang chủ"')
    payment_expression_button = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeButton[1]')
    text_payment_expression = (AppiumBy.ACCESSIBILITY_ID, 'Thanh toán khi nhận hàng (COD)')
    back_icon_button = (AppiumBy.ACCESSIBILITY_ID, 'backIcon')
