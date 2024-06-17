import sys
import requests
import asyncio
import time
import os
import validators

START_TIME = time.time()
NAME_DIR = 'download_images'


async def download(some_url: str):
    response = requests.get(some_url).content
    file_name = f'{NAME_DIR}/{some_url.split("/")[-1]}'
    with open(file_name, 'wb') as f_img:
        f_img.write(response)
    print(f'Downloaded {some_url} in {time.time() - START_TIME:.2f}seconds')


async def main():
    tasks = []

    for url in sys.argv[1:]:
        check_format = url.split('/')[-1]
        if validators.url(url) and check_format.endswith('jpg') or check_format.endswith('png'):
            tasks.append(asyncio.create_task(download(url)))
        else:
            print('Введите корректный адрес для скачивания img')
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print(f'Программа завершилась через: {time.time() - START_TIME:.2f}seconds')