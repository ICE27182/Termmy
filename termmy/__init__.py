
from .pixel import Pixel32, Pixel24
from .frame import Frame, Frame24
from .text_tag import TextTag
from .settings import Settings, DisplaySetting

def display_frame(frame:Frame24, display_settings:int|Settings):
    
    pass

__all__ = ["Settings", "TextTag", "DisplaySetting"]