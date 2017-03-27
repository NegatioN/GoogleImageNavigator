## Examples
By removing the constraint of the query-parameter, we sometimes get to apply filters or directions to our selection which doesn't match to where Google think it's taking us.

![step1](https://raw.githubusercontent.com/NegatioN/GoogleImageNavigator/master/image-examples/step1.jpg)

Here we're about ready to step into (curly red haired girls)[https://www.google.no/search?q=&tbm=isch&tbs=rimg:CZVazid2KFhzIji5IaVxm1t0lDaR5IAK2GPL9gu6spes7r6OaaKi7Hr5T0guqXmnJBKYEyNC2wVEgLweUZ6LIIIoQioSCbkhpXGbW3SUEb6toiYTUexgKhIJNpHkgArYY8sRoL_13Zyt9gUYqEgn2C7qyl6zuvhHGyuW66GjQ7CoSCY5poqLsevlPEcRzkMIEwlBVKhIJSC6peackEpgR5bZ8Xgagg5gqEgkTI0LbBUSAvBGwmzGGxrP5SyoSCR5RnosggihCESXLQfVaN494&tbo=u&sa=X&ved=0ahUKEwiopruD5PfSAhXJDSwKHVD4AQ8Q9C8IGw#imgrc=kASjDbUXdlrxRM:].

![step2](https://raw.githubusercontent.com/NegatioN/GoogleImageNavigator/master/image-examples/step2.jpg)

Instead we end up seeing completely different images from what Google told us it would show, and we seem to have stepped into ("curly hair"-space)[https://www.google.no/search?q=&tbm=isch&tbs=rimg:CZAEow21F3ZaIjiUtiwPQcY5PZ57KpctIL2UHychJ6kVH7V2d9nlvA3qrsn3siFLN9SmYhcFplYOZm0brJlAfYoMRyoSCZS2LA9Bxjk9EUr9d6Lh5HiMKhIJnnsqly0gvZQRgAVQuyvCHsgqEgkfJyEnqRUftRHzO0UjpXbvkSoSCXZ32eW8DequEf-6Bcn3fhVCKhIJyfeyIUs31KYRNeWaL9GzwYwqEgliFwWmVg5mbRH_18K9XD8wX0ioSCRusmUB9igxHEUhsZFFDYnBb&tbo=u&sa=X&ved=0ahUKEwj1tPeJ5PfSAhXIfiwKHft4B0IQ9C8IGw], where there are more asian girls for some reason.

![step3](https://raw.githubusercontent.com/NegatioN/GoogleImageNavigator/master/image-examples/step3.jpg)

## Usage
PS: only tested with python3

Install dependencies with ````pip install -r requirements.txt````

Run ````python main.py````

### Commands
Input a query whenever you're prompted, or type "k" to keep a previous query.

To select a specific image to choose as your direction, input it's position from left -> right, and downwards. (ex: row 3 image 4, if there are 8 pictures on each row, means 2*8+4=20)

Or you may input "r" to get a random direction, or selected image to move towards.

By inputting an empty query (can't happen on the first call), you will move towards the filters or direction in an unconstrained matter.
