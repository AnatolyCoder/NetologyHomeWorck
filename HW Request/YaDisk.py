import requests


class YaUploader:
    URL_FILE_LIST: str = 'https://cloud-api.yandex.net:443/v1/disk/resources/files'
    URL_UPLOAD_LINK: str = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    @property
    def header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_file_list(self):
        response = requests.get(self.URL_FILE_LIST, headers=self.header)
        return response.json()

    def get_upload_link(self,ya_disk_path: str):
        params = {'path': ya_disk_path, 'owervrite': 'true'}
        response = requests.get(self.URL_UPLOAD_LINK, headers=self.header, params=params)
        upload_url = response.json().get('href')
        return  upload_url

    def upload_file(self, ya_disk_path: str, file_path: str):
        upload_link = self.get_upload_link(ya_disk_path)
        with open(file_path, 'rb') as file_obj:
            response = requests.put(upload_link, data=file_obj)
            if response.status_code == 201:
                print('Успешно загрузили!')
        return response.status_code


your_token = ''
uploader = YaUploader(your_token)
uploader.upload_file('','')