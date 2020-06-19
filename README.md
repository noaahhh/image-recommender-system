# image recommender system
![](doc-img/architecture.png?raw=true)

# Requests

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /api/bitirme/images/all | `GET` | Empty | Get all images . |
| /api/bitirme/images/get?img='foo.jpg' | `GET` | Empty | Get similar images of given image. |
 /api/bitirme/images?name='bar.jpg' | `GET` | Empty | Get the image file. |
| /api/bitirme/saveImagesInfo?img='foo.jpg' | `GET` | Empty | Run object detection service . |
