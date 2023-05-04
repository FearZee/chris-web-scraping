from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from excel import create_excel

chop = webdriver.ChromeOptions()
chop.add_extension('extension_1_49_0_0.crx')

driver = webdriver.Chrome(options=chop)
wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
driver.get(f"https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures")
aggree_btn = driver.find_element(By.CSS_SELECTOR, value='[mode=primary]')
if aggree_btn is not None:
    aggree_btn.click()

seasons = ['2018-2019', '2019-2020', '2020-2021', '2021-2022']

def read_website():
    all_matches = []
    game_data = ()
    data = list(game_data)
    try:
        for season in seasons:
            driver.get(f"https://fbref.com/en/comps/9/{season}/schedule/{season}-Premier-League-Scores-and-Fixtures")
            # driver.get(f"https://fbref.com/en/comps/189/{season}/schedule/{season}-Womens-Super-League-Scores-and-Fixtures")
            table = driver.find_element(By.CSS_SELECTOR, value='tbody')



            for trow in table.find_elements(By.CSS_SELECTOR, value='tr:not(.spacer):not(.thead)'):
                # home_team = trow.find_element(By.CSS_SELECTOR, value='[data-stat=home_team]').text
                # away_team = trow.find_element(By.CSS_SELECTOR, value='[data-stat=away_team]').text
                score = trow.find_element(By.CSS_SELECTOR, value='[data-stat=match_report] a')
                driver.execute_script("arguments[0].scrollIntoView();", score)
                # t = trow.find_element(By.XPATH, value="//td[@data-stat='match_report']/a")
                all_matches.append(score.get_attribute('href'))

            for link in all_matches:
                driver.get(link)
                stats = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'team_stats_extra')))
                # stats = driver.find_element(By.ID, 'team_stats_extra')
                home_team = driver.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[1]//div[1]").text
                away_team = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[1]//div[3]").text

                print(home_team)
                print(away_team)

                h_possession = stats.find_element(By.XPATH, "//div[@id='team_stats']//table//tbody//tr[3]//td[1]").text
                a_possession = stats.find_element(By.XPATH, "//div[@id='team_stats']//table//tbody//tr[3]//td[2]").text

                h_shots_on_target = stats.find_element(By.XPATH,
                                                       "//div[@id='team_stats']//table//tbody//tr[7]//td[1]// div[1] / div[1]").text
                a_shots_on_target = stats.find_element(By.XPATH,
                                                       "//div[@id='team_stats']//table//tbody//tr[7]//td[2]// div[1] / div[1]").text

                h_yellow_cards = stats.find_elements(By.XPATH,
                                                     "//div[@id='team_stats']//table//tbody//tr[11]//td[1]//*[@class='yellow_card']")
                a_yellow_cards = stats.find_elements(By.XPATH,
                                                     "//div[@id='team_stats']//table//tbody//tr[11]//td[2]//*[@class='yellow_card']")

                h_yellow_red_cards = stats.find_elements(By.XPATH,
                                                         "//div[@id='team_stats']//table//tbody//tr[11]//td[1]//*[@class='yellow_red_card']")
                a_yellow_red_cards = stats.find_elements(By.XPATH,
                                                         "//div[@id='team_stats']//table//tbody//tr[11]//td[2]//*[@class='yellow_red_card']")

                h_red_cards = stats.find_elements(By.XPATH,
                                                  "//div[@id='team_stats']//table//tbody//tr[11]//td[1]//*[@class='red_card']")
                a_red_cards = stats.find_elements(By.XPATH,
                                                  "//div[@id='team_stats']//table//tbody//tr[11]//td[2]//*[@class='red_card']")

                h_fouls = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[1]//div[4]").text
                a_fouls = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[1]//div[6]").text

                t = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']/div[1]")
                if t.size['height'] < 88 :
                    h_touches = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']/div[1]/div[10]").text
                    a_touches = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[1]//div[12]").text
                else:
                    h_touches = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']/div[1]/div[13]").text
                    a_touches = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[1]//div[15]").text

                h_tackles = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[2]//div[4]").text
                a_tackles = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[2]//div[6]").text

                h_interceptions = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[2]//div[7]").text
                a_interceptions = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[2]//div[9]").text

                h_aerials_won = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[2]//div[10]").text
                a_aerials_won = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[2]//div[12]").text

                h_clearances = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[2]//div[13]").text
                a_clearances = stats.find_element(By.XPATH, "//div[@id='team_stats_extra']//div[2]//div[15]").text

                data.append(
                    [home_team, away_team, h_fouls, a_fouls, h_touches, a_touches, h_tackles, a_tackles, h_interceptions,
                     a_interceptions, h_aerials_won, a_aerials_won, h_clearances, a_clearances, h_yellow_cards,
                     a_yellow_cards, h_yellow_red_cards, a_yellow_red_cards, h_red_cards, a_red_cards, h_possession,
                     a_possession, h_shots_on_target, a_shots_on_target])


            game_data = tuple(data)
            create_excel(game_data, 'Womens-Super-League', season)
    except:
        game_data = tuple(data)
        create_excel(game_data, 'Womens-Super-League', season)
        print("An exception occurred")


read_website()
