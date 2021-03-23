# modulos de PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Qt

# diseño
from view.ui_Imagenes import Ui_Imagenes

class Ui_Principal(QMainWindow):

    def __init__(self):
        super(Ui_Principal, self).__init__()
        
        self.raizImg = Ui_Imagenes()
        self.raizImg.setupUi(self)

        # IGNORE *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

        # cargar
        self.raizImg.btncar1.clicked.connect(lambda : 
                self.cargar_imagen_ignore(self.raizImg.lblcover1)
            )

        # restablecer
        self.raizImg.btndel1.clicked.connect(lambda : 
                self.none_imagen(self.raizImg.lblcover1)
            )

        # KEEP *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

        # cargar
        self.raizImg.btncar2.clicked.connect(lambda : 
                self.cargar_imagen_keep(self.raizImg.lblcover2)
            )

        # restablecer
        self.raizImg.btndel2.clicked.connect(lambda : 
                self.none_imagen(self.raizImg.lblcover2)
            )
    
    # RUTA DE IMAGEN
    def obtener_ruta(self):
        """obtener ruta de la imagen"""
        # segun las extensiones correspondientes
        ruta = QFileDialog().getOpenFileName(None, 'Seleccionar archivo',r'./images',
                                            "Archivos de imagen (*.jpg *.png);;Imagen (*.jpg);;Imagen (*.png)")
        return ruta[0]

    # RESTABLECER LABEL
    def none_imagen(self, label):
        """retiramos todo el contenido del label"""
        label.clear()

    # IMAGEN CON PROPORCION
    def cargar_imagen_keep(self, label):
        """insertar imagen manteniendo proporcion"""
        
        # verificamos que la ruta sea valida, si no retornamos /*/*/*/*/*/
        ruta = self.obtener_ruta()
        if(ruta==''):return

        # generamos el Pixmap en base a la ruta de imagen /*/*/*/*/*/
        imagen=QPixmap.fromImage(QImage(ruta))#imagen.jpg

        if(imagen.height()<imagen.width()):
            # mantiene proporcion segun el ALTO DE IMAGEN /*/*/*/*/*/
            'todo en base al alto del label'
            imagen = imagen.scaledToHeight(label.height(),Qt.SmoothTransformation)

        else:
            # mantiene proporcion segun el ANCHO DE IMAGEN /*/*/*/*/*/
            'todo en base al ancho del label'
            imagen = imagen.scaledToWidth(label.width(),Qt.SmoothTransformation)

        # insertar imagen /*/*/*/*/*/
        label.setPixmap(imagen)

    # IMAGEN ELASTICA
    def cargar_imagen_ignore(self, label):
        """insertar imagen elastica"""

        # verificamos que la ruta sea valida, si no retornamos /*/*/*/*/*/
        ruta = self.obtener_ruta()
        if(ruta==''):return

        # generamos el Pixmap en base a la ruta de imagen /*/*/*/*/*/
        imagen = QPixmap.fromImage(ruta)

        # insertar imagen /*/*/*/*/*/
        label.setPixmap(imagen)


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    mi_aplicacion = Ui_Principal()
    mi_aplicacion.show()
    sys.exit(app.exec_())