# Lesson 07 HTML Embedding Media
HTML provides a range of elements and attributes to embed media, such as images, ```audio```, and ```video```, into web pages. The ```<img>``` element is used to embed images, while the ```<audio>``` and ```<video>``` elements are used to embed audio and video files, respectively. Additionally, HTML provides elements like ```<iframe>```, ```<embed>```, and ```<object>``` to embed media from external sources, such as YouTube videos or social media content. By using these elements and attributes, developers can create engaging and interactive content for users, while also ensuring accessibility and compatibility across different devices and browsers.

## Introduction
HTML provides several elements and attributes to embed media, such as images, audio, and video, into web pages. This allows developers to create engaging and interactive content for users.

## Embedding Images
The ```<img>``` element is used to embed images into HTML documents. The required attributes are:

- ```src```: specifies the URL of the image file
- ```alt```: provides alternative text for the image, which is displayed if the image cannot be loaded

Example
```
<img src="image.jpg" alt="An image of a sunset">
```

## Embedding Audio
The ```<audio>``` element is used to embed audio files into HTML documents. The required attributes are:

- ```src```: specifies the URL of the audio file
- ```controls```: displays audio controls, such as ```play```, ```pause```, and volume

Example
```
<audio src="audio.mp3" controls>
  Your browser does not support the audio element.
</audio>
```

## Embedding Video
The ```<video>``` element is used to embed video files into HTML documents. The required attributes are:

- ```src```: specifies the URL of the video file
- ```controls```: displays video controls, such as play, pause, and volume
- ```width``` and ```height```: specify the width and height of the video player

Example
```
<video src="video.mp4" controls width="640" height="480">
  Your browser does not support the video element.
</video>
```

## Embedding Media from External Sources
HTML provides several elements to embed media from external sources, such as:

- ```<iframe>```: embeds an HTML document from an external source
- ```<embed>```: embeds a media file from an external source
- ```<object>```: embeds a media file from an external source

Example
```
<iframe src="https://www.youtube.com/embed/VIDEO_ID" width="640" height="480"></iframe>
```

## HTML Embeded Media Tags

| Tag | Use | Code Example |
| --- | --- | --- |
| ```<img>``` | Embeds an image into an HTML document | ```<img src="image.jpg" alt="An image of a sunset">``` |
| ```<audio>``` | Embeds an audio file into an HTML document | ```<audio src="audio.mp3" controls></audio>``` |
|```<video>``` | Embeds a video file into an HTML document | ```<video src="video.mp4" controls width="640" height="480"></video>``` |
| ```<iframe>``` | Embeds an HTML document or media file from an external source | ```<iframe src="https://www.youtube.com/embed/VIDEO_ID" width="640" height="480"></iframe>``` |
| ```<embed>``` | Embeds a media file from an external source | ```<embed src="media.swf" width="640" height="480"></embed>``` |
| ```<object>``` | Embeds a media file from an external source | ```<object data="media.swf" width="640" height="480"></object>``` |
| ```<source>``` | Specifies multiple sources for audio or video elements | ```<video controls><source src="video.mp4" type="video/mp4"><source src="video.ogg" type="video/ogg"></video>``` |
| ```<track>``` | Specifies text tracks for audio or video elements | ```<video controls><track src="captions.vtt" kind="captions" srclang="en" label="English"></video>``` |



## Accessibility Considerations
When embedding media into HTML documents, it's essential to consider accessibility:
- Provide alternative text for images
- Provide transcripts for audio and video content
- Use closed captions for video content
- Ensure media controls are accessible via keyboard navigation

By following these guidelines and using the HTML elements and attributes described above, developers can create engaging and accessible media-rich content for users.
