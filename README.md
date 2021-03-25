# Agregar imagen en QLabel (keep & ignore)

**Indice**
  * [Recursos utilizados](#recursos-utilizados)
  * [Ruta de imagen](#ruta-de-imagen)
  * [ nsertarción y borrado de imagen](#insertarción-y-borrado-de-imagen)
  * [Imagen Ignore (Elastica)](#imagen-ignore-(elastica))
  * [Imagen Keep (Proporcional)](#imagen-keep-(proporcional))
  * [Imágenes utilizadas](#imágenes-utilizadas)
  * [Previsualización](#previsualización)

# Recursos utilizados

`pip install PySide2`

[Documentación QLabel](https://doc.qt.io/qt-5/qpixmap.html "Doc QLabel")

# Ruta de imagen

Para ello tabajaremos con la funcion `QFileDialog` 

Parametros de QFileDialog
```
QFileDialog().getOpenFileName(None, 'Titulo', 'ruta por defecto', 'extensiones de archivo')
```
En el codigo retorna la posicion 0 ya que en allí se encuentra la ruta del archivo seleccionado

```python
def obtener_ruta(self):
    ruta = QFileDialog().getOpenFileName(None, 'Seleccionar archivo',r'./images',
                                        "Archivos de imagen (*.jpg *.png);;Imagen (*.jpg);;Imagen (*.png)")
    return ruta[0]
```

Para verificar que la ruta es valida lo condicionamos de la siguiente manera

```python
if(ruta==''):
	print("Invalida")
else:
	print("Valido")
```
# Insertarción y borrado de imagen

**Insertar**

Cargar mediante una ruta

```
imagen = QPixmap.fromImage("./imagen1.fpg")
```

He insertarlo en el label

```python
label.setPixmap(imagen)
```

**Eliminar**

Para restablecer el `QLabel`, utilizamos el metodos `clear`

```python
label.clear()
```



# Imagen Ignore (Elastica)

**Configuración previa**

Al agregar el objeto `QLabel`, debemos configurar con `scaledContents` 

![](https://1.bp.blogspot.com/-JnEm_hpshPk/YFkqBLs_ljI/AAAAAAAAAI4/8dZmrIh-Cu0ytctNl4BH5_8YjbRcG6FKgCLcBGAsYHQ/s1600/25424.png)

y en codigo procedemos a insertar la imagen

```python
imagen = QPixmap.fromImage(ruta)
label.setPixmap(imagen)
```

En ese apartado no intereza la proporción debido a que adaptara la imagen a todo el tamaño del `QLabel`
![](https://1.bp.blogspot.com/-hWx_uv_wSEs/YFkowkhEi_I/AAAAAAAAAIw/taDCLeJ26FkaOPKnoij6BRBc56dPl4LnACLcBGAsYHQ/s1600/1421342.jpg)

# Imagen Keep (Proporcional)

**Configuración previa**

Al agregar el objeto `QLabel`, debemos configurar el ambos alignament en el centro:  `AlinearCentroH` y `AlinearCentroV`

![](https://1.bp.blogspot.com/-S3grNAffchg/YFkqBTf5obI/AAAAAAAAAI8/kl_FpnYZt2IRmEpsUnKAffUQYOqRqInnQCLcBGAsYHQ/s1600/45450.png)


Antes de insertar la imagen, se procede a verificar el tamaño de la imagen,
en donde si

- ` alto_imagen` < `ancho_imagen` : se escala el ancho de imagen con respecto al ancho del label

- `alto_imagen` > `ancho_imagen` : se escala el ancho de imagen con respecto al ancho del label

```python
imagen=QPixmap.fromImage(QImage(ruta))#imagen.jpg

if(imagen.height()<imagen.width()):
    imagen = imagen.scaledToHeight(label.height(),Qt.SmoothTransformation)
	
else:
    imagen = imagen.scaledToWidth(label.width(),Qt.SmoothTransformation)
	
label.setPixmap(imagen)
```

![](https://1.bp.blogspot.com/-4ebXM1wCITM/YFkDloLaK0I/AAAAAAAAAIU/otly4Zf99TQZ15w9AllJZbCN7gq7jcqIACLcBGAsYHQ/s1600/142314.jpg)

# Imágenes utilizadas

- [Imagen 1](https://pics.alphacoders.com/pictures/view/377738 "Imagen 1")
- [Imagen 2](https://pics.alphacoders.com/pictures/view/365718 "Imagen 2")

# Previsualización

![](https://1.bp.blogspot.com/-NLuOv1VTPP0/YFkHiQo7OJI/AAAAAAAAAIo/I7li26Gs7Qcs78sxa1zvpxaOG7D6SBklgCLcBGAsYHQ/s1600/516514515.jpg)