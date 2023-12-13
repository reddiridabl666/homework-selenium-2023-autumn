from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class element_in_viewport(object):
    def __init__(self, locator: tuple[str, str]):
        self.locator = locator

    def __call__(self, driver: RemoteWebDriver):
        script = """
                    var elem = arguments[0],
                    box = elem.getBoundingClientRect(),
                    cx = box.left + box.width / 2,
                    cy = box.top + box.height / 2,
                    e = document.elementFromPoint(cx, cy);
                    for (; e; e = e.parentElement) {
                    if (e === elem)
                      return true;
                    }
                    return false;
                """

        elem = driver.find_element(*self.locator)
        return driver.execute_script(script, elem)


class elements_count_changed:
    def __init__(self, locator: tuple[str, str], start_size: int):
        self.locator = locator
        self.start_size = start_size

    def __call__(self, driver: RemoteWebDriver):
        elems = driver.find_elements(*self.locator)

        if self.start_size == len(elems):
            return False

        return elems
