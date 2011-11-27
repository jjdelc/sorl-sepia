# Sorl-sepia

Sorl-thumbnail engine to convert images to sepia.
Currently only supports PIL engine

## Instalation and usage

Add 'sorl_sepia.engine.Engine' as your THUMBNAIL_ENGINE

If you want all your thumbnails to be sepia, set the SORL_SEPIA_ALWAYS settings to True
SORL_SEPIA_ALWAYS = True # Default value is False

To change the sepia tone, set the SORL_DEFAULT_SEPIA_TONE settings which is an (int, int, int) tuple.

SORL_DEFAULT_SEPIA_TONE = (255, 240, 192) # Default value

Alternatively, if you want to enable sepia and tone per image, use the 'sepia' and 'sepia_tone' thumbnail templatetag options:

{% thumbnail my_pic.image_file "100x100" sepia=True sepia_tone="255,240,193" as thumb %}

* `sepia` set to True to convert such picture to sepia
* `sepia_tone` is a comma separated string indicating RGB values

# TODO

- PgMagick engine
