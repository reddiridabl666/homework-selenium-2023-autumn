class element_in_viewport(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        script = "var elem = arguments[0],                " + \
                "  box = elem.getBoundingClientRect(),    " + \
                "  cx = box.left + box.width / 2,         " + \
                "  cy = box.top + box.height / 2,         " + \
                "  e = document.elementFromPoint(cx, cy); " + \
                "for (; e; e = e.parentElement) {         " + \
                "  if (e === elem)                        " + \
                "    return true;                         " + \
                "}                                        " + \
                "return false;                            "
      
      
        elem = driver.find_element(*self.locator)
        return driver.execute_script(script, elem)
