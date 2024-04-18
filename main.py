import time
import random
import string
from selenium import webdriver

chromedriver_path = '/path/to/your/chromedriver'  # เปลี่ยนเส้นทางไปยัง Chrome WebDriver ในอุปกรณ์ของคุณ

def generate_random_username(prefix, length):
    if length <= len(prefix):
        raise ValueError("Length should be greater than the length of the prefix.")
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(prefix)))
    username = f"{prefix}{random_chars}"
    return username

def generate_random_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def create_account(num_iterations, starting_name, name_length):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ใช้โหมด headless เพื่อไม่แสดง GUI
    options.add_argument('--no-sandbox')  # เพื่อรับสิทธิ์การเข้าถึงไฟล์สำหรับ WebDriver ใน Android
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    for _ in range(num_iterations):
        driver.get("https://www.roblox.com/")
        time.sleep(2)

        # โค้ดส่วนที่เหมือนกันในการสร้างบัญชี

    driver.quit()
    print("Finished creating accounts")

num_iterations = int(input("Enter the number of iterations: "))
starting_name = input("Starting name: ")
name_length = int(input("Name length: "))

create_account(num_iterations, starting_name, name_length)
