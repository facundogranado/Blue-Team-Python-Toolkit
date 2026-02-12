#  Blue Team Python Toolkit

## Detección • Análisis 


##  Descripción del Proyecto

**Blue Team Python Toolkit** es un conjunto de herramientas desarrolladas en Python orientadas a la detección, análisis e investigación de eventos de seguridad desde una perspectiva defensiva.

El proyecto está diseñado para simular escenarios de ciberseguridad, aplicando conceptos técnicos utilizados en entornos de monitoreo, análisis de tráfico y respuesta ante incidentes.


#  Objetivos

Este proyecto busca demostrar:

* Análisis de tráfico de red
* Detección de patrones de Command & Control (C2)
* Identificación de TLS Beaconing
* Parsing y correlación de logs
* Enriquecimiento de indicadores (IP / dominio)
* Aplicación práctica de fundamentos de Threat Hunting


#  Escenarios Simulados

Los scripts incluidos permiten replicar situaciones comunes en entornos defensivos:

###  Detección de Comunicación C2

Identificación de conexiones periódicas hacia destinos externos que pueden indicar actividad de beaconing sobre TLS.

###  Análisis de Logs de Seguridad

Procesamiento de registros de firewall, proxy o IDS para detectar IPs frecuentes, comportamientos anómalos y patrones repetitivos.

###  Investigación de Indicadores

Obtención de contexto adicional sobre IPs sospechosas (ASN, geolocalización, organización) para apoyar la toma de decisiones.

#  Estructura del Repositorio

```
blue-team-python-toolkit/
│
├── beaconing_detector.py      # Detección de posible TLS beaconing
├── log_parser.py              # Análisis de logs de seguridad
├── ip_enrichment.py           # Enriquecimiento de indicadores
├── samples/                   # Logs simulados para pruebas
└── README.md
```

Cada módulo representa una capacidad técnica relevante dentro de un enfoque Blue Team.


#  Conceptos Técnicos Aplicados

* Command & Control (C2)
* TLS Beaconing
* Análisis temporal de tráfico
* Parsing y normalización de logs
* Identificación de patrones anómalos
* Enriquecimiento contextual de indicadores

