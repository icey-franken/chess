# W17 Lecture Notes (Python)

_________________________________________________________________________________________
_________________________________________________________________________________________

## W17D1 (Intro to Python 3) (actually W16D5)

_________________________________________________________________________________________

### Gordon - Intro to Python (OBS#1 start - 0:30)

* block comments with """block comment here""" - we should be putting these at the top of every file letting folks know what's going on

## W17D3 (Python 3)

Gordon on how to do logging in Python 3:

```python
################################################################################
# configure logging - here we just log to the console
################################################################################
import logging
logger = logging.Logger(__file__)
# set the level for this logger
logger.setLevel(logging.DEBUG)
# set the level for the (console) logging handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
# define a format string for logging output
formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
# attach the formatter to the handler
handler.setFormatter(formatter)
# and the handler to the logger
logger.addHandler(handler)
################################################################################
```

Gordon says: "invoke this as logger.debug(_whatever_) or logger.info... similarly warning and error"

_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________

## [[TEMPLATE BELOW]]

_________________________________________________________________________________________
_________________________________________________________________________________________

## [WXDX] ([topic])

_________________________________________________________________________________________

### Notes on [lecture vid title]

_________________________________________________________________________________________

### [Lecturer] - [topic] (OBS#X x:xx - x:xx)
