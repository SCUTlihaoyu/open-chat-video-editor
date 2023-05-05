from meta_sever import download_image
from PIL import Image


def test_download_image():
    url = "https://cdn.shopify.com/s/files/1/0282/0804/products/pulp_1024x1024.jpg?v=1474264437"
    buffer = download_image(url)
    img = Image.open(buffer)
    img.show()
    
if __name__ == "__main__":
    test_download_image()