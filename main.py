from image_scraper import ImageScraper
import html_generator
import scraper_io

URL = 'https://www.google.com/search?q=python&sxsrf=APq-WBvHgTgLbfxvn0uy0_ZxC-NrxeCyhQ:1644486375751&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjGiY6S7fT1AhWE_qQKHRavAeUQ_AUoAXoECAIQAw&biw=1440&bih=796&dpr=2'

if __name__ == '__main__':
    scr = ImageScraper()
    srcs = scr.scrap_image(URL)
    html = html_generator.generate_images_html(srcs=srcs)
    scraper_io.save_and_open(file=html, name='index.html')