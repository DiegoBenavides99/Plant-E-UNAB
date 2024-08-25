from django.db import models

# Create your models here.
class USUARIO(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()
    domicilio = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_usuario


class PLANTA(models.Model):
    id_planta = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(USUARIO, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    estado_salud_sano = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class HONGO(models.Model):
    id_hongo = models.AutoField(primary_key=True)
    nombre_cientifico = models.CharField(max_length=100)
    tratamiento_recomendado = models.TextField()
    nombre_comun = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cientifico


class DIAGNOSTICO(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    id_planta = models.ForeignKey(PLANTA, on_delete=models.CASCADE)
    id_hongo = models.ForeignKey(HONGO, on_delete=models.CASCADE)
    fecha_diagnostico = models.DateTimeField()
    nivel_gravedad = models.CharField(max_length=20)
    observaciones = models.TextField()

    def __str__(self):
        return f"Diagnostico {self.id_diagnostico} - Planta {self.id_planta}"


class IMAGEN(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_planta = models.ForeignKey(PLANTA, on_delete=models.CASCADE)
    ruta_imagen = models.CharField(max_length=255)
    fecha_subida = models.DateTimeField()

    def __str__(self):
        return f"Imagen {self.id_imagen} - Planta {self.id_planta}"


class TRATAMIENTO(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    id_diagnostico = models.ForeignKey(DIAGNOSTICO, on_delete=models.CASCADE)
    fecha_tratamiento = models.DateTimeField()
    tipo_tratamiento = models.CharField(max_length=50)
    resultado = models.CharField(max_length=50)
    seguimiento_requerido = models.BooleanField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tratamiento {self.id_tratamiento} - Diagnostico {self.id_diagnostico}"


class HISTORIAL_TRATAMIENTO(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_planta = models.ForeignKey(PLANTA, on_delete=models.CASCADE)
    id_tratamiento = models.ForeignKey(TRATAMIENTO, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateTimeField()
    resultado = models.CharField(max_length=50)
    notas = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Historial {self.id_historial} - Planta {self.id_planta}"
