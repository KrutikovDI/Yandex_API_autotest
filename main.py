import requests

class YDisk:
    url = 'https://cloud-api.yandex.net/v1/disk/'
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json', 
            'Authorization': 'OAuth {}'.format("y0_AgAAAAAObWe6AADLWwAAAADa5IEtx9pRvkYgRhOex53Nu9Q2X-GbJcA")
        }

    def recording_yd(self, name_folder):
        upload_url_put = self.url + 'resources'
        params_folder_creation = {'path': name_folder}
        folder_creation = requests.put(upload_url_put, headers=self.headers, params=params_folder_creation)
        return folder_creation.status_code
    

if __name__ == '__main__':    
    yd_photos = YDisk()
    print(yd_photos.recording_yd('11111'))
