from modules.selenium_custom import DiamondRushSelenium

diamondRush = DiamondRushSelenium()

diamondRush.start_driver()

for i in range(5):
    diamondRush.move_arrow_to('R')
for i in range(3):
    diamondRush.move_arrow_to('D')
for i in range(5):
    diamondRush.move_arrow_to('L')
for i in range(3):
    diamondRush.move_arrow_to('D')

diamondRush.take_screenshot()

diamondRush.driver.quit()