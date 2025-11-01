import uuid
from datetime import datetime


class NullResourceFactory:
    @staticmethod
    def create(name: str, triggers: dict = None) -> dict:
        triggers = triggers or {
            "factory_uuid": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat()
        }
        return {
            "resource": {
                "null_resource": {
                    name: {"triggers": triggers}
                }
            }
        }


class TimestampedNullResourceFactory(NullResourceFactory):
    @staticmethod
    def create(name: str, fmt: str = '%Y%m%d') -> dict:
        """Crea null_resource con timestamp formateado según fmt."""
        ts = datetime.utcnow().strftime(fmt)
        triggers = {
            "factory_uuid": str(uuid.uuid4()),
            "timestamp": ts,
            "timestamp_format": fmt
        }
        return {
            "resource": {
                "null_resource": {
                    name: {"triggers": triggers}
                }
            }
        }
