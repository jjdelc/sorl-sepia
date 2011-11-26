# Sorl-sepia

Sorl-thumbnail engine to convert images to sepia.
Currently only supports PIL engine

## Instalation

Add 'sorl_sepia.engine.Engine' as your THUMBNAIL_ENGINE

To change the sepia tone, set the SORL_DEFAULTSEPIA_TONE settings which is an (int, int, int) tuple.

SORL_DEFAULTSEPIA_TONE = (255, 240, 192) # Default value

# TODO

- PgMagick engine
