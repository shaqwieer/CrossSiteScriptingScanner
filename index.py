import Crawler as cr
import Scanner as scan
import Encoding as en
import Encryption as crypt
import Browser as br
from urllib.parse import urlparse


if __name__ == '__main__':
    url = input('enter a url:')
    domain = urlparse(url).netloc
    x = "http://"+domain
    depth = 1
    found= []
    cr.crawler(x,found,depth+2)
    print(found)
    # forms = scan.get_forms(url)
    # print(scan.xss(forms["url"],forms["forms"][0],"<script>alert(1)</script>"))