"""
    - PACKAGE class: **archivos**
    - Autor: pedrogrr@gmail.com
    - Fecha publicación: Noviembre 2022
"""

class archivos:

# ====================== CONSTRUCTOR ==================================================
    def __init__(self, ruta):        
        if ruta is not None:
            self._ruta = ruta.copy()   
# ====================== FUNCIONES DE SOPORTE =========================================                
    def buscar_archivos(self,ruta): 
        archivos_texto=[] 
        archivos = glob.glob(os.path.join(ruta, '*.txt'))
        for archivo in archivos: 
            if archivo[-4:] == '.txt': 
                archivos_texto.append(archivo) 
        return archivos_texto 