# -*- coding: utf-8 -*-
#Copyright (c) 2011, Walter Bender, Paulina Clares, Chris Rowe
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

# The challenges are arrays:
# [a fraction to display on the ball,
#  the number of segments in the bar,
#  the number of times this challenge has been played]

EASY = [['1/2', 2, 0], ['1/3', 3, 0], ['1/4', 4, 0],
        ['2/4', 4, 0], ['2/3', 3, 0], ['3/4', 4, 0]]
MEDIUM = [['1/6', 6, 0], ['2/6', 6, 0], ['3/6', 6, 0],
          ['4/6', 6, 0], ['5/6', 6, 0],
          ['1/8', 8, 0], ['2/8', 8, 0],  ['3/8', 8, 0],
          ['4/8', 8, 0], ['5/8', 8, 0],  ['6/8', 8, 0],
          ['7/8', 8, 0]]
HARD = [['1/12', 12, 0], ['2/12', 12, 0], ['3/12', 12, 0],
        ['4/12', 12, 0], ['3/12', 12, 0], ['6/12', 12, 0],
        ['7/12', 12, 0], ['8/12', 12, 0], ['9/12', 12, 0],
        ['10/12', 12, 0], ['11/12', 12, 0],
        ['1/5', 10, 0], ['2/5', 10, 0], ['3/5', 10, 0],
        ['4/5', 10, 0],
        ['1/10', 10, 0], ['2/10', 10, 0], ['3/10', 10, 0],
        ['4/10', 10, 0], ['5/10', 10, 0], ['6/10', 10, 0],
        ['7/10', 10, 0], ['8/10', 10, 0], ['9/10', 10, 0],
        ['1/16', 4, 0], ['2/16', 4, 0], ['3/16', 4, 0],
        ['4/16', 4, 0], ['5/16', 4, 0], ['6/16', 4, 0],
        ['7/16', 4, 0], ['8/16', 4, 0], ['9/16', 4, 0],
        ['10/16', 4, 0], ['11/16', 4, 0], ['12/16', 4, 0],
        ['13/16', 4, 0], ['14/16', 4, 0], ['15/16', 4, 0]]
EXPERT = 100  # after some number of correct answers, don't segment the bar
BAR_HEIGHT = 25
STEPS = 100.  # number of time steps per bounce rise and fall
STEP_PAUSE = 50  # milliseconds between steps
BOUNCE_PAUSE = 3000  # milliseconds between bounces
DX = 10  # starting step size for horizontal movement
DDX = 1.25  # acceleration during keypress
ANIMATION = {10: (0, 1), 15: (1, 2), 20: (2, 1), 25: (1, 2), 30: (2, 1),
             35: (1, 2), 40: (2, 3), 45: (3, 4), 50: (4, 3), 55: (3, 4),
             60: (4, 3), 65: (3, 4), 70: (4, 5), 75: (5, 6), 80: (6, 5),
             85: (5, 6), 90: (6, 7)}
ACCELEROMETER_DEVICE = '/sys/devices/platform/lis3lv02d/position'
CRASH = 'crash.ogg'  # wrong answer sound
LAUGH = 'bottle.ogg'  # correct answer sound
BUBBLES = 'bubbles.ogg'  # Easter Egg sound
# Easter Egg animation graphics
TRANSFORMS = ['<g>',
              '<g transform="matrix(0.83251323,0.17764297,-0.48065174, \
1.0074555,27.969568,-8.7531294)">',
              '<g transform="matrix(-0.83251323,0.17764297,0.48065174, \
1.0074555,57.030432,-8.7531294)">',
              '<g transform="matrix(0.57147881,-0.357582,-0.32994345, \
0.96842187,32.525583,15.686767)">',
              '<g transform="matrix(-0.57147881,-0.357582,0.32994345, \
0.96842187,52.474417,15.686767)">',
              '<g transform="matrix(0.39557109,-0.57943591,-0.22838308, \
0.86196565,35.595823,29.733447)">',
              '<g transform="matrix(-0.39557109,-0.57943591,0.22838308, \
0.86196565,49.404177,29.733447)">',
              '<g transform="matrix(1,0,0,0.08410415,0,73.873449)">']
