from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_all_my_pets(signup_form):
    names, types, age, unique_name = [], [], [], []
    flag_clone = True
    driver = signup_form
    WebDriverWait(driver, 5).until(EC.title_contains, "PetFriends: My Pets")
    driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()
    driver.implicitly_wait(2)
    driver.find_elements_by_tag_name('td')
    len_list_of_pets = len(driver.find_elements_by_tag_name('tr')) - 1
    statistic_user = driver.find_element_by_class_name('\.col-sm-4.left')

    for i in range(len_list_of_pets):
        names.append(driver.find_element_by_xpath(f'//*[@id="all_my_pets"]/table/tbody/tr[{i + 1}]/td[1]').text)
        types.append(driver.find_element_by_xpath(f'//*[@id="all_my_pets"]/table/tbody/tr[{i + 1}]/td[2]').text)
        age.append(driver.find_element_by_xpath(f'//*[@id="all_my_pets"]/table/tbody/tr[{i + 1}]/td[3]').text)

    # находим питомцев без фото, используя тег и атрибут со значением внутри него
    img = driver.find_elements_by_css_selector("img[src='']")

    # уникальные имена добавляем в новый список, если имя не уникально проверяем совпадает ли при этом порода и возраст
    for i in range(len_list_of_pets):
        if names[i] not in unique_name:
            unique_name.append(names[i])
        elif types[i] == types[names.index(names[i])]:
            if age[i] == age[names.index(names[i])]:
                flag_clone = False

    assert len_list_of_pets == int(statistic_user.text.split()[2])
    assert (len_list_of_pets - len(img)) >= len(img)
    assert len(names) == len(types) and len(types) == len(age)
    assert len(names) == len(unique_name)
    assert flag_clone == True
