# coding: utf-8

from PIL import ImageOps

from django.conf import settings

from sorl.thumbnail.engines.base import EngineBase
from sorl.thumbnail.engines.pil_engine import Engine as PILEngine

# Set this tone on settings to turn to sepia or any other tone
SEPIA_DEFAULT_TONE = getattr(settings, 'SORL_DEFAULTSEPIA_TONE', 
    (255, 240, 192))

# Based on http://effbot.org/zone/pil-sepia.htm
class SepiaPILEngineMixin(object):

    @staticmethod
    def _make_linear_ramp(white):
        """ Normalizes a RGB tuple to 0-1 values """ 
        ramp = []
        r, g, b = white
        for i in range(255):
            ramp.extend((r*i/255, g*i/255, b*i/255))

        return ramp
    
    def sepia(self, image):

        sepia = self._make_linear_ramp(SEPIA_DEFAULT_TONE)

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

        return self.sepia(image)
