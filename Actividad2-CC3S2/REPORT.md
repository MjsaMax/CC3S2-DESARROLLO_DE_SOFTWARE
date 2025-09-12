
#### Preguntas guía (responde en `Reporte.md`)

1. **HTTP:** explica **idempotencia** de métodos y su impacto en *retries*/*health checks*. Da un ejemplo con `curl -X PUT` vs `POST`.

```
Idempotencia es que realizar los mismos metodos debe producir los mismos resultados y su impacto en retries debe ser que el mismo usuario haga reintentos de peticiones pero con el mismo nombre es decir se usaria PUT y health checks de la misma manera si existe alguna falla de comprobacion automatica debe usarse PUT , PUT es idempotente y POST no.
```
2. **DNS:** ¿por qué `hosts` es útil para laboratorio pero no para producción? ¿Cómo influye el **TTL** en latencia y uso de caché?
```
porque usando hosts es mas rapido localmente, el TTL influye en que mientras mas alto sea el uso de cache sera mas aprovechado y si es bajo no se aprovechara
```
3. **TLS:** ¿qué rol cumple **SNI** en el *handshake* y cómo lo demostraste con `openssl s_client`?
```
asdas
```
4. **12-Factor:** ¿por qué **logs a stdout** y **config por entorno** simplifican contenedores y CI/CD?
```
asdas
```
5. **Operación:** ¿qué muestra `ss -ltnp` que no ves con `curl`? ¿Cómo triangulas problemas con `journalctl`/logs de Nginx?
```
asdas
```
