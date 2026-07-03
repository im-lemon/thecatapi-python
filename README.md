## TheCatAPI-python

TheCatAPI is a web API that can be accessed [here](https://api.thecatapi.com), this library is a wrapper around it to easily acces the API.

### Usages:

- Training CV models (On cat images.)

- Placeholder images for applications.


### Legal disclaimer

TheCatAPI-python is not affiliated with the devlopers of the original TheCatAPI, it is simply a wrapper around the API, using requests.

### Syntax:

```bash
# install the library first:

pip install thecatapi-python
```

```python
# Use it in a script:

from thecatapi import TheCatAPI

# get a single cat image.
TheCatAPI.random_cat()


# Get multiple cat images.
TheCatAPI.multiple_cats(max: int)
```