PUNCTURE = \
'  <g \
     transform="translate(2.5316175, -8)">\
    <path \
       d="m 33.19688,68.961518 c 3.900378,7.602149 10.970659,7.634416 \
13.708164,7.432138"\
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:round;\
stroke-miterlimit:4" />\
    <path \
       d="m 33.031721,77.05429 c 8.199837,0.123635 12.819227,-7.570626 \
12.882372,-8.423089" \
       style="fill:none;stroke:#000000;stroke-width:2;stroke-linecap:round;\
stroke-miterlimit:4" />\
  </g>'
AIR = \
'  <g \
     transform="matrix(0.63786322,0,0,0.64837179,17.379518,68.534252)"> \
    <path \
       d="M 39.054054,1.75 C 37.741313,16.51834 25.926641,23.082047 \
25.926641,23.082047 l 0,0" \
       style="fill:none;stroke:#0ac9fb;stroke-width:6.0;stroke-linecap:round;\
stroke-miterlimit:4;" />\
    <path \
       d="m 39.710425,1.75 c 1.312741,14.76834 13.127413,21.332047 \
13.127413,21.332047 l 0,0" \
       style="fill:none;stroke:#0ac9fb;stroke-width:6.0;stroke-linecap:round;\
stroke-miterlimit:4" />\
    <path \
       d="m 39.054054,1.75 c 1.969112,3.281854 -0.656371,20.347491 \
-0.656371,20.347491 l 0,0" \
       style="fill:none;stroke:#0ac9fb;stroke-width:6.0;stroke-linecap:round;\
stroke-miterlimit:4" />\
  </g>'

import gtk
from random import uniform
import os
import gobject

from play_audio import play_audio_from_file

from gettext import gettext as _

import logging
_logger = logging.getLogger('fractionbounce-activity')

try:
    from sugar.graphics import style
    GRID_CELL_SIZE = style.GRID_CELL_SIZE
except ImportError:
    GRID_CELL_SIZE = 0

from sprites import Sprites, Sprite


def generate_xo_svg(scale=1.0, colors=["#C0C0C0", "#282828"]):
    ''' Returns an SVG string representing an XO image '''
    return _svg_header(55, 55, scale) + \
           _svg_xo(colors[0], colors[1]) + \
           _svg_footer()


def svg_str_to_pixbuf(svg_string):
    ''' Load pixbuf from SVG string '''
    pl = gtk.gdk.PixbufLoader('svg')
    pl.write(svg_string)
    pl.close()
    pixbuf = pl.get_pixbuf()
    return pixbuf


def _svg_rect(w, h, rx, ry, x, y, fill, stroke):
    ''' Returns an SVG rectangle '''
    svg_string = '       <rect\n'
    svg_string += '          width="%f"\n' % (w)
    svg_string += '          height="%f"\n' % (h)
    svg_string += '          rx="%f"\n' % (rx)
    svg_string += '          ry="%f"\n' % (ry)
    svg_string += '          x="%f"\n' % (x)
    svg_string += '          y="%f"\n' % (y)
    svg_string += _svg_style('fill:%s;stroke:%s;' % (fill, stroke))
    return svg_string


def _svg_xo(fill, stroke, width=3.5):
    ''' Returns XO icon graphic '''
    svg_string = '<path d="M33.233,35.1l10.102,10.1c0.752,\
0.75,1.217,1.783,1.217,2.932\
   c0,2.287-1.855,4.143-4.146,4.143c-1.145,0-2.178-0.463-2.932-1.211L27.372,\
40.961l-10.1,10.1c-0.75,0.75-1.787,1.211-2.934,1.211\
   c-2.284,0-4.143-1.854-4.143-4.141c0-1.146,0.465-2.184,\
1.212-2.934l10.104-10.102L11.409,24.995\
   c-0.747-0.748-1.212-1.785-1.212-2.93c0-2.289,1.854-4.146,4.146-4.146c1.143,\
0,2.18,0.465,2.93,1.214l10.099,10.102l10.102-10.103\
   c0.754-0.749,1.787-1.214,2.934-1.214c2.289,0,4.146,1.856,4.146,4.145c0,\
1.146-0.467,2.18-1.217,2.932L33.233,35.1z" '
    svg_string += _svg_style('fill:%s;stroke:%s;stroke_width:%f' % (fill,
                                                                    stroke,
                                                                    width))
    svg_string += '\n<circle cx="27.371" cy="10.849" r="8.122" '
    svg_string += _svg_style('fill:%s;stroke:%s;stroke_width:%f' % (fill,
                                                                    stroke,
                                                                    width))
    return svg_string


