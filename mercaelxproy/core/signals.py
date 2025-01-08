from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Provincia, Ciudad

# Diccionario de capitales de provincia
CAPITALES = {
    "ALB": "Albacete",
    "ALC": "Alicante",
    "ALM": "Almería",
    "BADA": "Badajoz",
    "BCN": "Barcelona",
    "BIL": "Bilbao",
    "BUR": "Burgos",
    "CAD": "Cádiz",
    "CAC": "Cáceres",
    "CAS": "Castellón",
    "CEU": "Ceuta",
    "CIR": "Ciudad Real",
    "COR": "Córdoba",
    "CUE": "Cuenca",
    "GIR": "Girona",
    "GRA": "Granada",
    "GUA": "Guadalajara",
    "HUE": "Huelva",
    "JAÉ": "Jaén",
    "LEO": "León",
    "LLE": "Lleida",
    "LOG": "Logroño",
    "LPA": "Las Palmas",
    "LUG": "Lugo",
    "MAD": "Madrid",
    "MAL": "Málaga",
    "MEL": "Melilla",
    "MUR": "Murcia",
    "ORE": "Ourense",
    "OVI": "Oviedo",
    "PAL": "Palencia",
    "PAL": "Palma",
    "PAM": "Pamplona",
    "SAL": "Salamanca",
    "SAN": "Santander",
    "SANT": "Santa Cruz de Tenerife",
    "SEG": "Segovia",
    "SEV": "Sevilla",
    "SORI": "Soria",
    "TAR": "Tarragona",
    "TER": "Teruel",
    "TOLE": "Toledo",
    "VAL": "Valencia",
    "VALL": "Valladolid",
    "VGO": "Vigo",
    "VIT": "Vitoria",
    "ZAM": "Zamora",
    "ZAR": "Zaragoza"
}

@receiver(post_save, sender=Provincia)
def crear_capital(sender, instance, created, **kwargs):
    if created:
        capital_nombre = CAPITALES.get(instance.codigo)
        if capital_nombre:
            Ciudad.objects.create(codigo=instance.codigo, nombre=capital_nombre, provincia=instance)