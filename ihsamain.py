from ihsa_oop import Problem
from PyQt4 import QtGui
import sys
import ihsagui


class IHSAApp(QtGui.QMainWindow, ihsagui.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.Oblicz.clicked.connect(self.funkcjaoblicz)
		self.Zamknij.clicked.connect(self.funkcjazamknij)
	def funkcjaoblicz(self):
		ranges = []
		ranges.append(float(self.dg1.value()))
		ranges.append(float(self.gg1.value()))
		ranges.append(float(self.dg2.value()))
		ranges.append(float(self.gg2.value()))		
		function = self.ownFunction.text()
		if function: 
			if 'x3' in function:
    				dimensions = 3
    				ranges.append(float(self.dg3.value()))
    				ranges.append(float(self.gg3.value()))
			else:
    				dimensions = 2
		else:
    			dimensions = 0


		prob = Problem(function, dimensions, ranges)		
		prob.draw_contour(ranges)
		prob.solve()

		wyniki = prob.harmony_memory
		for i in range(7):
			x1 = QtGui.QTableWidgetItem(str(wyniki[i][0]))
			x2 = QtGui.QTableWidgetItem(str(wyniki[i][1]))
			self.tableWidget.setItem(i, 0, x1)
			self.tableWidget.setItem(i, 1, x2)
			if dimensions == 3:
				x3 = QtGui.QTableWidgetItem(str(wyniki[i][2]))
				self.tableWidget.setItem(i, 2, x3)
		wartosci = prob.values
		for i in range(7):
			y = QtGui.QTableWidgetItem(str(wartosci[i]))
			self.tableWidget.setItem(i, 3, y)


	def funkcjazamknij(self):
		sys.exit()

def main():
	app = QtGui.QApplication(sys.argv)
	form = IHSAApp()
	form.show()
	app.exec_()
	

if __name__ == '__main__':
	main()
