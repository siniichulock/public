from api import PetFriends
from settings import valid_email, valid_password, invalid_email
import os

pf = PetFriends()


def test_get_api_key(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result

def test_update_pet_info_in_list_all_pets(name="Баг", animal_type="кот", age="2"):
    """№1 Тест бага. Изменение данных о питомце, не находящемся в списке 'Мои питомцы'"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_all_pets(auth_key, "")

    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_get_list_all_pets(filter=""):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_all_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0


def test_add_new_pet_without_photo(name="Бублик", animal_type="кот", age="2"):
    """№2 Тест на добавление питомца без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result["name"] == name


def test_add_new_photo_of_a_pet_without_photo(pet_photo='images/Cat_1.jpg'):
    """№3 Тест на добавление фото к уже существующему питомцу"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_all_pets(auth_key, "my_pets")

    status, result = pf.add_new_photo_of_a_pet_without_photo(auth_key, pet_photo, my_pets['pets'][0]['id'])
    assert status == 200
    assert "image/jpeg" in result["pet_photo"]


def test_successful_del_a_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_all_pets(auth_key, "my_pets")

    status, result = pf.successful_del_a_pet(auth_key, my_pets['pets'][0]['id'])
    assert status == 200
    assert "" in result


def test_add_new_pet_with_photo(name="Бублик", animal_type="пес", age="2", pet_photo='images/cat_2.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result["name"] == name


def test_update_pet_info(name="Бублик", animal_type="кот", age="2"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_all_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


def test_get_api_key_with_invalid_email(email=invalid_email, password=valid_password):
    """№4 Тест на получение ключа с использованием некорректного адреса электронной почты"""

    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_list_my_pets(filter="my_pets"):
    """№5 Тест но получение списка 'Мои питомцы'"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_all_pets(auth_key, filter)

    assert status == 200
    assert len(result["pets"]) >= 0


def test_get_list_all_pets_with_invalid_api_key(filter=""):
    """№6 Тест на получение списка питомцев с использованием некорректного api_key"""

    auth_key = {"key": "abc"}
    status, result = pf.get_list_all_pets(auth_key, filter)
    assert status == 403


def test_add_new_photo_of_a_pet_without_photo_uncorrectly_type_of_photo(pet_photo='images/abc'):
    """№7 Тест на добавление файла некорректного формата на место фото, к уже существующему питомцу"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_all_pets(auth_key, "my_pets")

    status, result = pf.add_new_photo_of_a_pet_without_photo(auth_key, pet_photo, my_pets['pets'][0]['id'])
    assert status == 500


def test_add_new_pet_with_uncorrectly_type_of_photo(name="Бублик", animal_type="пес", age="2", pet_photo='images/abc'):
    """№8 Тест на добавление питомца с некорректным форматом фото. Некорректный файл добавляться не должен"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert "" in result["pet_photo"]


def test_update_pet_info_uncorrectly_id(name="Морошка", animal_type="кот", age="7"):
    """№9 Тест для замены данных питомца, с некорректным id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = "io34-kfh"

    status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
    assert status == 400

def test_add_new_pet_with_photo_png(name="Бусинка", animal_type="котик", age="2", pet_photo='images/cat_3.png'):
    """№10 Тест бага. Добавление питомца с фото в формате png. Питомец добавляется, фото не добавляется"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    print (pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert "" in result["pet_photo"]