def _svg_header(w, h, scale, hscale=1.0):
    ''' Returns SVG header; some beads are elongated (hscale) '''
    svg_string = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    svg_string += '<!-- Created with Python -->\n'
    svg_string += '<svg\n'
    svg_string += '   xmlns:svg="http://www.w3.org/2000/svg"\n'
    svg_string += '   xmlns="http://www.w3.org/2000/svg"\n'
    svg_string += '   version="1.0"\n'
    svg_string += '   width="%f"\n' % (w * scale)
    svg_string += '   height="%f">\n' % (h * scale * hscale)
    svg_string += '<g\n       transform="matrix(%f,0,0,%f,0,0)">\n' % (
                                  scale, scale)
    return svg_string


def _svg_footer():
    ''' Returns SVG footer '''
    svg_string = '</g>\n'
    svg_string += '</svg>\n'
    return svg_string


def _svg_style(extras=''):
    ''' Returns SVG style for shape rendering '''
    return 'style="%s"/>\n' % (extras)


def svg_from_file(pathname):
    ''' Read SVG string from a file '''
    f = file(pathname, 'r')
    svg = f.read()
    f.close()
    return(svg)


def _extract_svg_payload(fd):
    """Returns everything between <svg ...> and </svg>"""
    payload = ''
    looking_for_start_svg_token = True
    looking_for_close_token = True
    looking_for_end_svg_token = True
    for line in fd:
        if looking_for_start_svg_token:
            if line.find('<svg') < 0:
                continue
            looking_for_start_svg_token = False
            line = line.split('<svg', 1)[1]
        if looking_for_close_token:
            if line.find('>') < 0:
                continue
            looking_for_close_token = False
            line = line.split('>', 1)[1]
        if looking_for_end_svg_token:
            if line.find('</svg>') < 0:
                payload += line
                continue
            payload += line.split('</svg>')[0]
            break
    return payload


