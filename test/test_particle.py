#
# Los Cocos: Particle Example
# http://code.google.com/p/los-cocos/
#

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from cocos.director import *
from cocos.particle import *
from cocos.layer import *
from cocos.scene import *

class ParticleLayer( AnimationLayer ):

    def __init__( self ):
        super( ParticleLayer, self ).__init__()

        p1 = ParticleEmitter( 60, (320,240) )
        p2 = ParticleEmitter( 60, (120,340) )
        p3 = ParticleEmitter( 60, (420,340) )

        self.add( p1, p2, p3 )


if __name__ == "__main__":
    director.init( resizable=True)
    director.run( Scene( ParticleLayer()) )