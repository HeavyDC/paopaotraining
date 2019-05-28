keyboard
========

Take full control of your keyboard with this small Python library. Hook
global events, register hotkeys, simulate key presses and much more.

Features
--------

-  **Global event hook** on all keyboards (captures keys regardless of
   focus).
-  **Listen** and **send** keyboard events.
-  Works with **Windows** and **Linux** (requires sudo), with
   experimental **OS X** support (thanks @glitchassassin!).
-  **Pure Python**, no C modules to be compiled.
-  **Zero dependencies**. Trivial to install and deploy, just copy the
   files.
-  **Python 2 and 3**.
-  Complex hotkey support (e.g. ``ctrl+shift+m, ctrl+space``) with
   controllable timeout.
-  Includes **high level API** (e.g. `record <#keyboard.record>`__ and
   `play <#keyboard.play>`__,
   `add\_abbreviation <#keyboard.add_abbreviation>`__).
-  Maps keys as they actually are in your layout, with **full
   internationalization support** (e.g. ``Ctrl+ç``).
-  Events automatically captured in separate thread, doesn't block main
   program.
-  Tested and documented.
-  Doesn't break accented dead keys (I'm looking at you, pyHook).
-  Mouse support available via project
   `mouse <https://github.com/boppreh/mouse>`__ (``pip install mouse``).

Usage
-----

Install the `PyPI package <https://pypi.python.org/pypi/keyboard/>`__:

::

    pip install keyboard

or clone the repository (no installation required, source files are
sufficient):

::

    git clone https://github.com/boppreh/keyboard

or `download and extract the
zip <https://github.com/boppreh/keyboard/archive/master.zip>`__ into
your project folder.

Then check the `API docs
below <https://github.com/boppreh/keyboard#api>`__ to see what features
are available.

Example
-------

.. code:: py

    import keyboard

    keyboard.press_and_release('shift+s, space')

    keyboard.write('The quick brown fox jumps over the lazy dog.')

    keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

    # Press PAGE UP then PAGE DOWN to type "foobar".
    keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

    # Blocks until you press esc.
    keyboard.wait('esc')

    # Record events until 'esc' is pressed.
    recorded = keyboard.record(until='esc')
    # Then replay back at three times the speed.
    keyboard.play(recorded, speed_factor=3)

    # Type @@ then press space to replace with abbreviation.
    keyboard.add_abbreviation('@@', 'my.long.email@example.com')

    # Block forever, like `while True`.
    keyboard.wait()

Known limitations:
------------------

-  Events generated under Windows don't report device id
   (``event.device == None``).
   `#21 <https://github.com/boppreh/keyboard/issues/21>`__
-  Media keys on Linux may appear nameless (scan-code only) or not at
   all. `#20 <https://github.com/boppreh/keyboard/issues/20>`__
-  Key suppression/blocking only available on Windows.
   `#22 <https://github.com/boppreh/keyboard/issues/22>`__
-  To avoid depending on X, the Linux parts reads raw device files
   (``/dev/input/input*``) but this requries root.
-  Other applications, such as some games, may register hooks that
   swallow all key events. In this case ``keyboard`` will be unable to
   report events.
-  This program makes no attempt to hide itself, so don't use it for
   keyloggers or online gaming bots. Be responsible.


