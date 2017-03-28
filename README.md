## What is this?
Just a fun CLI that lets you query for something, then re-adjust your queries to Google images afterwards, ever so slightly nudging you in the direction you want to go.

Querying for very extreme words seem to have the biggest effect, and change your movement-vector the most.

An example would be querying for "Nintendo 64", then later querying for "Zelda". This would after a few nudges show you Zelda themed Nintendo 64s, or Zelda on the N64.

Another thing we can do, is remove the query-parameter altogether, which lets us move through the image-space of Google's similar images, based on the directions the related images point us. An example of this is shown below.

### How does Google Similar Images work?
Seemingly, they rely on various filters (or directions towards other images in the space parhaps) to take you in a given direction from your current image. These are represented by the 8 images show to you (where the "View more"-button is) when you highlight an image.
The direction you are taken in, is then constrained by the query-word you have given, so you won't stray into something completely off-topic. This query-parameter can't really be modified mid-search unless you re-forge the query-url manually with respect to the query, and rimg-tag.

## Examples
By removing the constraint of the query-parameter, we sometimes get to apply filters or directions to our selection which doesn't match to where Google think it's taking us.

![step1](https://raw.githubusercontent.com/NegatioN/GoogleImageNavigator/master/image-examples/step1.jpg)

Here we're ready to step into [curly red haired girls](https://www.google.no/search?q=&tbm=isch&tbs=rimg:CZVazid2KFhzIji5IaVxm1t0lDaR5IAK2GPL9gu6spes7r6OaaKi7Hr5T0guqXmnJBKYEyNC2wVEgLweUZ6LIIIoQioSCbkhpXGbW3SUEb6toiYTUexgKhIJNpHkgArYY8sRoL_13Zyt9gUYqEgn2C7qyl6zuvhHGyuW66GjQ7CoSCY5poqLsevlPEcRzkMIEwlBVKhIJSC6peackEpgR5bZ8Xgagg5gqEgkTI0LbBUSAvBGwmzGGxrP5SyoSCR5RnosggihCESXLQfVaN494&tbo=u&sa=X&ved=0ahUKEwiopruD5PfSAhXJDSwKHVD4AQ8Q9C8IGw#imgrc=kASjDbUXdlrxRM:) by pressing the "View more"-button.

![step2](https://raw.githubusercontent.com/NegatioN/GoogleImageNavigator/master/image-examples/step2.jpg)

Instead we end up seeing completely different images from what Google told us it would show, and we seem to have stepped into ["curly hair"-space](https://www.google.no/search?q=&tbm=isch&tbs=rimg:CZAEow21F3ZaIjiUtiwPQcY5PZ57KpctIL2UHychJ6kVH7V2d9nlvA3qrsn3siFLN9SmYhcFplYOZm0brJlAfYoMRyoSCZS2LA9Bxjk9EUr9d6Lh5HiMKhIJnnsqly0gvZQRgAVQuyvCHsgqEgkfJyEnqRUftRHzO0UjpXbvkSoSCXZ32eW8DequEf-6Bcn3fhVCKhIJyfeyIUs31KYRNeWaL9GzwYwqEgliFwWmVg5mbRH_18K9XD8wX0ioSCRusmUB9igxHEUhsZFFDYnBb&tbo=u&sa=X&ved=0ahUKEwj1tPeJ5PfSAhXIfiwKHft4B0IQ9C8IGw), where there are more asian girls for some reason.

![step3](https://raw.githubusercontent.com/NegatioN/GoogleImageNavigator/master/image-examples/step3.jpg)

## Why did I make this?
One of my hunches is that this could theoretically be used to bypass some of the content gating Google does of illegal images. However it seems like in practice, this is exceedingly difficult to do, since you are moving manually through an N-dimensional space. But it does seem like some of the ordinary blocking of content is disregarded.

I reported this to Google, but I believe it was either too difficult to reproduce, or they simply know this is un-exploitable. :) But this tool was a lot of fun to just surf around with anyways, so I thought i'd share it.

## Usage
PS: only tested with python3

Install dependencies with ````pip install -r requirements.txt````

Run ````python main.py````

### Commands
Input a query whenever you're prompted, or type "k" to keep a previous query.

To select a specific image to choose as your direction, input it's position from left -> right, and downwards. (ex: row 3 image 4, if there are 8 pictures on each row, means 2*8+4=20)

Or you may input "r" to get a random direction, or selected image to move towards.

By inputting an empty query (can't happen on the first call), you will move towards the filters or direction in an unconstrained matter.
