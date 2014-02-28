 c = webdriver.DesiredCapabilities.CHROME
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=c)