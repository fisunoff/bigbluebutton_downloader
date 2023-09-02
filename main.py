import requests


def download_svgs(url: str) -> int:
    """
    Скачивание svg с сервера конференций

    :param url: url с вырезанным номером слайда
    :return: количество скачанных файлов
    """
    id = 1
    r = requests.get(url + str(id))
    status = r.status_code
    while status == 200:
        with open(f"img/{id}.svg", "wb") as f:
            f.write(r.content)
        id += 1
        r = requests.get(base_url + str(id))
        status = r.status_code
    return id - 1


sample_url = input("Введите ссылку на любой слайд: ")
base_url = "/".join(sample_url.split("/")[:-1]) + "/"  # отрезает номер слайда
print(base_url)

download_result = download_svgs(base_url)
if download_result > 0:
    print(f"Скачано слайдов: {download_result}")
else:
    print("Ничего не скачано! Проверьте корректность ссылки ")