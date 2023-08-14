Title: Qt QShortcut Ambiguity
Date: 2023-08-14 12:38
Category: Qt
Tags: Qt, PySide6, Python, My StackOverflow Answer

I hope this answer still has value for anyone who comes across this shortcut context problem, and can save you couple hours of struggling with Qt QShortcut.

Long story in short: Qt think shortcuts with same key sequence(e.g. CTRL+F) defined on both parent and child widgets is the case of `ambiguity`, and signals `activatedAmbiguously()` will be emitted in one by one in bubble order(the order of top to bottom, first `QMainWindow` then `QTextEdit` then `QMainWindow`... to infinite loop).

> From Qt offical document: When the user types the key sequence for a given shortcut, the shortcut’s activated() signal is emitted. (In the case of ambiguity, the activatedAmbiguously() signal is emitted.) A shortcut is “listened for” by Qt’s event loop when the shortcut’s parent widget is receiving events.

As a result, if you have `QShortcut` objects with same `QKeySeqence` `CTRL+F` on `QMainWindow` and `QTextEdit`(center widget of `QMainWindow`), no matter you focus(mouse click in) on `QTextEdit` or `QMainWindow`. When you press `CTRL+F`. None of shortcut will emit signal `activated`, but signal `activatedAmbiguously` will be emitted in the order of `['QMainWindow.QShortcut.activatedAmbiguously', 'QTextEdit.QShortcut.activatedAmbiguously', 'QMainWindow.QShortcut.activatedAmbiguously' ...]`.

This behavior is checked by me after several exhausting hours of testing QShortcut in different senario again and again. You can refer to the unittest(requires pytest, pytest-qt and PySide6) code I post below:

``` python
from unittest.mock import MagicMock
import pytest

def test_shortcut_override(qtbot):
    """
    In this test we have built a simple UI has an QTextEdit in an QMainWindow,
    Both QTextEdit and QMainWindow has same shortcut 'Ctrl+F'. The shortcuts
    emit `activatedAmbiguously()` signal in bubble order.
    """
    from PySide6 import QtWidgets, QtCore, QtGui
    import random

    mainWindow = QtWidgets.QMainWindow()
    qtbot.add_widget(mainWindow)

    # build UI hierarchy
    textEdit = QtWidgets.QTextEdit()
    mainWindow.setCentralWidget(textEdit)

    # window must be shown, otherwise the shortcut will never work since it
    # needs window to receive the shortcut event
    mainWindow.show()

    mainWindowSCAmbigouslyTrigger = MagicMock(returns=None)
    textEditSCAmbigouslyTrigger = MagicMock(returns=None)

    mainWindowMockSC = MagicMock(returns=None)
    textEditMockSC = MagicMock(returns=None)

    sc = QtGui.QShortcut('Ctrl+F', mainWindow, mainWindowMockSC, QtGui.Qt.ShortcutContext.WindowShortcut)
    sc.activatedAmbiguously.connect(mainWindowSCAmbigouslyTrigger)

    sc = QtGui.QShortcut('Ctrl+F', textEdit, textEditMockSC, QtGui.Qt.ShortcutContext.WindowShortcut)
    sc.activatedAmbiguously.connect(textEditSCAmbigouslyTrigger)

    mainWindowSCAmbiguouslyCount = 0
    textEditSCAmbiguouslyCount = 0

    for i in range(20):
        # no matter which widget is focus, it doesn't change the bubble order.
        widget = random.choice([textEdit, mainWindow])
        widget.setFocus()
        qtbot.keyClicks(widget, 'F', QtCore.Qt.KeyboardModifier.ControlModifier, delay=1)

        # Result 1) neither shortcut's signal `activated` not emitted, so these two not called.
        mainWindowMockSC.assert_not_called()
        textEditMockSC.assert_not_called()

        # Result 2) shortcuts are ambiguously activated in bubble order.
        if i % 2 == 0:
            mainWindowSCAmbiguouslyCount += 1
        else:
            textEditSCAmbiguouslyCount += 1

        assert mainWindowSCAmbigouslyTrigger.call_count == mainWindowSCAmbiguouslyCount
        assert textEditSCAmbigouslyTrigger.call_count == textEditSCAmbiguouslyCount

        print(f"'CTRL+F' has been triggered: {i + 1} times.")
        print(f"QMainWindow's shortcut ambiguously triggered: {mainWindowSCAmbigouslyTrigger.call_count} times.")
        print(f"QTextEdit's shortcut ambiguously triggered: {textEditSCAmbigouslyTrigger.call_count} times.")
```

I'm sure this "ambiguous" shortcut behavior is same in Qt/C++.

> "Is there a way for a focussed widget to steal and consume a shortcut, no matter if there is another shortcut with context WindowShortcut or ApplicationShortcut?"

Saddly, the answer is NO, but since you know that shortcuts with same key sequence will emit `activatedAmbiguously` signal in bubble order. You can exploit this behavior by binding all `activatedAmbiguously` signal to one SLOT function, and in that function you can use `QApplication::focusWidget()` to get focused widget then trigger the shortcut action by yourself now.

I won't post the implementation here because since you've read this far, you should fully understand `QShortcut` ambiguity and how signals are emitted in bubble order now, go and try it yourself :)



