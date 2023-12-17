from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

# Set the path to the Microsoft Edge WebDriver executable
edge_driver_path = 'C:/Users/BR/Downloads/msedgedriver.exe'  # Replace with the actual path on your system

# Create a new Edge browser session
edge_service = EdgeService(edge_driver_path)
edge_options = webdriver.EdgeOptions()

# If you want to open Edge in incognito mode, uncomment the line below
# edge_options.add_argument('--inprivate')

driver = webdriver.Edge(service=edge_service, options=edge_options)

# URL to visit
url_to_visit = 'https://www.amazon.com/'  # Replace with the desired URL

# Open the specified URL
driver.get(url_to_visit)
driver.maximize_window()
# Close the browser window after 5 seconds (you can adjust this time as needed)
driver.implicitly_wait(5000)
driver.quit()