

import time
from pages.pim_pg import Pim

def test_Pim_pg(setup):
    driver = setup
    pim = Pim(driver)
    pim.click_pim()
    time.sleep(3)
    pim.click_del()
    time.sleep(3)
    expected='//*[@id="app"]/div[3]/div/div/div/div[2]/p'
    actual="The selected record will be permanently deleted. Are you sure you want to continue?"
    assert actual==expected ,"pass"