class Bounce():
    ''' The Bounce class is used to define the ball and the user
    interaction. '''

    def __init__(self, canvas, path, parent=None):
        ''' Initialize the canvas and set up the callbacks. '''
        self.activity = parent

        if parent is None:        # Starting from command line
            self.sugar = False
            self.canvas = canvas
        else:                     # Starting from Sugar
            self.sugar = True
            self.canvas = canvas
            parent.show_all()

        self.canvas.grab_focus()

        if os.path.exists(ACCELEROMETER_DEVICE):
            self.accelerometer = True
        else:
            self.accelerometer = False

        self.canvas.set_flags(gtk.CAN_FOCUS)
        self.canvas.add_events(gtk.gdk.BUTTON_PRESS_MASK)
        self.canvas.add_events(gtk.gdk.BUTTON_RELEASE_MASK)
        self.canvas.add_events(gtk.gdk.POINTER_MOTION_MASK)
        self.canvas.add_events(gtk.gdk.KEY_PRESS_MASK)
        self.canvas.add_events(gtk.gdk.KEY_RELEASE_MASK)
        self.canvas.connect('expose-event', self._expose_cb)
        self.canvas.connect('button-press-event', self._button_press_cb)
        self.canvas.connect('button-release-event', self._button_release_cb)
        self.canvas.connect('key_press_event', self._keypress_cb)
        self.canvas.connect('key_release_event', self._keyrelease_cb)
        self.width = gtk.gdk.screen_width()
        self.height = gtk.gdk.screen_height() - GRID_CELL_SIZE
        self.sprites = Sprites(self.canvas)
        self.scale = gtk.gdk.screen_height() / 900.0
        self.timeout = None

        self.buddies = []  # used for sharing
        self.my_turn = False
        self.select_a_fraction = False

        self.easter_egg = int(uniform(1, 100))

        # Find paths to sound files
        self.path_to_success = os.path.join(path, LAUGH)
        self.path_to_failure = os.path.join(path, CRASH)
        self.path_to_bubbles = os.path.join(path, BUBBLES)

        self._create_sprites(path)

        self.challenges = []
        for challenge in EASY:
            self.challenges.append(challenge)
        self.fraction = 0.5  # the target of the current challenge
        self.label = '1/2'  # the label
        self.count = 0  # number of bounces played
        self.correct = 0  # number of correct answers
        self.press = None  # sprite under mouse click
        self.mode = 'fractions'
        self.new_bounce = False
        self.n = 0

        self.dx = 0.  # ball horizontal trajectory
        # acceleration (with dampening)
        self.ddy = (6.67 * self.height) / (STEPS * STEPS)
        self.dy = self.ddy * (1 - STEPS) / 2.  # initial step size

    def _create_sprites(self, path):
        ''' Create all of the sprites we'll need '''
        self.smiley_graphic = svg_str_to_pixbuf(svg_from_file(
                os.path.join(path, 'smiley.svg')))

        self.frown_graphic = svg_str_to_pixbuf(svg_from_file(
                os.path.join(path, 'frown.svg')))

        self.egg_graphic = svg_str_to_pixbuf(svg_from_file(
                os.path.join(path, 'Easter_egg.svg')))

        self.blank_graphic = svg_str_to_pixbuf(
            _svg_header(BAR_HEIGHT, BAR_HEIGHT, 1.0) + \
            _svg_rect(BAR_HEIGHT, BAR_HEIGHT, 5, 5, 0, 0,
                      '#C0C0C0', '#282828') + \
            _svg_footer())

        self.ball = Sprite(self.sprites, 0, 0, svg_str_to_pixbuf(
                svg_from_file(os.path.join(path, 'basketball.svg'))))
        self.ball.set_layer(1)
        self.ball.set_label_attributes(24)

        ball = _extract_svg_payload(
            file(os.path.join(path, 'basketball.svg'), 'r'))
        self.cells = []  # Easter Egg animation
        for i in range(8):
            self.cells.append(Sprite(
                    self.sprites, 0, 0, svg_str_to_pixbuf(
                        _svg_header(85, 85, 1.0) + TRANSFORMS[i] + \
                            ball + PUNCTURE + AIR + '</g>' + _svg_footer())))

        for spr in self.cells:
            spr.set_layer(1)
            spr.move((0, self.height))  # move animation cells off screen
        self.frame = 0

        mark = _svg_header(self.ball.rect[2] / 2.,
                           BAR_HEIGHT * self.scale + 4, 1.0) + \
               _svg_rect(self.ball.rect[2] / 2.,
                         BAR_HEIGHT * self.scale + 4, 0, 0, 0, 0,
                         '#FF0000', '#FF0000') + \
               _svg_rect(1, BAR_HEIGHT * self.scale + 4, 0, 0,
                         self.ball.rect[2] / 4., 0, '#000000', '#000000') + \
               _svg_footer()
        self.mark = Sprite(self.sprites, 0,
                           self.height,  # hide off bottom of screen
                           svg_str_to_pixbuf(mark))
        self.mark.set_layer(2)

        self.bars = {}
        self.bars[2] = Sprite(self.sprites, 0, 0,
                              svg_str_to_pixbuf(self._gen_bar(2)))
        self.bars[2].move((int(self.ball.rect[2] / 2),
                           self.height - int((self.ball.rect[3] + \
                                                  self.bars[2].rect[3]) / 2)))
        self.current_bar = self.bars[2]

        num = _svg_header(BAR_HEIGHT * self.scale, BAR_HEIGHT * self.scale,
                           1.0) + \
              _svg_rect(BAR_HEIGHT * self.scale,
                        BAR_HEIGHT * self.scale, 0, 0, 0, 0,
                        'none', 'none') + \
              _svg_footer()
        self.left = Sprite(self.sprites, int(self.ball.rect[2] / 4),
                           self.bars[2].rect[1], svg_str_to_pixbuf(num))
        self.left.set_label('0')
        self.right = Sprite(self.sprites,
                            self.width - int(self.ball.rect[2] / 2),
                            self.bars[2].rect[1], svg_str_to_pixbuf(num))
        self.right.set_label('1')

        self.ball_y_max = self.bars[2].rect[1] - self.ball.rect[3]
        self.ball.move((int((self.width - self.ball.rect[2]) / 2),
                        self.ball_y_max))

    def _gen_bar(self, nsegments):
        ''' Return a bar with n segments '''
        svg = _svg_header(self.width - self.ball.rect[2], BAR_HEIGHT, 1.0)
        dx = (self.width - self.ball.rect[2]) / float(nsegments)
        for i in range(int(nsegments) / 2):
            svg += _svg_rect(dx, BAR_HEIGHT * self.scale, 0, 0,
                             i * 2 * dx, 0, '#FFFFFF', '#FFFFFF')
            svg += _svg_rect(dx, BAR_HEIGHT * self.scale, 0, 0,
                             (i * 2 + 1) * dx, 0, '#AAAAAA', '#AAAAAA')
        if int(nsegments) % 2 == 1:  # odd
            svg += _svg_rect(dx, BAR_HEIGHT * self.scale, 0, 0,
                             (i * 2 + 2) * dx, 0, '#FFFFFF', '#FFFFFF')
        svg += _svg_footer()
        return svg

    def pause(self):
        ''' Pause play when visibility changes '''
        if self.timeout is not None:
            gobject.source_remove(self.timeout)
            self.timeout = None

    def we_are_sharing(self):
        ''' If there is more than one buddy, we are sharing. '''
        if len(self.buddies) > 1:
            return True

    def its_my_turn(self):
        ''' When sharing, it is your turn... '''
        gobject.timeout_add(1000, self._take_a_turn)

    def _take_a_turn(self):
        ''' On your turn, choose a fraction. '''
        self.my_turn = True
        self.select_a_fraction = True
        self.activity.set_player_on_toolbar(self.activity.nick)
        self.activity.challenge.set_label(
            _("Click on the bar to choose a fraction."))

    def its_their_turn(self, nick):
        ''' When sharing, it is nick's turn... '''
        gobject.timeout_add(1000, self._wait_your_turn, nick)

    def _wait_your_turn(self, nick):
        ''' Wait for nick to choose a fraction. '''
        self.my_turn = False
        self.activity.set_player_on_toolbar(nick)
        self.activity.challenge.set_label(
            _('Waiting for %(buddy)s') % {'buddy': nick})

    def play_a_fraction(self, fraction):
        ''' Play this fraction '''
        fraction_is_new = True
        for i, c in enumerate(self.challenges):
            if c[0] == fraction:
                fraction_is_new = False
                self.n = i
                break
        if fraction_is_new:
            self.add_fraction(fraction)
            self.n = len(self.challenges)
        self._choose_a_fraction()
        self._move_ball()

    def _button_press_cb(self, win, event):
        ''' Callback to handle the button presses '''
        win.grab_focus()
        x, y = map(int, event.get_coords())
        self.press = self.sprites.find_sprite((x, y))
        return True

    def _button_release_cb(self, win, event):
        ''' Callback to handle the button releases '''
        win.grab_focus()
        x, y = map(int, event.get_coords())
        if self.press is not None:
            if self.we_are_sharing():
                if self.select_a_fraction and self.press == self.current_bar:
                    # Find the fraction closest to the click
                    fraction = self._search_challenges(
                        (x - self.current_bar.rect[0]) / \
                            float(self.current_bar.rect[2]))
                    self.select_a_fraction = False
                    self.activity.send_a_fraction(fraction)
                    self.play_a_fraction(fraction)
            else:
                if self.timeout is None and self.press == self.ball:
                    self._choose_a_fraction()
                    self._move_ball()
        return True

    def _search_challenges(self, f):
        ''' Find the fraction which is closest to f in the list. '''
        dist = 1.
        closest = '1/2'
        for c in self.challenges:
            numden = c[0].split('/')
            delta = abs((float(numden[0]) / float(numden[1])) - f)
            if delta <= dist:
                dist = delta
                closest = c[0]
        return closest

    def _move_ball(self):
        ''' Move the ball and test boundary conditions '''
        if self.new_bounce:
            self.mark.move((0, self.height))  # hide the mark
            if not self.we_are_sharing():
                self._choose_a_fraction()
            self.new_bounce = False
            self.dy = self.ddy * (1 - STEPS) / 2  # initial step size

        if self.accelerometer:
            fh = open(ACCELEROMETER_DEVICE)
            string = fh.read()
            xyz = string[1:-2].split(',')
            self.dx = float(xyz[0]) / 18.
            fh.close()

        if self.ball.get_xy()[0] + self.dx > 0 and \
           self.ball.get_xy()[0] + self.dx < self.width - self.ball.rect[2]:
            self.ball.move_relative((int(self.dx), int(self.dy)))
        else:
            self.ball.move_relative((0, int(self.dy)))

        # speed up ball in x while key is pressed
        self.dx *= DDX

        # accelerate in y
        self.dy += self.ddy

        if self.ball.get_xy()[1] >= self.ball_y_max:
            # hit the bottom
            self.ball.move((self.ball.get_xy()[0], self.ball_y_max))
            self._test()
            self.new_bounce = True

            if self.we_are_sharing():
                if self.my_turn:
                    # Let the next player know it is their turn.
                    i = (self.buddies.index(self.activity.nick) + 1) % \
                        len(self.buddies)
                    self.its_their_turn(self.buddies[i])
                    self.activity.send_event('t|%s' % (self.buddies[i]))
            else:
                if self._easter_egg_test():
                    self._animate()
                else:
                    self.timeout = gobject.timeout_add(
                        max(STEP_PAUSE,
                            BOUNCE_PAUSE - self.count * STEP_PAUSE),
                        self._move_ball)
        else:
            self.timeout = gobject.timeout_add(STEP_PAUSE, self._move_ball)

    def _animate(self):
        ''' A little Easter Egg just for fun. '''
        if self.new_bounce:
            self.dy = self.ddy * (1 - STEPS) / 2  # initial step size
            self.new_bounce = False
            self.frame = 0
            self.frame_counter = 0
            self.cells[self.frame].move(self.ball.get_xy())
            self.ball.move((self.ball.get_xy()[0], self.height))
            gobject.idle_add(play_audio_from_file, self, self.path_to_bubbles)

        if self.accelerometer:
            fh = open(ACCELEROMETER_DEVICE)
            string = fh.read()
            xyz = string[1:-2].split(',')
            self.dx = float(xyz[0]) / 18.
            fh.close()
        else:
            self.dx = uniform(-int(DX * self.scale), int(DX * self.scale))
        self.cells[self.frame].move_relative((int(self.dx), int(self.dy)))
        self.dy += self.ddy

        self.frame_counter += 1
        if self.frame_counter in ANIMATION:
            self._switch_cells(ANIMATION[self.frame_counter])

        if self.cells[self.frame].get_xy()[1] >= self.ball_y_max:
            # hit the bottom
            self.ball.move((self.ball.get_xy()[0], self.ball_y_max))
            for spr in self.cells:
                spr.move((0, self.height))  # hide the animation frames
            self._test(easter_egg=True)
            self.new_bounce = True
            self.timeout = gobject.timeout_add(BOUNCE_PAUSE, self._move_ball)
        else:
            gobject.timeout_add(STEP_PAUSE, self._animate)

    def _switch_cells(self, cells):
        ''' Switch between cells in the animation '''
        self.cells[cells[1]].move(self.cells[cells[0]].get_xy())
        self.cells[cells[0]].move((0, self.height))
        self.frame = cells[1]

    def add_fraction(self, string):
        ''' Add a new challenge; set bar to 2x demominator '''
        numden = string.split('/', 2)
        self.challenges.append([string, int(numden[1]), 0])

    def _choose_a_fraction(self):
        ''' Select a new fraction challenge from the table '''
        if not self.we_are_sharing():
            self.n = int(uniform(0, len(self.challenges)))
        fstr = self.challenges[self.n][0]
        saw_a_fraction = False
        if '/' in fstr:  # fraction
            numden = fstr.split('/', 2)
            self.fraction = float(numden[0].strip()) / float(numden[1].strip())
            saw_a_fraction = True
        elif '%' in fstr:  # percentage
            self.fraction = float(fstr.strip().strip('%').strip()) / 100.
        else:  # To do: add support for decimals (using locale)
            _logger.debug('Could not parse challenge (%s)', fstr)
            fstr = '1/2'
            self.fraction = 0.5
            saw_a_fraction = True

        if self.mode == 'fractions':
            if saw_a_fraction:
                self.label = fstr
            else:
                self.label = fstr.strip().strip('%').strip() + '/100'
        else:  # percentage
            if not saw_a_fraction:
                self.label = fstr
            else:
                self.label = str(int(self.fraction * 100 + 0.5)) + '%'
        self.activity.reset_label(self.label)
        self.ball.set_label(self.label)

        for bar in self.bars:
            self.bars[bar].set_layer(-1)
        if self.correct > EXPERT:  # Show two-segment bar in expert mode
            self.bars[2].set_layer(0)
            self.current_bar = self.bars[2]
        else:
            if self.mode == 'fractions':
                nseg = self.challenges[self.n][1]
            else:
                nseg = 10  # percentages
            # generate new bar on demand
            if not nseg in self.bars:
                self.bars[nseg] = Sprite(self.sprites, 0, 0,
                    svg_str_to_pixbuf(self._gen_bar(nseg)))
                self.bars[nseg].move((self.bars[2].rect[0],
                                      self.bars[2].rect[1]))
            self.bars[nseg].set_layer(0)
            self.current_bar = self.bars[nseg]

    def _easter_egg_test(self):
        ''' Test to see if we show the Easter Egg '''
        delta = self.ball.rect[2] / 8
        x = self.ball.get_xy()[0] + self.ball.rect[2] / 2
        f = self.bars[2].rect[2] * self.easter_egg / 100.
        if x > f - delta and x < f + delta:
            return True
        else:
            return False

    def _test(self, easter_egg=False):
        ''' Test to see if we estimated correctly '''
        self.timeout = None
        delta = self.ball.rect[2] / 4
        x = self.ball.get_xy()[0] + self.ball.rect[2] / 2
        f = self.ball.rect[2] / 2 + int(self.fraction * self.bars[2].rect[2])
        self.mark.move((int(f - self.mark.rect[2] / 2),
                        self.bars[2].rect[1] - 2))
        if self.challenges[self.n][2] == 0:  # label the column
            spr = Sprite(self.sprites, 0, 0, self.blank_graphic)
            spr.set_label(self.label)
            spr.move((int(self.n * 25), 0))
            spr.set_layer(-1)
        self.challenges[self.n][2] += 1
        if x > f - delta and x < f + delta:
            if not easter_egg:
                spr = Sprite(self.sprites, 0, 0, self.smiley_graphic)
            self.correct += 1
            gobject.idle_add(play_audio_from_file, self, self.path_to_success)
        else:
            if not easter_egg:
                spr = Sprite(self.sprites, 0, 0, self.frown_graphic)
            gobject.idle_add(play_audio_from_file, self, self.path_to_failure)

        if easter_egg:
            spr = Sprite(self.sprites, 0, 0, self.egg_graphic)

        spr.move((int(self.n * 25), int(self.challenges[self.n][2] * 25)))
        spr.set_layer(-1)

        # after enough correct answers, up the difficulty
        if self.correct == len(EASY) * 2:
            for challenge in MEDIUM:
                self.challenges.append(challenge)
        elif self.correct == len(EASY) * 4:
            for challenge in HARD:
                self.challenges.append(challenge)

        self.count += 1
        self.dx = 0.  # stop horizontal movement between bounces

    def _keypress_cb(self, area, event):
        ''' Keypress: moving the slides with the arrow keys '''
        k = gtk.gdk.keyval_name(event.keyval)
        if k in ['h', 'Left', 'KP_Left']:
            self.dx = -DX * self.scale
        elif k in ['l', 'Right', 'KP_Right']:
            self.dx = DX * self.scale
        elif k in ['KP_Page_Up', 'Return']:
            self._choose_a_fraction()
            self._move_ball()
        else:
            self.dx = 0.
        return True

    def _keyrelease_cb(self, area, event):
        ''' Keyrelease: stop horizontal movement '''
        self.dx = 0.
        return True

    def _expose_cb(self, win, event):
        ''' Callback to handle window expose events '''
        self.sprites.redraw_sprites(event.area)
        return True

    def _destroy_cb(self, win, event):
        ''' Callback to handle quit '''
        gtk.main_quit()