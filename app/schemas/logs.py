from pydantic import BaseModel
from datetime import datetime

class LogCreate(BaseModel):
    host: str
    service: str
    level: str
    message: str
    timestamp: datetime | None = None
from pydantic import BaseModel
from datetime import datetime

class LogEntry(BaseModel):
    host: str
    service: str        # consul | nomad | postgres | fluentbit
    level: str          # info | warning | error
    message: str
    timestamp: datetime
from pydantic import BaseModel
from datetime import datetime

class LogCreate(BaseModel):
    host: str
    service: str
    level: str
    message: str
    timestamp: datetime | None = None

