from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationPath:
    def __init__(self,
                 path_id: int,
                 species: str,
                 start_location: Habitat,
                 destination: Habitat,
                 duration: Optional[int] = None) -> None:
        self.path_id: int = path_id
        self.species: str = species
        self.start_location = start_location
        self.destination: Habitat = destination
        self.duration: Optional[int] = duration
    
    def get_migration_path_details(self, path_id) -> dict:
        pass
    
    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass
