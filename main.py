# selenium for web driving
from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_page1(file):
    # Using Chrome to access web
    driver = webdriver.Chrome()
    href_list = []
    wait_time = 10

    fileobject = open(file, "w+")
    for page in range(1, 2):

        if page == 1:
            url = 'https://www.trucksandauto.com/auctions/20756-January-31st-%E2%80%A2-Pasco----Online-Only'
        else:
            page_num = str(page)
            url = 'https://www.trucksandauto.com/auctions/20756-January-31st-%E2%80%A2-Pasco----Online-Only?page='
            url += page_num

        driver.get(url)

        # enter search list to search box
        username_form = driver.find_element(By.NAME, 'search')
        username_form.send_keys('Mazda')

        # click on search button
        driver.implicitly_wait(wait_time + 10)
        search_button = driver.find_element(By.CLASS_NAME, 'input-group-addon')
        search_button.click()

        driver.implicitly_wait(wait_time + 10)

        # identify elements with tag-name <a>
        links = driver.find_elements(By.TAG_NAME, 'a')

        # traverse list
        # for lnk in links:
        #     # get_attribute() to get all href
        #     href = lnk.get_attribute('href')
        #     if href is not None:
        #         href_list.append(href)
    #
    # # remove duplicates
    # res = [*set(href_list)]
    #
    # for r in res:
    #     fileobject.write(r + "\n")
    #     print(r)

    return


if __name__ == '__main__':
    # file_name = str(input("File to populate: "))
    # website = str(input("Auction to parse: "))
    # key_words = []
    # print("Enter '0' to finish list.")
    # while input != 0:
    #     name = str(input("Vehicle : "))
    #     key_words.append(name)
    #
    # parse_page1(file_name, website, key_words)
    parse_page1("cars.txt")
