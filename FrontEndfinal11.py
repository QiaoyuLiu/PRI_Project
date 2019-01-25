
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
        self.title = 'The Six Sigma Samurais'
        self.left = 200
        self.top = 200
        self.width = 480
        self.height = 700
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
        self.gs = pd.DataFrame()
        self.gs1 = pd.DataFrame()
        self.gs2 = pd.DataFrame()


        # Initialize the labels for the first tab

        self.productLabel = QLabel("Product", self)
        self.countryLabel = QLabel("Country", self)
        #self.stateLabel = QLabel("State", self)
        #self.cityLabel = QLabel("City", self)

        # Initialise the textbox for all the labels along with the tooltips

        self.productTextBox = QLineEdit(self)

        self.productTextBox.setToolTip("Enter the product here")
        self.countryTextBox = QComboBox(self)
        self.countryTextBox.setToolTip("Enter the country here")










        #self.stateTextBox = QComboBox(self)
        #self.stateTextBox.setToolTip("Enter the state here")




        #self.cityTextBox = QComboBox(self)
        #self.cityTextBox.setToolTip("Enter the city here")


        # Canvas and Toolbar
        # a figure instance to plot on
        self.figure = Figure()
        self.figure3 = Figure()
        self.figure4 = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.canvas3 = FigureCanvas(self.figure3)
        self.canvas4 = FigureCanvas(self.figure4)

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
        self.tabs.addTab(self.tab3, "The Data")
        self.tabs.addTab(self.tab4, "The Recommendation")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)

        self.tab1.layout.addWidget(self.productLabel)
        self.tab1.layout.addWidget(self.productTextBox)
        self.tab1.layout.addWidget(self.countryLabel)
        self.tab1.layout.addWidget(self.countryTextBox)
        self.tab1.layout.addWidget(self.submitButton)
        self.tab1.layout.addWidget(self.clearAllButton)
        #self.tab1.layout.addWidget(self.stateLabel)
        #self.tab1.layout.addWidget(self.stateTextBox)
        #self.tab1.layout.addWidget(self.cityLabel)
        #self.tab1.layout.addWidget(self.cityTextBox)



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
        self.canvasComp = FigureCanvas(self.figureComp )

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Create the second tab
        tab2layout = QVBoxLayout()
        tab2layout.addWidget(self.toolbar)
        tab2layout.addWidget(self.canvas)
        tab2layout.addWidget(self.canvasComp)


        self.tab2.setLayout(tab2layout)

        # Tab 3 The Data

        self.tab3Table = QFormLayout()

        self.tableWidget = QTableWidget()
        self.tab3Table.addWidget(self.tableWidget)

        self.tab3.setLayout(self.tab3Table)

        self.tab3Table.addRow(self.tableWidget)



        # Buttons to be added to the first tab
        self.exportCSVButton = QPushButton("Export Data to CSV")
        self.exportCSVButton.resize(self.clearAllButton.sizeHint())
        self.exportCSVButton.setToolTip("To export the above data to a CSV")
        self.exportCSVButton.clicked.connect(self.export_csv_connect)

        self.tab3Table.addRow(self.exportCSVButton)
        self.tab3.setLayout(self.tab3Table)

        #self.tab3.layout.addWidget(self.exportCSVButton)

        # Tab 4 The Recommendation

        self.tab4Form = QFormLayout()
        self.recommendationText = QTextEdit()
        self.recommendationText.setMinimumSize(480, 320)
        self.recommendationText.setToolTip("This tab shows the recommendation ")
        self.tab4Form.addRow(self.recommendationText)

        self.tab4.setLayout(self.tab4Form)

        self.countryTextBox.addItems(ScorceCode.countryName(self))
        '''
        x = ['a', 'b', 'c', 'd']
        y = [23,21,32,13]
        self.barPainting(x,y)
        '''


        # call the function to get the recommendation and then load it into the textbox

        #Provide two list of data and draw the bar chart
    def barPainting(self,lables,data):
        width = 0.5
        self.axes = self.figureComp.add_subplot(111)
        self.axes.clear()
        self.axes.bar([0,1,2,3],data,width,align="center")
        self.axes.set_xticks([0,1,2,3])
        self.axes.set_xticklabels(lables, rotation=40)
        self.axes.tick_params(axis='x', labelsize=8)



    def onActivated(self, text):

        print(text+' Is selected')
        #print(ScorceCode.forCountry(text,self.productName))
        CountrySelected = text
        print('breakpoint')
        ls1 = ScorceCode.forCountry(CountrySelected,self.productName)
        #ls1.to_csv('C:/Users/lakshay/Desktop/udemy/PRI_Exported_CSV_files/finlistState.csv')
        #print(ls1)
        finlistState = ls1.index.tolist()
        self.gs1 = ls1

        #print(finlistState)
        #self.textEdit3.setText(ls1.to_string())

        tableFor = "country"

        self.createTable(tableFor)
        print('breakpoint 1')

       # self.stateTextBox.clear()
        #self.cityTextBox.clear()
       # self.stateTextBox.addItems(finlistState)

        #print(self.stateTextBox.activated[str].connect(self.onActivated1))



        self.plot(ls1)




