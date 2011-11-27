# coding: utf-8

from PIL import ImageOps

from django.conf import settings

from sorl.thumbnail.engines.base import EngineBase
from sorl.thumbnail.engines.pil_engine import Engine as PILEngine


# Set this tone on settings to turn to sepia or any other tone
SEPIA_DEFAULT_TONE = getattr(settings, 'SORL_DEFAULT_SEPIA_TONE', 
    (255, 240, 192))
SEPIA_ALWAYS = getattr(settings, 'SORL_SEPIA_ALWAYS', False)


def _make_linear_ramp(white):
    """ Normalizes a RGB tuple to 0-1 values """ 
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r*i/255, g*i/255, b*i/255))

    return ramp


# Based on http://effbot.org/zone/pil-sepia.htm
class SepiaPILEngineMixin(object):

    def sepia(self, image, tone=None):
        if tone is None:
            tone = SEPIA_DEFAULT_TONE

        sepia = _make_linear_ramp(tone)

        original_mode = image.mode
        # Make grayscale
        image = ImageOps.autocontrast(image.convert('L'))
        # Apply tone
        image.putpalette(sepia)
        # Restore mode
        image = image.convert(original_mode)

        return image
    

class Engine(SepiaPILEngineMixin, PILEngine):
    def create(self, image, geometry, options):
        image = super(Engine, self).create(image, geometry, options)

        tone = None
        if 'sepia_tone' in options:
            tone = [int(val.strip(), 10) 
                for val in options['sepia_tone'].split(',')]

        if SEPIA_ALWAYS:
            return self.sepia(image, tone)
        
        if 'sepia' in options:

            return self.sepia(image, tone)

        return image
