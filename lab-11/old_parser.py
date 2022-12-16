import threading
import time

import requests
from bs4 import BeautifulSoup

import config


def img_link_hunter(
        link: str,
        headers: dict = config.headers,
        class_item_box: str = config.class_item_box,
        class_item_img: str = config.class_item_img,
        class_item_info: str = config.class_item_info
) -> dict:
    """
    The function collects all links to images and their captions on a given page.
    Only one page is parsed at a time.
    In case of any errors, an empty dictionary will be returned.
    """
    res = requests.get(link, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_items_box = soup.find_all(class_=class_item_box)

    print(f"On page {link}, there are {len(all_items_box)} items")

    images = {}
    for item_box in all_items_box[:10]:
        src = item_box.find(class_=class_item_img).img.get('src')
        capture = item_box.find(class_=class_item_info).a.text
        images[capture] = src

    print(f"On page {link} {len(images)} images have been downloaded\n")

    return images


def img_downloader(images: dict):
    """The function expects a dictionary of names and links and loads images into a folder `image_heap`."""
    for img_name in images:
        img_title = img_name.replace('/', '-')
        img_body = requests.get(images[img_name])
        with open(f"image_heap/{img_title}.jpg", "wb") as out:
            out.write(img_body.content)


def scroller(
        base_link: str = config.base_url,
        page_counter: int = 3
):
    """The function reads the pages of the resource and processes each page in a separate thread."""
    threads = []
    for i in range(page_counter):
        page_link = base_link + str(i+1)
        images = img_link_hunter(link=page_link)
        thr = threading.Thread(target=img_downloader, args=(images,), daemon=True, name=f'thr-{i+1}')
        threads.append(thr)

    for thr in threads:
        thr.start()
        thr.join(timeout=15)


if __name__ == '__main__':
    start_time = time.time()
    scroller()
    print("--- Execution: %s seconds ---" % (time.time() - start_time))
