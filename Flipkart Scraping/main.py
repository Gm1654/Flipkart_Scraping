from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()

# Lists to store scraped data
Product_Name = []
Prices = []
Description = []
Reviews = []

# Loop through the pages
for i in range(1, 7):
    url = f"https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    
    # Open the page with Selenium
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)  # Wait for the page to load

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "lxml")

    # Find the product container
    box = soup.find("div", class_="DOjaWF gdgoEp")

    if box:  # Check if the box element was found
        # Extract product names
        names = box.find_all("div", class_="KzDlHZ")
        if names:  # Check if names were found
            for name in names:
                Product_Name.append(name.text.strip())
        else:
            Product_Name.append("N/A")  # Fallback value

        # Extract prices
        prices = box.find_all("div", class_="Nx9bqj _4b5DiR")
        if prices:  # Check if prices were found
            for price in prices:
                Prices.append(price.text.strip())
        else:
            Prices.append("N/A")  # Fallback value

        # Extract descriptions
        desc = box.find_all("ul", class_="G4BRas")
        if desc:  # Check if descriptions were found
            for description in desc:
                Description.append(description.text.strip())
        else:
            Description.append("N/A")  # Fallback value

        # Extract reviews
        reviews = box.find_all("div", class_="XQDdHH")
        if reviews:  # Check if reviews were found
            for review in reviews:
                Reviews.append(review.text.strip())
        else:
            Reviews.append("N/A")  # Fallback value
    else:
        print("The product container was not found on the page.")
        
driver.quit()

# Create a DataFrame and save to CSV
df = pd.DataFrame({
    'Product Name': Product_Name,
    'Prices': Prices,
    'Description': Description,
    'Reviews': Reviews
})

# Save the DataFrame to a CSV file
df.to_csv("Flipkart_Mobiles_Under_50000.csv", index=False)
print("Data has been successfully saved to 'Flipkart_Mobiles_Under_50000.csv'.")



































# # ------------------------------------------------This code with only Beautiful Soup------------------------------------

# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# Product_Name=[]
# Prices=[]
# Description=[]
# Reviews=[]


# for i in range(1,6):
#     url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1',
#         'DNT': '1',  # Do Not Track Request Header
#     }

#     session = requests.Session()
#     response = session.get(url, headers=headers)
#     # print(response)

#     soup=BeautifulSoup(response.text,"lxml")


#     box=soup.find("div",class_="DOjaWF gdgoEp")
#     names=box.find_all("div",class_="KzDlHZ")

#     for i in names:
#         name=i.text
#         Product_Name.append(name)
#     # print(len(Product_Name))



#     prices=box.find_all("div",class_="Nx9bqj _4b5DiR")

#     for i in prices:
#         name=i.text
#         Prices.append(name)
#     # print(Prices)



#     desc=box.find_all("ul",class_="G4BRas")

#     for i in desc:
#         name=i.text
#         Description.append(name)
#     # print(Description)   


#     reviews=box.find_all("div",class_="XQDdHH")

#     for i in reviews:
#         name=i.text
#         Reviews.append(name)
#     # print(len(Reviews))    



# df=pd.DataFrame({'Product Name':Product_Name,'Prices':Prices,"Description":Description,"Reviews":Reviews})
# df.to_csv("Flipkart_Mobiles_Under_50000.csv")
















































