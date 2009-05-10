"""
Presumed I/O hardware, first cut:

Input and output are line at a time, using punch cards or a print head
or typesetter or similar. There's an instruction to advance to the
next line, for either one. Each has a read or write head that can be
moved left or right one step at a time, plus read/write at the
position of the head. The charset includes the decimal digits, space,
and at least a few more symbols (dot, comma, dash, ... and the
alphabet would be nice too).

First programs to write:

* Binary/decimal conversions
"""


# Model the I/O operations:

line_width = 20

input_line = [' '] * line_width
input_pos = 0

output_line = [' '] * line_width
output_pos = 0

def input_next():
    line = raw_input()
    line = (line + ' '*line_width)[:line_width]
    input_line[:] = list(line)

def input_move(dir):
    global input_pos
    input_pos = move(input_pos, dir)

def input_read():
    return input_line[input_pos]

def output_next():
    print ''.join(output_line)
    output_line[:] = [' '] * line_width

def output_move(dir):
    global output_pos
    output_pos = move(output_pos, dir)

def output_write(ch):
    output_line[output_pos] = ch

def move(pos, dir):
    return max(0, min(line_width-1, pos + (-1 if dir < 0 else +1)))


# Output to decimal
# [super-crude start]

def write_decimal(u, width):
    """Put the decimal representation of the unsigned integer u into
    the output line from the current position leftwards in a 0-padded
    field of the given width."""
    for i in range(width):
        ones = u % 10
        output_write(chr(ord('0') + ones))
        output_move(-1)
        u //= 10

def test_write_decimal():
    for i in range(line_width):
        output_move(+1)
    write_decimal(31416, 6)
    output_next()

test_write_decimal()


# Input from decimal

def read_decimal(width):
    """Return the value of an unsigned decimal integer field, 0-padded
    starting from the current position rightwards for the given
    width."""
    u = 0
    for i in range(width):
        ones = ord(input_read()) - ord('0')
        input_move(+1)
        assert 0 <= ones <= 9
        u = u * 10 + ones
    return u

def test_read_decimal():
    line = '031416'
    line = (line + ' '*line_width)[:line_width]
    input_line[:] = list(line)
    print read_decimal(6)

test_read_decimal()
