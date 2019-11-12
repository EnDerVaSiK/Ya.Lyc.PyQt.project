import sys
from random import randint, choice

from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog, QMessageBox, QColorDialog
from gameui import Ui_GameWindow
from man_setui import Ui_Manual_SettingsWindow

"""
Секунды !!!====!!! ВСЕГДА = 20 !!!====!!! потому что я не придумал как решить проблему с подсчетом кликов ¯\_(ツ)_/¯
и из-за этой проблемы не будет аккаунтов, очков, рекордов и баз данных с ними .(Т_Т). Минус 50+ строк...
"""
TIME_OUT = 20
# начальный размер 30, потом будет меняться
SIZE_OF_RUNNER = 30
# сложности, список для упрощения
LEVELS = [('easy', 3), ('normal', 2), ('hard', 1)]
# смайлы
SMLS = ['¯\\_(ツ)_/¯ ', '(* ^ ω ^)', '(o^▽^o)', 'ヽ(・∀・)ﾉ', '(o･ω･o)', '(^人^)', '( ´ ω )', '(((o(*°▽°*)o)))',
        '(´• ω •)', '(＾▽＾)', '╰(▔∀▔)╯', '(─‿‿─)', '(✯◡✯)', '(◕‿◕)', '(⌒‿⌒)', '＼(≧▽≦)／', '(*°▽°*)',
        '٩(｡•́‿•̀｡)۶', '(´｡• ᵕ •｡)', '( ´ ▽ )', 'ヽ(>∀<☆)ノ', 'o(≧▽≦)o', '＼(￣▽￣)／', '(*¯︶¯*)', '(o˘◡˘o)',
        '\\(★ω★)/', '(╯✧▽✧)╯', 'o(>ω<)o', '( ‾́ ◡ ‾́ )', '(ﾉ´ヮ)ﾉ*: ･ﾟ', '(๑˘︶˘๑)', '( ˙꒳​˙ )', '(´･ᴗ･ )',
        '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧', '(͡° ͜ʖ ͡°)', '(͡°╭͜ʖ╮͡°)', '( ͡⊙ ͜ʖ ͡⊙)﻿', '(V)(;,;)(V)', '(>^.^)>(^*o*)^', '▄︻̷̿┻̿═━一',
        '[✖‿✖]﻿', "ʕ•ᴥ•ʔ", '(ง ͠° ͟ل͜ ͡°)ง', '༼ つ ◕_◕ ༽つ', '(づ｡◕‿‿◕｡)づ', '(͡°╭͜ʖ╮͡°)', '[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]',
        '[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)', '(ಠ_ಠ)', '(ಥ﹏ಥ)', '(づ￣ ³￣)づ', '| (• ◡•)| (❍ᴥ❍ʋ)',
        '(ノಠ益ಠ)ノ彡┻━┻', '﴾͡๏̯͡๏﴿ O’RLY?', '٩(͡๏̯͡๏)۶', 'ಠ_ಠ', '(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)', '(╯°□°)╯︵ ʞooqǝɔɐɟ', '(╯°□°)╯︵ ɐǝʇ',
        '(͡ᵔ ͜ʖ ͡ᵔ)', '(☞ﾟヮﾟ)☞', 'ヾ(⌐■_■)ノ♪', 'ヽ༼ຈل͜ຈ༽ﾉ', '༼ つ ಥ_ಥ ༽つ', "(ง'̀-'́)ง", '(•_•) (•_•)>⌐■-■ (⌐■_■)',
        '(╯°□°）╯︵ ┻━┻', 'ᕦ(ò_óˇ)ᕤ', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧', '┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻', '(☞ﾟ∀ﾟ)☞', '(._.) (l:) (.-.) (:l) (._.)',
        '┬┴┬┴┤(･_├┬┴┬┴', '┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴', 'ᕙ(⇀‸↼‶)ᕗ', '(~˘▾˘)~ (◕‿◕)', '(｡◕‿‿◕｡)', '(｡◕‿◕｡)', '~(˘▾˘~)', '⌐╦╦═─',
        '(☞ຈل͜ຈ)☞', '(ง°ل͜°)ง', '┌(ಠ_ಠ)┘', '◉_◉', '(╯°□°）╯︵(.o.)', '┬──┬ ノ(゜-゜ノ)', '☜(˚▽˚)☞', '(─‿‿─)',
        'ლ(´ڡ`ლ)', '(ಥ_ಥ)', 'ᄽὁȍ ̪ őὀᄿ', '\\ (•◡•) /', '(° ͡ ͜ ͡ʖ ͡ °)', '☜(⌒▽⌒)☞', '+1 ☜(⌒▽⌒)☞ +1', '｡◕‿‿◕｡',
        '╚(ಠ_ಠ)=┐', '(ಠ‿ಠ)', "(ʘᗩʘ')", '(✿´‿`)', 'ಥ_ಥ', '(ღ˘⌣˘ღ)', '(；一_一)', '¯\\(°_o)/¯', '(¬‿¬)', '͠° ͟ل͜ ͡°',
        '(>ლ)', '(｡◕‿◕｡)', '┬─┬ノ(º _ ºノ)', '•_•)', '(•_•)>⌐■-■', '(⌐■_■)', 'o ()xxxx[{:>', 'O===|_________________/',
        '¦̵̱ ̵̱ ̵̱ ̵̱ ̵̱(̢ ̡͇̅└͇̅┘͇̅ (▤8כ−◦', '༼ つ ಥ_ಥ ༽つ', '| (• ◡•)|', '(❍ᴥ❍ʋ)', 't (-.-)t', '(☞ﾟヮﾟ)☞', '(;´༎ຶД༎ຶ`)',
        '<:[]=¤༼ຈل͜ຈ༽ﾉ', '(͡° ͜ʖ ͡°) ▄︻̷̿┻̿═━一 ʕ•ᴥ•ʔ', 'ლ(ಠ益ಠლ)', '(⌐■_■)>¸,ø¤º°`°º¤ø,¸¸', '(x_x)@~(-_-Q)',
        '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*: ･ﾟ✧', '(͡° ͜ʖ ͡°) ▄︻̷̿┻̿═━一', "(ʘᗩʘ')", 'ζ༼Ɵ͆ل͜Ɵ͆༽ᶘ', 'ლ(ಠ‿ಠლ)']
