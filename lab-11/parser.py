import asyncio
import time

import aiohttp
from bs4 import BeautifulSoup

import config


async def img_link_hunter(
        session: aiohttp.ClientSession,
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
    async with session.get(url=link, headers=headers) as response:
        page_text = await response.text()
        soup = BeautifulSoup(page_text, 'html.parser')
        all_items_box = soup.find_all(class_=class_item_box)

        print(f"On page {link}, there are {len(all_items_box)} items")

        images = {}
        for item_box in all_items_box[:10]:
            src = item_box.find(class_=class_item_img).img.get('src')
            capture = item_box.find(class_=class_item_info).a.text
            images[capture] = src

        print(f"On page {link} {len(images)} images have been downloaded\n")

        return images


async def img_downloader(
        session: aiohttp.ClientSession,
        images: dict,
        headers: dict = config.headers
):
    """The function expects a dictionary of names and links and loads images into a folder `image_heap`."""
    for img_name in images:
        img_title = img_name.replace('/', '-')
        async with session.get(url=images[img_name], headers=headers) as image:
            with open(f"image_heap/{img_title}.jpg", "wb") as out:
                out.write(await image.read())


async def scroller(
        base_link: str = config.base_url,
        page_counter: int = 3
):
    """The function reads the pages of the resource and processes each page using asyncio."""
    tasks = []
    async with aiohttp.ClientSession() as session:
        for page in range(page_counter):
            page_link = base_link + str(page+1)
            tasks.append(asyncio.create_task(img_link_hunter(session=session, link=page_link)))

        links_dicts = await asyncio.gather(*tasks)

        for links_dict in links_dicts:
            tasks.append(asyncio.create_task(img_downloader(session=session, images=links_dict)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(scroller())
    print("--- Execution: %s seconds ---" % (time.time() - start_time))
