import bpy, re, mathutils
from bpy.app.handlers import persistent
from math import sqrt, pow, sin, cos, asin, acos
from math import pi as M_PI
M_PI_2 = M_PI * 2

bl_info = {
  'name': 'Driver Functions',
  'version': (1, 0, 0),
  'author': 'passivestar',
  'blender': (3, 0, 0),
  'description': 'Adds useful functions to the driver namespace',
  'category': 'Animation'
}

# @Easings

class easings(object):
  def __init__(self):
    pass

  @staticmethod
  def in_quad(p):
    return p * p

  @staticmethod
  def out_quad(p):
    return -(p * (p - 2))

  @staticmethod
  def in_out_quad(p):
    if p < 0.5:
      return 2 * p * p
    return (-2 * p * p) + (4 * p) - 1

  @staticmethod
  def in_cubic(p):
    return p * p * p

  @staticmethod
  def out_cubic(p):
    f = p - 1
    return f * f * f + 1

  @staticmethod
  def in_out_cubic(p):
    if p < 0.5:
      return 4 * p * p * p
    else:
      f = (2 * p) - 2
      return 0.5 * f * f * f + 1

  @staticmethod
  def in_quart(p):
    return p * p * p * p

  @staticmethod
  def out_quart(p):
    f = p - 1
    return f * f * f * (1 - p) + 1

  @staticmethod
  def in_out_quart(p):
    if p < 0.5:
      return 8 * p * p * p * p
    else:
      f = p - 1
      return -8 * f * f * f * f + 1

  @staticmethod
  def in_quint(p):
    return p * p * p * p * p

  @staticmethod
  def out_quint(p):
    f = p - 1
    return f * f * f * f * f + 1

  @staticmethod
  def in_out_quint(p):
    if p < 0.5:
      return 16 * p * p * p * p * p
    else:
      f = (2 * p) - 2
      return  0.5 * f * f * f * f * f + 1

  @staticmethod
  def in_sin(p):
    return sin((p - 1) * M_PI_2) + 1

  @staticmethod
  def out_sin(p):
    return sin(p * M_PI_2)

  @staticmethod
  def in_out_sin(p):
    return 0.5 * (1 - cos(p * M_PI))

  @staticmethod
  def in_circle(p):
    return 1 - sqrt(1 - (p * p))

  @staticmethod
  def out_circle(p):
    return sqrt((2 - p) * p)

  @staticmethod
  def in_out_circle(p):
    if p < 0.5:
      return 0.5 * (1 - sqrt(1 - 4 * (p * p)))
    else:
      return 0.5 * (sqrt(-((2 * p) - 3) * ((2 * p) - 1)) + 1)

  @staticmethod
  def in_exp(p):
    return p if p == 0 else pow(2, 10 * (p - 1))

  @staticmethod
  def out_exp(p):
    return p if p == 1 else 1 - pow(2, -10 * p)

  @staticmethod
  def in_out_exp(p):
    if p == 0 or p == 1:
      return p
    if p < 0.5:
      return 0.5 * pow(2, (20 * p) - 10)
    else:
      return -0.5 * pow(2, (-20 * p) + 10) + 1

  @staticmethod
  def in_elastic(p):
    return sin(13 * M_PI_2 * p) * pow(2, 10 * (p - 1))

  @staticmethod
  def out_elastic(p):
    return sin(-13 * M_PI_2 * (p + 1)) * pow(2, -10 * p) + 1

  @staticmethod
  def in_out_elastic(p):
    if p < 0.5:
      return 0.5 * sin(13 * M_PI_2 * (2 * p)) * pow(2, 10 * ((2 * p) - 1))
    else:
      return 0.5 * (sin(-13 * M_PI_2 * ((2 * p - 1) + 1)) * pow(2, -10 * (2 * p - 1)) + 2)

  @staticmethod
  def in_back(p):
    return p * p * p - p * sin(p * M_PI)

  @staticmethod
  def out_back(p):
    f = 1 - p
    return 1 - (f * f * f - f * sin(f * M_PI))

  @staticmethod
  def in_out_back(p):
    if p < 0.5:
      f = 2 * p
      return 0.5 * (f * f * f - f * sin(f * M_PI))
    else:
      f = (1 - (2 * p - 1))
      return 0.5 * (1 - (f * f * f - f * sin(f * M_PI))) + 0.5

  @staticmethod
  def in_bounce(p):
    return 1 - easings.out_bounce(1 - p)

  @staticmethod
  def out_bounce(p):
    if p < 4 / 11:
      return (121 * p * p) / 16
    elif p < 8 / 11:
      return (363 / 40 * p * p) - (99 / 10 * p) + 17 / 5
    elif p < 9 / 10:
      return (4356 / 361 * p * p) - (35442 / 1805 * p) + 16061 / 1805
    else:
      return (54 / 5 * p * p) - (513 / 25 * p) + 268 / 25

  @staticmethod
  def in_out_bounce(p):
    if p < 0.5:
      return 0.5 * easings.in_bounce(p * 2)
    else:
      return 0.5 * easings.out_bounce(p * 2 - 1) + 0.5

# @Functions

# Current object's index derived from the name
def i(obj):
  match = re.search('(\d+)$', obj.name)
  return int(match.group(1)) if match else 0

# Get object by name
def obj(name):
  return bpy.data.objects[name]

# Transforms
def loc(name): return bpy.data.objects[name].location
def rot(name): return bpy.data.objects[name].rotation
def scale(name): return bpy.data.objects[name].scale
def dloc(name): return bpy.data.objects[name].delta_location
def drot(name): return bpy.data.objects[name].delta_rotation
def dscale(name): return bpy.data.objects[name].delta_scale

# Noise
def rand(n): return mathutils.noise.noise((n, 0, 0))

# How far into the timeline we are
def t():
  scene = bpy.context.scene
  return scene.frame_current / scene.frame_end

functions_and_classes = (
  i, obj, loc, rot, scale, dloc, drot, dscale, rand, t, easings
)

@persistent
def load_handler(dummy):
  dn = bpy.app.driver_namespace
  for el in functions_and_classes:
    dn[el.__name__] = el
  # Shortcuts
  dn['es'] = dn['easings']

def register():
  load_handler(None)
  bpy.app.handlers.load_post.append(load_handler)

def unregister():
  bpy.app.handlers.load_post.remove(load_handler)

if __name__ == '__main__': register()