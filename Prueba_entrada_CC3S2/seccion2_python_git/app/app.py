# Implementa la función summarize y el CLI.
# Requisitos:
# - summarize(nums) -> dict con claves: count, sum, avg
# - Valida que nums sea lista no vacía y elementos numéricos (acepta strings convertibles a float).
# - CLI: python -m app "1,2,3" imprime: sum=6.0 avg=2.0 count=3
import sys
def summarize(nums:list)->dict:  # TODO: tipado opcional
    if not nums:
        raise ValueError("La lista está vacía")
    valores = []
    for n in nums:
        valores.append(float(n))
    return {
    "count": len(valores),
    "sum": sum(valores),
    "avg": sum(valores)/len(valores)
    }

        


if __name__ == "__main__":
    raw = sys.argv[1] if len(sys.argv) > 1 else ""
    items = [p.strip() for p in raw.split(",") if p.strip()]
    result = summarize(items)
    print(f"sum={result['sum']} avg={result['avg']} count={result['count']}")
