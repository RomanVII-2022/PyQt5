import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Change window title 
        self.setWindowTitle('First Window')
        
        #Set Layout
        self.setLayout(qtw.QVBoxLayout())

        # Create Label
        my_label = qtw.QLabel('Hello World')
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)

        # Create Line Edit
        my_text = qtw.QLineEdit()
        my_text.setObjectName('name_text')
        self.layout().addWidget(my_text)

        #Create Button
        my_button = qtw.QPushButton('Press Me!', clicked = lambda: press_it())
        self.layout().addWidget(my_button)



        self.show()

        def press_it():
            my_label.setText(f'Hello {my_text.text()}, welcome.')
            my_text.setText('')

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()