# переменная своих настроек
col = ''


# класс своих настроек
class Man_Set(QWidget, Ui_Manual_SettingsWindow):
    def __init__(self):
        # global col
        super().__init__()
        # super().__init_()
        super().setupUi(self)
        self.initUi()

    def initUi(self):
        # случайно менять цвет кнопки
        self.rm_col.clicked.connect(self.rm_color)
        # сделать цвет кнопки красным
        self.red_col.clicked.connect(self.red_color)
        # сделать цвет кнопки зеленым
        self.green_col.clicked.connect(self.green_color)
        # сделать цвет кнопки синим
        self.blue_col.clicked.connect(self.blue_color)
        # самому выбрать цвет
        self.manual_col.clicked.connect(self.manual_color)
        self.acceptbtn.clicked.connect(self.closeee)

    def closeee(self):
        self.close()

    def rm_color(self):
        global col
        col = 'rm_col'

    def red_color(self):
        global col
        col = 'red_col'

    def green_color(self):
        global col
        col = 'green_col'

    def blue_color(self):
        global col
        col = 'blue_col'

    def manual_color(self):
        global col
        col = 'manual_col'

    # метод вызывающий окно с подтверждением выхода
    def closeEvent(self, event):
        res = QMessageBox.question(self, "Confirm exit",
                                   "Are you sure you want to exit?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if res == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# класс главного окна
class Game(QMainWindow, Ui_GameWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.setFixedSize(500, 400)
        # внетренняя переменная сколько сек живет кнопка
        self.t = TIME_OUT
        self.timer = QTimer()
        self.time = QTime(0, 0, self.t)
        # кнопка-бегунок
        self.runner.hide()
        # переменная сложности для размера кнопки-бегунка
        self.d = SIZE_OF_RUNNER * LEVELS[0][1]
        self.runner.resize(self.d, self.d)
        # таймер в окне
        self.label.setText('00:20')
        # сообзщение перед запуском
        # message = QInputDialog.getItem(self, 'Сообщение', 'Обязательно посмотрите раздел О программе', 'OK', 0, False)
        self.initUi()
        # свои настройки
        self.man_set = Man_Set()
        self.is_dark = False

    def initUi(self):
        # просто случайный смайл в статусбаре ¯\(⌒‿⌒)/¯
        self.statusBar().showMessage(choice(SMLS))
        # кнопка старта
        self.beginbtn.clicked.connect(self.run)
        # меню сложности
        self.Menu_Difficulty.triggered.connect(self.Difficulty)
        # меню своих настроек
        self.Manual_Settings.triggered.connect(self.Man_Set)
        # меню справки
        self.About_program.triggered.connect(self.About)
        # темная тема
        self.dark.clicked.connect(self.dark_phone)

    # TODO: -----
    def dark_phone(self):
        if not self.is_dark:
            self.is_dark = True
            self.setStyleSheet('background-color: black')
            self.beginbtn.setStyleSheet('background-color: gray')
            self.label.setStyleSheet('background-color: gray')
            self.dark.setStyleSheet('background-color: gray')
        else:
            self.is_dark = False
            self.beginbtn.setStyleSheet('background-color: white')
            self.label.setStyleSheet('background-color: white')
            self.dark.setStyleSheet('background-color: white')
            self.setStyleSheet('background-color: white')
        if not col:
            self.runner.setStyleSheet('background-color: grey')

    # злополучный таймер, там же применение своих настроек
    def run(self):
        print('run timer')
        # свои настройки
        self.run_color()
        self.timer = QTimer()
        self.time = QTime(0, 0, self.t)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timerEvent)

    # события связанные с таймером
    def timerEvent(self):
        print(self.t)
        # меняет время в окне в QLabel
        self.label.setText(self.time.toString("mm:ss"))
        # таймер до 0
        if self.time != QTime(0, 0, 0):
            print('!')
            self.runner.show()
            self.beginbtn.hide()
            self.runner.clicked.connect(self.change_pos)
            self.time = self.time.addSecs(-1)
        else:
            print('else')
            self.runner.hide()
            self.beginbtn.show()
            self.label.setText('00:20')
            self.timer.stop()

    # проблемный метод изменения позиции "бегуна", меняет столько раз, сколько прошло секунд... (не знаю как исправить)
    def change_pos(self):
        # случайный цвет
        if col == 'rm_col':
            self.runner.setStyleSheet("background-color: rgb({}, {}, {})".format(randint(0, 255), randint(0, 255),
                                                                                 randint(0, 255)))
            # красный цвет
        elif col == 'red_col':
            self.runner.setStyleSheet("background-color: red")
        # зеленый цвет
        elif col == 'green_col':
            self.runner.setStyleSheet("background-color: green")
        # синий цвет
        elif col == 'blue_col':
            self.runner.setStyleSheet("background-color: blue")
        self.runner.move(randint(100, self.width() - 200), randint(100, self.height() - 200))
        self.runner.repaint()

    # метод вызывающий окно выбора сложности
    def Difficulty(self):
        diff, okBtnPressed = QInputDialog.getItem(self, "Difficulty",
                                                  'Выберите сложность, с которой хотите играть.',
                                                  ('easy', 'normal', 'hard'),
                                                  0, False)

        # постановка сложности
        if okBtnPressed:
            if diff == 'easy':
                self.d = SIZE_OF_RUNNER * LEVELS[0][1]
            elif diff == 'normal':
                self.d = SIZE_OF_RUNNER * LEVELS[1][1]
            elif diff == 'hard':
                self.d = SIZE_OF_RUNNER * LEVELS[2][1]
        self.runner.resize(self.d, self.d)

    # метод окна своих настроек
    def Man_Set(self):
        print('Man_Set')
        self.man_set.setFixedSize(400, 300)
        self.man_set.show()

    # осуществление своих настроек
    def run_color(self):
        # случайный цвет
        if col == 'rm_col':
            self.runner.setStyleSheet("background-color: rgb({}, {}, {})".format(randint(0, 255), randint(0, 255),
                                                                                 randint(0, 255)))
        # красный цвет
        elif col == 'red_col':
            self.runner.setStyleSheet("background-color: red")
        # зеленый цвет
        elif col == 'green_col':
            self.runner.setStyleSheet("background-color: green")
        # синий цвет
        elif col == 'blue_col':
            self.runner.setStyleSheet("background-color: blue")
        # выбрать цвет самостоятельно
        elif col == 'manual_col':
            color = QColorDialog.getColor()
            if color.isValid():
                self.runner.setStyleSheet("background-color: {}".format(
                    color.name()))

    # метод окна справки
    def About(self):
        QInputDialog.getItem(self, 'About', 'Эта программа создана для проверки и улучшения реакции.\nЕсть несколько '
                                            'режимов сложности, они влияют на размер\nкнопки.\nЕще можно менять цвет в своих '
                                            'настройках, обязательно\nзагляните туда!\nЖелаю хорошо провести время!\n'
                                            '---------------------------------------------------------------------------------------\n'
                                            'И кстати, пожалуйста, перезапускайте программу хотябы через каждые 5 стартов.\n'
                                            '---------------------------------------------------------------------------------------\n',
                             ('ок', 'хорошо', 'нормально', 'спасибо))0)00))0)))'), 3, False)

    # Метод кнопочек
    def keyPressEvent(self, event):
        # Esc >> exit
        if event.key() == Qt.Key_Escape:
            self.close()

    # Метод вызывающий окно с подтверждением выхода
    def closeEvent(self, event):
        res = QMessageBox.question(self, "Confirm exit",
                                   "Are you sure you want to exit?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if res == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# PyQt traceback
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


# функция, запускающая прогу
def main():
    app = QApplication(sys.argv)
    app.setApplicationDisplayName('Reaction')
    ex = Game()
    ex.show()
    sys.exit(app.exec())


# САМЫЙ ВАЖНЫЙ КОПМПОНЕНТ! оставьте пж )
if __name__ == '__main__':
    main()
