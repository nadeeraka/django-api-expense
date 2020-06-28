from typing import List
from app.models import Saving

def saving_resolver(savings:List[Saving]):
    print(savings)