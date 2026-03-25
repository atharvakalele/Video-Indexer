# Selenium Python Automation - Topic Index

This index contains topics extracted from the tutorial video ["Selenium with Python Tutorial..."](https://youtu.be/2DD-ynCIZ4w).

## 1. Introduction & Core Concepts
- What is Selenium WebDriver and what are its primary components?
- Why is Selenium WebDriver the most popular component in the Selenium suite?
- Does Selenium support automation for mobile or desktop applications, or just web applications?
- How is WebDriver defined in the context of Python (e.g., as a module or package)?
- Why is Selenium WebDriver referred to as an API (Application Programming Interface)?
- What is the three-layer architecture of a web application (Presentation, Business Logic, Backend)?
- What is the difference between GUI testing, API testing, and Database testing?
- Which tools are commonly used for API and Database testing alongside Selenium?

## 2. Selenium Architecture (v3 vs v4)
- How does Selenium 3.x interact with browsers using the JSON Wire Protocol?
- What are the common issues associated with the JSON Wire Protocol (unstability, performance)?
- What architectural changes were introduced in Selenium 4.x regarding the W3C Protocol?
- Why is the W3C Protocol considered superior for browser communication?
- Who implements the browser-specific drivers (e.g., Chrome Driver, Gecko Driver)?

## 3. Environment Setup & Configuration
- What are the prerequisites for setting up a Selenium automation environment?
- How do you download and configure browser-specific drivers for Chrome, Edge, and Firefox?
- Why is it critical to match the browser driver version with the installed browser version?
- Where is the best practice location to store browser drivers on a local machine?
- What are the two main ways to install the Selenium package in a Python project?
- How can you install a specific version (e.g., a beta version) of Selenium using pip?
- How can you configure your system to launch browsers without explicitly specifying the driver path in your code?

## 4. Writing Your First Automation Script
- How do you import the WebDriver module into a Python script?
- How do you initialize a Chrome browser instance using Selenium?
- What is the purpose of the `driver.get()` method?
- How do you handle "Deprecation Warnings" when using Selenium 4?
- How do you use the `Service` class in Selenium 4 to manage executable paths?
- What is a "Web Element" and how does Selenium interact with them?
- What are the common attributes used to identify elements (ID, Name, XPath)?
- How do you use `find_element` in Selenium 4 compared to the Selenium 3 approach?
- How do you perform actions like typing (`send_keys`) and clicking (`click`) on elements?
- Why is it important to use the `clear()` method on input fields before typing?
- How do you capture and verify the page title for validation purposes?
- What is the difference between `driver.close()` and `driver.quit()`?
- How can you run the same automation script on different browsers like Firefox or Edge?
- How do you find an element's XPath if it doesn't have a unique ID or Name?

## Session 2: Locators in Selenium
- What are the two main focus areas in automation testing (Identification and Action)?
- What is a "Locator" and why is it essential in Selenium WebDriver?
- Is there a strict rule on which locator to use for a specific element, or is it a matter of choice?
- What are the basic built-in locators supported by Selenium (ID, Name, Link Text, Partial Link Text, Class Name, Tag Name)?
- What are "Customized Locators" (CSS Selector and XPath) and how do they differ from basic locators?
- What is the basic structure of an HTML element (Tag, Attribute, Value)?
- How do you use the `inspect` tool in a browser to view an element's HTML source?
- What is the significance of the `img` tag for images and the `a` tag for links?
- How do you use `driver.find_element(By.ID, "value")` to identify an element by its ID?
- How do you use `driver.find_element(By.NAME, "value")` to identify an element by its Name?
- What is the `driver.maximize_window()` method used for?
- What is "Link Text" and how do you use the `By.LINK_TEXT` locator?
- What is "Partial Link Text" and when is it more useful than `By.LINK_TEXT`?
- Are locator values case-sensitive?
- Why are `Class Name` and `Tag Name` often used to find multiple elements?
- What is the difference between `find_element` and `find_elements`?
- What data type does `find_elements` return in Python (a list of web element objects)?
- How do you count the total number of links or sliders on a page using `find_elements` and the `len()` function?
- What happens if you use `find_element` on a locator that matches multiple elements?
- What is a "CSS Selector" and what are the different combinations used to create one?
- How do you create a CSS Selector using the Tag and ID combination (syntax: `tag#id`)?
- How do you create a CSS Selector using the Tag and Class combination (syntax: `tag.class`)?
- How do you handle spaces in class names when writing a CSS Selector?
- How do you create a CSS Selector using the Tag and Attribute combination (syntax: `tag[attribute='value']`)?
- How do you combine Tag, Class, and an additional Attribute in a CSS Selector to target a specific element among multiple similar ones?
- How do you use `By.CSS_SELECTOR` in your Python script?

## Session 3: XPath Locators in Selenium
- What is the full form of XPath?
- Why is XPath considered a powerful and essential locator in Selenium, especially for dynamic web pages?
- What is the "Document Object Model" (DOM) and how does it relate to how XPath works?
- Does XPath work directly on the HTML source or the browser-created DOM?
- What are the two main types of XPath?
- What is "Absolute XPath" (Full XPath) and what is its starting root node?
- What is the syntax difference between Absolute XPath and Relative XPath (single slash vs. double slash)?
- How does Absolute XPath navigate through the DOM to find an element?
- What are the disadvantages of using Absolute XPath in automation projects?
- Why can Absolute XPath be unstable and easily broken by developer changes?
- What is "Relative XPath" (Partial XPath) and what is its main advantage over Absolute XPath?
- How do you find an element's XPath using browser developer tools (Right-click -> Inspect -> Copy XPath)?
- What is the common syntax for a Relative XPath expression?
- Can you use the `*` wildcard in place of a tag name in an XPath expression?
- What is "Selectors Hub" and how does it help in generating and testing locators?
- How do you use the `OR` operator in an XPath to match an element with multiple attributes?
- How do you use the `AND` operator in an XPath to ensure multiple conditions are met?
- What is the `contains()` function in XPath and why is it useful for dynamic elements?
- How do you use the `starts-with()` function to handle elements with attributes that change but have a fixed prefix?
- What is the `text()` function in XPath and how do you use it to identify elements based on their visible inner text?
- How do you use `By.XPATH` in a Selenium Python script?
- Why is Relative XPath preferred 100% of the time over Absolute XPath in industry projects?

## Session 4: XPath Axes in Selenium
- What are "XPath Axes" and how do they allow you to traverse the DOM?
- How does XPath enable both top-to-bottom and bottom-to-top navigation?
- What does the `self` axis refer to in an XPath expression?
- What is a `parent` axis and how do you use it to find the immediate parent of an element?
- How do you find all child elements of a specific node using the `child` axis?
- What are `ancestor` and `descendant` axes? How do they differ from `parent` and `child`?
- What is the difference between `following` and `following-sibling` axes?
- What is the difference between `preceding` and `preceding-sibling` axes?
- How do you use the `::` syntax with XPath axes (e.g., `parent::td`, `child::li`)?
- In what scenarios is it necessary to use XPath axes instead of simple attributes?
- How can you identify a target element that has no unique attributes by using its nearby "self" or parent elements?
- What is the advantage of using `find_elements` when dealing with axes like `child` or `descendant`?
- How do you count the number of descendant nodes or siblings using Selenium and XPath axes?
- Why is understanding the DOM hierarchy crucial for effectively using XPath axes?
- When should you use the `*` wildcard with an axis (e.g., `following::*`)?
- Can you traverse from a child element (like a link) to its grandparent or higher (ancestor)?

## Session 5: Selenium WebDriver Commands - Part 1
- What are the five main categories of Selenium WebDriver commands?
- What are the "Application Related Commands" (also known as Get commands) in Selenium Python?
- How do you use `driver.get(url)` to open a web application?
- How do you capture the title of the current web page using `driver.title`?
- How do you retrieve the current URL of the page using `driver.current_url`?
- What is the purpose of `driver.page_source` and what information does it return?
- What are the "Conditional Commands" and which three methods belong to this category?
- What is the return type of conditional methods like `is_displayed()`, `is_enabled()`, and `is_selected()`?
- How does `is_displayed()` differ from `is_enabled()` in terms of element status?
- Why is `is_selected()` specifically used for radio buttons and checkboxes?
- What are the "Browser Commands" and what is the key difference between `driver.close()` and `driver.quit()`?
- Which command (`close` or `quit`) kills the entire browser process and all associated windows?
- What are the "Navigational Commands" and how do `back()`, `forward()`, and `refresh()` work?
- What is the difference between `find_element` and `find_elements` when a locator matches multiple elements?
- What happens if `find_element` fails to locate an element versus when `find_elements` fails?
- What is "Inner Text" and how do you retrieve it using the `.text` property?
- When should you use `get_attribute("value")` instead of `.text` to retrieve the content of an input box?
- How do you extract the value of a specific HTML attribute (like `id`, `name`, or `type`) using `get_attribute()`?

## Session 6: Synchronization and Wait Commands (Implicit vs. Explicit)
- What is the "Synchronization Problem" in automation and why does it occur?
- Why is script execution usually faster than web application responses?
- What is `time.sleep()` and why is it generally discouraged in professional automation scripts?
- What are the two main types of Wait commands provided by Selenium WebDriver?
- What is "Implicit Wait" and how do you declare it globally for a driver instance?
- At what point in the script should Implicit Wait be defined for maximum effectiveness?
- Does Implicit Wait wait for the full timeout duration if the element appears early?
- What is "Explicit Wait" and how does it differ from Implicit Wait in terms of conditions?
- Which class is used to implement Explicit Wait in Selenium Python (`WebDriverWait`)?
- What are "Expected Conditions" (`EC`) and can you name a few examples (e.g., `presence_of_element_located`)?
- How do you use the `until()` and `until_not()` methods with `WebDriverWait`?
- How can you handle or ignore specific exceptions (like `NoSuchElementException`) within an Explicit Wait?
- What is "Polling Frequency" in the context of Explicit Wait?
- Why is `find_element` not explicitly required when using `WebDriverWait` with a condition?
- Which wait type is considered more effective and "stabler" for complex synchronization issues?
- Can you explain the syntax for importing and using the `By` class with `expected_conditions`?

## Session 7: Interacting with Web Elements - Checkboxes, Links, and Dropdowns
- How do you select a specific checkbox using its ID or XPath in Selenium?
- How can you select all checkboxes on a page using `find_elements` and a loop?
- What logic can be used to select multiple checkboxes based on their names (e.g., "Monday" and "Sunday")?
- How do you select only the last 2 or last 3 checkboxes from a dynamic list?
- What is the formula for calculating the starting index when selecting elements from the end of a list?
- How do you select the first few checkboxes based on a specific count?
- How do you clear or unselect all checkboxes, and why should you use `is_selected()` before clicking?
- What are the three common types of links (Internal, External, Broken)?
- How do you click a link using `link_text` vs. `partial_link_text`?
- How can you find the total number of links on a page using the `<a>` tag name?
- What is a "Broken Link" and how do you identify it using HTTP response codes?
- Which Python module (`requests`) is used to verify link status without opening them in a browser?
- What range of HTTP status codes (e.g., >= 400) indicates a broken or invalid link?
- How do you handle dropdowns that use the `<select>` tag in HTML?
- Which Selenium class (`Select`) must be imported to work with dropdown elements?
- What are the three ways to select an option from a dropdown (`visible_text`, `value`, `index`)?
- How do you capture and print all options from a dropdown using the `.options` attribute?
- How can you select a dropdown option *without* using the built-in `Select` class methods?

## Session 8: Alerts, Frames, and Multiple Browser Windows
- What are the three main types of JavaScript alerts/popups (Alert, Confirm, Prompt)?
- How do you switch the driver's focus to an alert window using `driver.switch_to.alert`?
- How can you retrieve the text message displayed on an alert window?
- What is the difference between `accept()` and `dismiss()` methods when handling alerts?
- How do you send text input to a "Prompt" alert using the `send_keys()` method?
- Why is it often necessary to store the alert object in a variable before performing multiple actions?
- What is an "Authentication Popup" and how does it differ from a standard JavaScript alert?
- What is the common technique to bypass an authentication popup by injecting credentials into the URL?
- What are Frames (IFrames) and why can't Selenium interact with elements inside them by default?
- How do you switch to a frame using its Name, ID, or as a WebElement?
- What is the purpose of `driver.switch_to.default_content()` after interacting with a frame?
- How do you handle "Nested" or "Inner" frames, and what is `driver.switch_to.parent_frame()`?
- What is the difference between `window_handle` and `window_handles`?
- How are browser window IDs (Handles) generated, and are they static or dynamic?
- How do you switch between multiple browser windows using `driver.switch_to.window(handle)`?
- How can you use window titles to identify and switch to a specific child window?
- What is the strategy for closing *only* specific browser windows while keeping others open?
- How does `driver.close()` differ from `driver.quit()` when multiple windows are open?

## Session 9: Notification Popups and Handling Web Tables
- What are "Notification Popups" and why can't they be handled using standard Alert commands?
- How do you use `ChromeOptions` to disable browser-level notifications using the `--disable-notifications` argument?
- What are the basic HTML tags that define a web table (`<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`)?
- How can you count the total number of rows in a table using XPath and the `len()` function on a list of WebElements?
- How do you count the total number of columns by identifying the number of header (`<th>`) or data (`<td>`) tags in a single row?
- What is the XPath syntax for retrieving data from a specific cell (e.g., Row 5, Column 1)?
- How do you iterate through all rows and columns of a table using nested loops?
- What is the concept of a "Dynamic XPath" and how do you parameterize row and column indices within it?
- How do you retrieve table data based on a specific condition (e.g., "Find all books where the Author is X")?
- What is the difference between a "Static Web Table" and a "Dynamic Web Table"?
- How do you handle tables where the number of rows changes dynamically (e.g., after logging in or filtering)?
- In a dynamic table, how can you iterate through rows to count elements matching a specific status (e.g., "Enabled" vs. "Disabled")?
- Why is it important to use `switch_to.default_content()` or `switch_to.parent_frame()` when dealing with tables nested inside frames?

## Session 10: Handling Date Pickers (Calendars)
- What is the difference between "Standard" web elements (buttons, radio buttons) and "Non-Standard/Customized" elements like date pickers?
- Why do date pickers require custom automation logic for different websites instead of a single standard approach?
- In what scenario can you use the `send_keys()` method to directly type a date into a date picker input box?
- What is the common date format (e.g., mm/dd/yyyy) used when passing dates via `send_keys()`?
- How do you handle cases where `send_keys()` is disabled or not permitted by the application?
- What is the step-by-step logic for selecting a future date by navigating through months using "Next" buttons?
- How do you use a `while True` loop with a `break` condition to keep clicking "Next" until the expected Month and Year are reached?
- What XPath strategy is used to capture all date elements within a specific calendar month?
- How do you iterate through the list of calendar dates to find and click the exact day (e.g., "15")?
- How does the logic change when you need to select a "Past" date (e.g., for a Date of Birth field)?
- For advanced date pickers with Month/Year dropdowns, how can you use the `Select` class to simplify navigation?
- Why is it more efficient to select Month and Year from dropdowns rather than clicking "Previous" or "Next" buttons multiple times?

## Session 11: Mouse Actions and Scrolling
- What is the `ActionChains` class in Selenium and why is it used for mouse-related operations?
- How do you perform a "Mouse Over" (Hover) action using the `move_to_element()` method?
- Why is the `perform()` method mandatory at the end of an `ActionChains` statement?
- How do you handle multi-level menu navigation using a chain of `move_to_element()` calls?
- What is the method used for performing a "Right Click" (Context Click) in Selenium?
- How can you interact with menu options (like Edit, Cut, Copy) that appear only after a Right Click?
- What is the difference between a normal `click()` and the `double_click()` method in `ActionChains`?
- How do you implement "Drag and Drop" by specifying a `source_element` and a `target_element`?
- How do you automate a "Slider" element using the `drag_and_drop_by_offset()` method?
- What are x-offset and y-offset, and how do they determine the movement of a slider?
- Why can't the `ActionChains` class be used for scrolling a web page?
- How do you use `execute_script()` to perform vertical scrolling using JavaScript (`window.scrollBy`)?
- What are the three common scrolling strategies: by pixel number, until an element is visible, and to the end of the page?
- How do you capture the current scroll position using `window.pageYOffset`?
- How do you scroll back up to the top of a page using a negative pixel value or a zero coordinate?

## Session 12: Keyboard Actions, File Downloads, and Uploads
- How do you use `ActionChains` to perform keyboard combinations like Ctrl+A (Select All), Ctrl+C (Copy), and Ctrl+V (Paste)?
- What is the purpose of the `key_down()` and `key_up()` methods in `ActionChains`?
- How do you simulate pressing the "Tab" key to navigate between input fields?
- Why is it important to release modifier keys (like Control or Shift) using `key_up()` after an action is performed?
- What are the challenges of automating file downloads in different browsers (Chrome, Edge, vs. Firefox)?
- How do you use "Browser Options" and "Preferences" to specify a custom download directory for files?
- What is a "Mime Type" and why is it necessary to specify it when configuring file downloads in Firefox?
- How do you bypass the browser's "Save/Open" dialogue box in Firefox using the `never_ask_to_save_disk` preference?
- What specific preference is used to download PDF files instead of opening them in the browser's built-in PDF viewer?
- How do you automate file uploads in Selenium using the `send_keys()` method on an `<input type="file">` element?
- Why is the `send_keys()` method preferred over clicking the "Upload" button for automation purposes?
- What are the limitations of Selenium when handling OS-level "Open File" dialogs, and how does `send_keys()` bypass these limitations?

## Session 13: Bootstrapped Dropdowns, Screenshots, Cookies, and Headless Mode
- What is a "Bootstrapped Dropdown" and how does it differ from a standard `<select>`-based dropdown?
- Why can't the `Select` class be used for handling bootstrapped dropdowns?
- What is the common automation strategy for selecting an option from a bootstrapped dropdown (e.g., clicking the toggle, then iterating through `<li>` elements)?
- How do you capture a screenshot of the current web page using the `save_screenshot()` method?
- What are the different screenshot methods available in Selenium (e.g., `get_screenshot_as_file`, `get_screenshot_as_png`)?
- How do you open a link in a new tab using the `Keys.CONTROL + Keys.ENTER` keyboard combination?
- What are the new Selenium 4 methods `new_window('tab')` and `new_window('window')` used for?
- How does `new_window()` differ from traditional window switching in terms of driver focus?
- What are cookies in the context of web applications, and why is it important to test them?
- How do you retrieve all cookies from a browser using the `get_cookies()` method?
- What information (attributes) is typically contained within a cookie object (e.g., Name, Value, Expiry, Domain)?
- How do you add a custom cookie to the browser session using `add_cookie()`?
- What are the methods for deleting a specific cookie (`delete_cookie`) vs. all cookies (`delete_all_cookies`)?
- What is "Headless Mode" in browser automation, and what are its primary advantages (speed, multitasking)?
- How do you configure Chrome, Edge, and Firefox to run in headless mode using their respective `Options` classes?
- In what scenarios is headless mode preferred over headed mode, and vice versa?

## Session 14: Data-Driven Testing (Excel)
- What is Data-Driven Testing (DDT) and why is it important in automation frameworks?
- Which Python module is commonly used to interact with Excel files (.xlsx) in Selenium?
- How do you install the `openpyxl` module using `pip` or PyCharm settings?
- What are the core components of an Excel file structure (Workbook -> Sheet -> Rows/Columns -> Cells)?
- How do you load an Excel workbook and access a specific sheet by name or as an "active" sheet?
- What methods are used to find the total number of rows (`max_row`) and columns (`max_column`) in a sheet?
- How do you read data from a specific cell using `sheet.cell(row, column).value`?
- How do you write data into a specific cell and ensure the changes are saved using `workbook.save(file)`?
- What is an "Excel Utility" file, and why is it better to centralize Excel operations there instead of in test cases?
- How do you implement reusable functions in a utility file for getting row counts, reading data, and writing data?
- How do you apply cell formatting (like green/red fill colors) to indicate test pass/fail results in Excel?
- What is the step-by-step workflow for a data-driven test case: from reading data, passing it to the UI, to validating and writing results back?
- Why is it necessary to convert data read from Excel (often strings) into appropriate types (like `float`) for comparison?
- How do you handle cleaning up the UI (e.g., clicking a "Clear" button) between different iterations of a data-driven test?

## Session 15: Database Testing (SQL)
- What is the difference between a Database Server and a Database Client?
- Why do we need a "Database Connector" (e.g., `mysql-connector-python`) to interact with a database from Python?
- How do you establish a connection to a MySQL database using `mysql.connector.connect()`?
- What are the essential connection parameters (Host, Port, User, Password, Database Name)?
- What is a "Cursor" in database programming, and how is it used to execute SQL queries?
- What is the difference between executing DML commands (Insert, Update, Delete) and DRL commands (Select)?
- Why is it mandatory to use `connection.commit()` after performing DML operations?
- How do you fetch and iterate through the result set of a `SELECT` query using a cursor?
- What are the differences between DDL (Data Definition), DML (Data Manipulation), and DRL (Data Retrieval) languages?
- How can you implement Data-Driven Testing by fetching test data from a database table instead of an Excel sheet?
- Why is using `try-except` blocks crucial when dealing with database connections?
- What are the limitations of using Selenium for direct "Database Testing," and why is it considered more of a DDT source?
- How do you close a database connection properly to release resources?

## Extra Video: Selenium & Java Mock Interview (gGWuzTPSJ8Y)
- What are the challenges and disadvantages of the Agile process?
- How do you ensure all scenarios in an application are tested (test coverage)?
- What are the various types of testing conducted in a project (Functional, Integration, System, Regression)?
- What is Integration Testing and what scenarios are checked?
- What are the common test case design techniques (BVA, Error Guessing, Equivalence Partitioning)?
- How do you handle a bug found in production?
- When do you perform regression testing, and what is considered?
- What is the difference between Change Request (CR) and Feature Request (FR)?
- What are the important features of Java used in automation (Inheritance, Abstraction, Polymorphism/Overloading, Encapsulation)?
- What collections are mainly used in Selenium (Set, List)?
- What is the difference between Set and List in Java?
- What is the use of the `final` keyword in Java (with class, variable, method)?
- What is the difference between `final` and `finally`?
- How to find the largest of two numbers without using an `if` condition using the Ternary Operator?
- How to count uppercase and lowercase characters in a string in Java?
- Can you explain the statement `WebDriver driver = new ChromeDriver();`?
- Why do we use wait statements, and what expected conditions are used in explicit waits?
- What is the use of Desired Capabilities in Selenium?
- What is the Document Object Model (DOM)?
- What is an XPath and how does it work with the DOM structure?
- What is the difference between Absolute and Relative XPath, and which is preferable?
- What is the use of `JavascriptExecutor` in Selenium?
- How do you handle multiple windows in Selenium (`getWindowHandle` vs `getWindowHandles`)?
- How do you find the number of options in a drop-down using the `Select` class?
- How do you perform mouse operations using the `Actions` class?
- What is the difference between Hard Assert and Soft Assert in TestNG?
- How does prioritization work in TestNG, especially when multiple tests have the same or zero priority?
- How do you execute only the failed test cases in TestNG?
- Can you explain the components of a Hybrid Driven Framework (Data-driven, Modular, Keyword)?
- How do you maintain test data and reusable utilities in your framework?
- What are the benefits of using a Maven project for automation?
- What is the role of Jenkins in your automation pipeline, and how does it integrate with GitHub?
- What are the basic Git commands used in a daily workflow (`push`, `pull`, `commit`, `merge`)?
