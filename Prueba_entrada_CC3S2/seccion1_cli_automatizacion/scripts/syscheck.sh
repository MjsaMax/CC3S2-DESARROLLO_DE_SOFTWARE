#!/usr/bin/env bash
set -euo pipefail
trap 'echo "[ERROR] Falló en línea $LINENO" >&2' ERR

mkdir -p reports

# TODO: HTTP-guarda headers y explica código en 2-3 líneas al final del archivo
{
  echo "curl -I example.com"
  curl -Is https://example.com | sed '/^\r$/d'
  echo
  echo "Explicación (editar): Código HTTP/2 es el protocolo que se esta usando y el 200 significa que se proceso la petición sin errores."
  echo "content type: Significa que el contenido recibido es de tipo HTML por lo que el navegador debe interpretarlo como paginaWeb"
  echo "etag es un identificador para validar cache,date es la fecha, y el alt-svc servicio alternativo en este caso puede ser HTTP/3(h3)"
} > reports/http.txt

# TODO: DNS — muestra A/AAAA/MX y comenta TTL
{
  echo "A";    dig A example.com +noall +answer
  echo "AAAA"; dig AAAA example.com +noall +answer
  echo "MX";   dig MX example.com +noall +answer
  echo
  echo "Nota (editar): TimeToLive, TTL alto vs bajo impacta en la velocidad de la pagina web, ya que si es bajo sera mas fluido el uso del servidor ya que el cache esta mas tiempo "
  echo "mientras que con TTL bajo, ofrece mayor dinammismo del DNS y en la resolucion de nombres"
  echo "La A indica las direcciones IPv4 y AAAA IPv6 4 veces que el IPv4 en tamaño y muestran la cantida de servidores que tienen cada tipo,y MX muestra la cantidad de servidores de mensajeria" 
} > reports/dns.txt

# TODO: TLS - registra versión TLS
{
  echo "TLS via curl -Iv"
  curl -Iv https://example.com 2>&1 | sed -n '1,20p'
  echo "La version es TLSv1.3 la que muestra el dominio example.com"
} > reports/tls.txt

# TODO: Puertos locales - lista y comenta riesgos
{
  echo "ss -tuln"
  ss -tuln || true
  echo
  echo "Riesgos (editar): Puertos abiertos innecesarios pueden ser vulnerables a ataques, o permitir accesos no autorizados al sistema."
} > reports/sockets.txt

echo "Reportes generados en ./reports"
