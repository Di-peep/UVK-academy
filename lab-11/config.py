from fake_useragent import UserAgent


class_item_box = 'card js-card sc-product'
class_item_img = 'card__image'
class_item_info = 'card__body'
class_item_name = 'products-list-item__name'


base_url = 'https://www.foxtrot.com.ua/ru/shop/mobilnye_telefony_samsung.html?page='

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;"
              "q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": UserAgent()['google_chrome']
}