# have to pass the state value to this method !!!!!!!!!!!!!!!!!!
    '''
    def onActivated1(self, StateSelected):


       try:
        self.cityTextBox.clear()
        print("state selected is ")
        print(StateSelected)
        print('value in state box :')
        print(self.stateTextBox.currentText())
        print(self.countryTextBox.currentText())
        StateSelected= self.stateTextBox.currentText()
        CountrySelected=self.countryTextBox.currentText()

        ls2=ScorceCode.forState(CountrySelected,StateSelected,self.productName)
        #ls2.to_csv('C:/Users/lakshay/Desktop/udemy/PRI_Exported_CSV_files/finlistCity.csv')
        self.gs2 = ls2
        finlistCity = ls2.index.tolist()

        #self.textEdit3.setText(ls2.to_string())
        tableFor = "state"
        self.createTable(tableFor)

        print('list of city')
        #print(finlistCity)


        self.cityTextBox.clear()
        self.cityTextBox.addItems(finlistCity)



        self.cityTextBox.activated[str].connect(self.onActivated2)
        self.plot(ls2)


       except:
        print('An error occured while retrieving the cities of the states.')




# have to pass the state value and city to this method !!!!!!!!!!

    def onActivated2(self, CitySelected):
        try:
         StateSelected = self.stateTextBox.currentText()
         CountrySelected = self.countryTextBox.currentText()
         print('final country selected')
         print(CountrySelected)
         print('final state selected')
         print(StateSelected)
         print("final city selected is ")
         print(CitySelected)
         print('Number of total internet users in '+ CitySelected+ ' is:' )
         print(ScorceCode.forTotalUsers(CountrySelected,CitySelected))


         ls2 = ScorceCode.forState(CountrySelected, StateSelected, self.productName)

         UserPercentage = int(ls2.loc[CitySelected, :])
         print(UserPercentage)

         totalUsers = ScorceCode.forTotalUsers(CountrySelected, CitySelected)
         print(totalUsers)

         finalUsers=int((totalUsers*UserPercentage)/100)

         totalPopulation= ScorceCode.forTotalPop(CitySelected)
         totalPenitration=ScorceCode.forTotalPenitration(CountrySelected)

         ratio = int((finalUsers / totalPopulation) * 100)

         self.recommendationText.setText("There are total of " + str(finalUsers) + " people searching for the keyword out of " + str(totalPopulation) + " people in the city of " + CitySelected + " which gives us the ratio of " + str(ratio) + "% of users searching for this keyword and the percentage of internet penetration is " + str(totalPenitration) + "%")
         print('end')
        except:
         print('An error occured while retrieving the population data of the city: ' +CitySelected)


    def createTable(self, tableFor):
        # Create table

        # print("Table data " + self.tableDf)PROGRAM RUNNING?????????

        # find the table length
        if (tableFor == "world"):
            self.lsTest = self.gs
        if(tableFor=="country"):
            self.lsTest = self.gs1

        #if(tableFor== "state"):
         #   self.lsTest= self.gs2




        # print(self.lsTest)
        rows = self.lsTest.count()
        columns = 2
        # rows=10
        #print(rows)

        #print(columns)

        # set the rows and columns of the table
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(columns)

        i = 0

        for index, value in self.lsTest.iterrows():
            #print(value[0])
            if i < int(rows):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(index))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(value[0])))
                i = i + 1
            ## self.tableWidget.setItem(index, 2, QTableWidgetItem(row['']))

        # for x in rows:
        # for y in columns:

        # if(y==0)
        # self.tableWidget.setItem(x, y, QTableWidgetItem(self.tableDf[x][y]))

        # self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))'''


    def show_model(self):
        font = QtGui.QFont()
        font.setFamily('Lucida')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.textEdit3.setCurrentFont(font)

        # selmodel = self.creSelectModel[str(self.comboBox.currentText())]
        self.textEdit3.setText("1234566465464")

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

        self.countryTextBox.activated[str].connect(self.onActivated)


        ls = ScorceCode.forWorld(self.productName)
        #print(ls)
        #ls.to_csv('C:/Users/lakshay/Desktop/udemy/PRI_Exported_CSV_files/finlistWorld.csv')
        self.gs = ls
        finlist = ls.index.tolist()
        #print(finlist)
        print('someht')
        self.countryTextBox.clear()
        self.countryTextBox.addItems(finlist)
        self.countryTextBox.activated[str].connect(self.onActivated)
        #makeitastring = ''.join(map(str, finlist))

        #print('the string is')
        #print(makeitastring)

        tableFor = "world"
        #self.textEdit3.setText(ls.to_string())
        self.createTable(tableFor)

        self.plot(ls)



    def clear_on_click(self):
        self.productTextBox.clear()
        print('all clear')

    def plot(self,data):

        # hit only if we have values on all the four components
        #if (self.productTextBox.text()):

            print("Inside the plot method")
            # Call the api #TODO


            #statisticsPerCountry = SourceCode.forCountry(self.selectedCountry,self.productTextBox.text())
            #statisticsPerState
            #statisticsPerUsers

            print('plotBreak')



            # create an axis
            ax = self.figure.add_subplot(111)

            # discards the old graph
            ax.clear()

            # plot data
            ax.plot(data, '*-')

            # refresh canvas
            self.canvas.draw()

       # else:
          #  QMessageBox.about(self, "Inputs", "Please check your inputs")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    barpainting()

