PYTHON := python3
PYTEST := $(PYTHON) -m pytest


debug:
	@echo "🚀 Running test debug..."
	@$(PYTEST) --log-cli-level=DEBUG --tb=auto -k "test_order_visa_001" -s 

test:
	@echo "🚀 Running test debug..."
	@$(PYTEST) -k "TestOrderAtm" -v

cd_source_xCode:
	@echo "cd_source_xCode"
	@ cd /Users/mac/.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent

open_source_xCode:
	@echo "open_xCode"
	@ open WebDriverAgent.xcodeproj