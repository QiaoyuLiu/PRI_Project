
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget,QTextEdit, QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, \
    QVBoxLayout, QDesktopWidget, QFormLayout, QLabel, QLineEdit, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from MainCodefinal import ScorceCode


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'The blue ocean'
        self.left = 200
        self.top = 200
        self.width = 700
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('six_sigma.ico'))

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.show()


class MyTableWidget(QWidget):



    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)



        # The dataframe
        self.df = pd.DataFrame()
        self.gs = []
        # Initialize the labels for the first tab

        self.productLabel = QLabel("Product", self)
        self.countryLabel = QLabel("Country", self)
        #self.stateLabel = QLabel("State", self)
        #self.cityLabel = QLabel("City", self)

        # Initialise the textbox for all the labels along with the tooltips

        self.productTextBox = QLineEdit(self)

        self.productTextBox.setToolTip("Enter the product here")
        self.countryTextBox = QLineEdit(self)
        self.countryTextBox.setToolTip("Enter the country here")



        # Canvas and Toolbar
        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        self.submitButton = QPushButton("Submit")
        self.submitButton.setToolTip("To submit and get results")
        self.submitButton.resize(self.submitButton.sizeHint())
        self.submitButton.clicked.connect(self.on_click)
        self.show()
        #print(self.on_click)

        # Buttons to be added to the first tab
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.resize(self.clearAllButton.sizeHint())
        self.clearAllButton.setToolTip("To clear all the fields")
        self.clearAllButton.clicked.connect(self.clear_on_click)



        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(480, 320)

        # Add tabs
        self.tabs.addTab(self.tab1, "The Input Tab")
        self.tabs.addTab(self.tab2, "The result")
        #self.tabs.addTab(self.tab3, "The Data")
        self.tabs.addTab(self.tab4, "The Recommendation")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)

        self.tab1.layout.addWidget(self.productLabel)
        self.tab1.layout.addWidget(self.productTextBox)
        self.tab1.layout.addWidget(self.countryLabel)
        self.tab1.layout.addWidget(self.countryTextBox)
        self.tab1.layout.addWidget(self.submitButton)
        self.tab1.layout.addWidget(self.clearAllButton)



        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # Canvas and Toolbar
        # a figure instance to plot on
        self.figure = Figure()
        self.figureComp = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.canvasComp = FigureCanvas(self.figureComp)
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Create the second tab
        tab2layout = QVBoxLayout()
        tab2layout.addWidget(self.toolbar)
        tab2layout.addWidget(self.canvas)
        tab2layout.addWidget(self.canvasComp)


        self.tab2.setLayout(tab2layout)

        # Tab 4 The Recommendation

        self.tab4Form = QFormLayout()
        self.tablewidget = QTableWidget()
        self.tablewidget2 = QTableWidget()
        self.tablewidget.setMinimumSize(300,70)
        self.tablewidget2.setMinimumSize(300,70)
        self.tablewidget.horizontalHeader().setStretchLastSection(True)
        self.tablewidget2.horizontalHeader().setStretchLastSection(True)
        self.recommendationText = QLabel()
        #self.recommendationText.setMinimumSize(480, 320)
        self.recommendationText.setToolTip("This tab shows the recommendation ")
        self.relQuerry = QLabel('Related Querry')
        self.relTop = QLabel('Related Top')
        self.tab4Form.addRow(self.relQuerry,self.tablewidget)
        self.tab4Form.addRow(self.relTop,self.tablewidget2)
        self.tab4.setLayout(self.tab4Form)
        self.tab4Form.addRow(self.recommendationText)

        #self.countryTextBox.addItems(ScorceCode.countryName(self))
        str = "test"
        self.recommendationText.setText(str)

        # call the function to get the recommendation and then load it into the textbox

        #Provide labels and data as lists and the number of subplot to draw the bar chart
    def barPainting(self,labels,data,n_subplot):
        width = 0.5
        self.axes = self.figureComp.add_subplot(n_subplot)
        self.axes.clear()
        self.axes.barh(labels,data,width,align="center")
        #self.axes.set_xticks([0,1,2,3])
        self.axes.set_yticklabels(labels, rotation=40)
        self.axes.tick_params(axis='y', labelsize=5)



    def createTable(self,tableWidget):
        # Create table
        # find the table length
        self.lsTest = self.gs
        rows = len(self.lsTest)
        columns = 1
        # set the rows and columns of the table
        tableWidget.setRowCount(rows)
        tableWidget.setColumnCount(columns)
        i = 0
        for value in self.lsTest:
            if i < int(rows):
                tableWidget.setItem(i, 0, QTableWidgetItem(value))
                i = i + 1
    def export_csv_connect(self):
        print('Export data to CSV operation: ')

        self.gs.to_csv('C:/Users/lakshay/Desktop/udemy/PRI_Exported_CSV_files/finlistWorld.csv')

        self.gs1.to_csv('C:/Users/lakshay/Desktop/udemy/PRI_Exported_CSV_files/finlistState.csv')

        self.gs2.to_csv('C:/Users/lakshay/Desktop/udemy/PRI_Exported_CSV_files/finlistCity.csv')

        QMessageBox.about(self, "Export to CSV", "Files Exported Successfully")

    def on_click(self):
        print("\n")
        print(self.productTextBox.text())
        self.productName=self.productTextBox.text()
        self.countryName = self.countryTextBox.text()

        ls, rel_quer, rel_top = ScorceCode.forCountry(self.countryName,self.productName)
        digital, analog = ScorceCode.forCountryMarketing(self.countryName)  #unpacking these two variable dataframes with the reslts
        labeld = ['Email Marketing','Radio Advertising','Mobile Marketing','Television Advertising','Social Media Usage']
        labela = ['Newspaper Marketing','Billboards','Bus Shelter Ads','Print Ads','Fliers']
        E = digital['Email marketing'].mean()  # Print average popularity for marketing on this country
        R = digital['Radio Advertising'].mean()
        M = digital['Mobile Marketing'].mean()
        T = digital['Television Advertising'].mean()
        S = digital['Social Media Usage'].mean()
        datad = [E, R, M, T, S]
        N = analog['Newspaper Marketing'].mean() # Print average popularity for marketing on this country
        B = analog['Billboards'].mean()
        BUS = analog['Bus Shelter Ads'].mean()
        ADS = analog['Print Ads'].mean()
        Fil = analog['Fliers'].mean()
        dataa = [N, B, BUS, ADS, Fil]
        self.barPainting(labela,dataa,121)
        self.barPainting(labeld,datad,122)
        self.gs = rel_quer
        self.createTable(self.tablewidget)
        self.gs = rel_top
        self.createTable(self.tablewidget2)
        self.plot(ls)




    def clear_on_click(self):
        self.productTextBox.clear()
        print('all clear')

    def plot(self,data):

        # hit only if we have values on all the four components
        #if (self.productTextBox.text()):

            print("Inside the plot method")
            # Call the api #TODO
            print('plotBreak')
            # create an axis
            ax = self.figure.add_subplot(111)

            # discards the old graph
            ax.clear()

            # plot data

            for tick in ax.get_xticklabels():
                tick.set_rotation(20)
            ax.plot(data, '*-')

            # refresh canvas
            self.canvas.draw()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

