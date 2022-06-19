import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):

        headers = {
            "email": email,
            "password": password
        }
        res = requests.get(self.base_url + "api/key", headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_all_pets(self, auth_key, filter):
        headers = {"auth_key": auth_key['key']}
        filter = {"filter": filter}
        res = requests.get(self.base_url + "api/pets", headers=headers, params=filter)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet_without_photo(self, auth_key, name, animal_type, age) -> json:
        """Добавляем питомца без фото. Для age формат str"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + "api/create_pet_simple", headers=headers, data=data)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_photo_of_a_pet_without_photo(self, auth_key, pet_photo, pet_id) -> json:
        """Добавляем фото к уже созданному питомцу"""

        data = MultipartEncoder(
            fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')})
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + "api/pets/set_photo/" + pet_id, headers=headers, data=data)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def successful_del_a_pet(self, auth_key, pet_id):

        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + "api/pets/" + pet_id, headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet_with_photo(self, auth_key, name, animal_type, age, pet_photo) -> json:
        """Добавляем питомца c фото. Для age формат str"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + "api/pets", headers=headers, data=data)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key, pet_id, name, animal_type, age):
        """Обновление данных по указанному id. Возвращает 200 и обновленные данные в Json"""

        headers = {'auth_key': auth_key['key']}
        data = {
                'name': name,
                'animal_type': animal_type,
                'age': age
            }
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result






