from requests import get

class TheCatAPI:
    def random_cat():
        json_response = get("https://api.thecatapi.com/v1/images/search")
        json_response = json_response.json()
        id = json_response[0]["id"]
        print("The Image id is: ", id)
        url = json_response[0]["url"]
        print("The image URL is: ", url)

        ext = url.split("/")[-1].split(".")[-1]

        r = get(url, stream=True)
        with open(f"{id}.{ext}", 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
    
    def multiple_cats(maximum: int):
        for _ in range(maximum):
            TheCatAPI.random_cat()