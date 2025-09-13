
#### Preguntas guía (responde en `Reporte.md`)

1. **HTTP:** explica **idempotencia** de métodos y su impacto en *retries*/*health checks*. Da un ejemplo con `curl -X PUT` vs `POST`.

```
Idempotencia es que realizar los mismos metodos debe producir los mismos resultados y su impacto en retries debe ser que el mismo usuario haga reintentos de peticiones pero con el mismo nombre es decir se usaria PUT y health checks de la misma manera si existe alguna falla de comprobacion automatica debe usarse PUT , PUT es idempotente y POST no.
```
2. **DNS:** ¿por qué `hosts` es útil para laboratorio pero no para producción? ¿Cómo influye el **TTL** en latencia y uso de caché?
```
porque usando hosts es mas rapido localmente, el TTL influye en que mientras mas alto sea el uso de cache sera mas aprovechado y si es bajo habra menor latencia.
```
3. **TLS:** ¿qué rol cumple **SNI** en el *handshake* y cómo lo demostraste con `openssl s_client`?
```
SNI en el handshake TLS indica el dominio solicitado, permitiendo multiples certificados en un mismo servidor. Con openssl s_client -"nombredelserver" se evidencia la diferencia, mostrando certificados distintos segun configuracion enviada.
```
4. **12-Factor:** ¿por qué **logs a stdout** y **config por entorno** simplifican contenedores y CI/CD?
```
Usar logs en stdout y config por entorno simplifica contenedores porque evita dependencias internas/ facilita CI/CD al estandarizar salida, separacion de configuracion y despliegues reproducibles en diferentes ambientes sin modificar codigo.
```
5. **Operación:** ¿qué muestra `ss -ltnp` que no ves con `curl`? ¿Cómo triangulas problemas con `journalctl`/logs de Nginx?
```
ss -ltnp muestra sockets, puertos y procesos que curl no muestra y para triangulos de fallas se usa journalctl y logs de Nginx, correlacionando errores de red, puertos y respuestas HTTP
```
