def check_path(driver, paths):
    for path in paths:
        try:
            driver.find_element('xpath', path)
            return path
        except:
            pass

    return None
