from typing import List, Dict


class CompositeModule:
    def __init__(self):
        self.children: List[Dict] = []

    def add(self, block: Dict):
        """Agrega un bloque de recurso o módulo a los hijos."""
        self.children.append(block)

    def export(self) -> Dict:
        """Exporta los hijos mergeados recursivamente en un JSON válido para Terraform."""
        merged: Dict = {"module": {}, "resource": {}}
        
        for child in self.children:
            # Procesar módulos si existen
            if "module" in child:
                merged["module"].update(child["module"])
            
            # Procesar recursos
            if "resource" in child:
                for rtype, resources in child["resource"].items():
                    merged["resource"].setdefault(rtype, {}).update(resources)
        
        # Limpiar claves vacías
        if not merged["module"]:
            del merged["module"]
        
        return merged
