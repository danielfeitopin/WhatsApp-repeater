from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def get_data() -> dict:
    name: str = input('Contact/Group name: ')
    message: str = input('Message: ')
    count: int = int(input('Counter: '))
    return {'name': name, 'message': message, 'count': count}


def send_msg(driver, name: str, message: str, count: int = 1):
    try:
        user = driver.find_element(By.XPATH, f'//span[@title = "{name}"]')
        user.click()
    except:
        print(f'Error opening chat: {name}')
    else:
        text_box = driver.find_element(
            By.XPATH, f'//div[@title = "Type a message"]')
        for _ in range(count):
            text_box.send_keys(message)
            text_box.send_keys(Keys.RETURN)


if __name__ == '__main__':
    
    # Set Path
    PATH_TO_DRIVER: str = 'chromedriver.exe'
        
    # Set Driver
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', 
                                           ['enable-logging'])
    driver = Chrome(PATH_TO_DRIVER,
                    options=chrome_options)
    driver.get('https://web.whatsapp.com')
    sleep(5)
    
    option: str = 'y'
    while option != 'n':
        
        if option == 'y':
            send_msg(driver, **get_data())
        else:
            option = None
            print('Please Enter Valid option!')
        
        option = input('Send more messages?[y/n]: ').casefold()

    driver.close()
    print('Bye!')
