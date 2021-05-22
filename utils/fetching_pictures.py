### Automating picture fetching to build fat image database 
### Very messy and just used once to build the dataset on one pc

import flickrapi
import os 
import argparse
from pprint import pprint
import wget 
import urllib.request
from PIL import Image

### Unicode strings for api key and secret
my_key = ''
my_secret = ''

#Equirectangular 360° pictures id - these people have a golden heart
group_id = '44671723@N00'

#Path to local file
LOCAL_PATH = './dataset_360_towns/'

### Set up parser arguments 
parser = argparse.ArgumentParser(description='Different options for fetching pictures on flickr')
parser.add_argument('--keywords', type=str, default='landscape')
parser.add_argument('--sort', type=str, default='relevance', help="Sorting used by flickr to display pictures")
parser.add_argument('--content_type', type=int, default=1, help="Check flickr api guide but basically just means we want photos only")
parser.add_argument('--media', type=str, default='photos') 
parser.add_argument('--safe', type=int, default=1)
parser.add_argument('--per_page', type=int, default=500, help="Number of pictures to go fetch per page")
parser.add_argument('--tags', type=str, default='360°, landscape, equirectangular')
parser.add_argument('--group_id', type=bool, default=True, help='If use group_id or walk through search results')
parser.add_argument('--image_type', type=str, default='landscape', help="Landscape or town or other, corresponds to keywords")
parser.add_argument('--dataroot', type=str, default='./datasets_360_towns/')
args = parser.parse_args()

flickr = flickrapi.FlickrAPI(my_key, my_secret)

def flickr_adventure():
    '''
    We want to go on a flickr adventure.
    To do so let's use some keywords and go and find some cool pics.
    Input :
    - keywords : list of str
    Output:
    - pictures
    '''
    photos = flickr.walk(text=args.keywords,
                         sort=args.sort,
                         media=args.media,
                         per_page=args.per_page,
                         extras='url_c',
                         tags=args.tags,
                         tag_mode='all')
    for photo in photos:
        try:
            url = photo.get('url_c') #get url from photo info imported through the api
            print(url)
        except Exception as e:
            print('failed to download the image')

def flickr_group():
    '''
    Predefined, uses cool equirectangular group set up in flickr.
    '''
    flickr = flickrapi.FlickrAPI(my_key, my_secret, format='parsed-json')
    print(f' Group id being used : {group_id}')
    response = flickr.photos.search(group_id=group_id,
                                    per_page=args.per_page,
                                    media=args.media,
                                    text=args.keywords,
                                    content_type=args.content_type,
                                    safe=args.safe,
                                    sort=args.sort,
                                    page=1,
                                    extras='url_k')
    for i, element in enumerate(response['photos']['photo']):
        #pprint(element['url_c'])
        try:
            #wget.download(element['url_c'], out=LOCAL_PATH)
            image  = Image.open(urllib.request.urlopen(element['url_k']))
            image.save(LOCAL_PATH + f'360_{args.image_type}_{i}.jpg', 'JPEG')

        except Exception as e:
            print('failed to download the image')
        


if args.group_id:
    if __name__ == "__main__":
        flickr_group()
else:
    if __name__ == "__main__":
        flickr_adventure()
