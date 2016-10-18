/*
 * The Python Imaging Library.
 * $Id$
 *
 * decoder for raw (uncompressed) image data
 *
 * Copyright (c) Fredrik Lundh 1996.
 * Copyright (c) Secret Labs AB 1997.
 *
 * See the README file for information on usage and redistribution.
 */


#include "Imaging.h"

#include "Raw.h"


int
ImagingRawDecode(Imaging im, ImagingCodecState state, UINT8* buf, int bytes)
{
    enum { LINE = 1, SKIP };
    RAWSTATE* rawstate = state->context;

    UINT8* ptr;

    if (state->state == 0) {

	/* Initialize context variables */

	/* get size of image data and padding */
	state->bytes = (state->xsize * state->bits + 7) / 8;
	rawstate->skip = (rawstate->stride) ?
	    rawstate->stride - state->bytes : 0;

	/* check image orientation */
	if (state->ystep < 0) {
	    state->y = state->ysize-1;
	    state->ystep = -1;
	} else
	    state->ystep = 1;

	state->state = LINE;

    }

    ptr = buf;

    for (;;) {

	if (state->state == SKIP) {

	    /* Skip padding between lines */

	    if (bytes < rawstate->skip)
		return ptr - buf;

	    ptr += rawstate->skip;
	    bytes -= rawstate->skip;

	    state->state = LINE;

	}

	if (bytes < state->bytes)
	    return ptr - buf;

	/* Unpack data */
	state->shuffle((UINT8*) im->image[state->y + state->yoff] +
		       state->xoff * im->pixelsize, ptr, state->xsize);

	ptr += state->bytes;
	bytes -= state->bytes;

	state->y += state->ystep;

	if (state->y < 0 || state->y >= state->ysize) {
	    /* End of file (errcode = 0) */
	    return -1;
	}

	state->state = SKIP;

    }

}
