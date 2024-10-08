from typing import Any

from wildlife_tracker.habitat_management.habitat import Habitat

class Migration:
    def __init__(self, 
                 migration_id: int, 
                 species: str,
                 start_date: str = '', 
                 current_date: str = '', 
                 current_location: str = '', 
                 destination: Habitat = None, 
                 status: str = "Scheduled") -> None:
        self.migration_id: int = migration_id
        self.species: str = species
        self.start_date: str = start_date
        self.current_date: str = current_date
        self.current_location: str = current_location
        self.destination: Habitat = destination
        self.status: str = status
    
    def update_migration_details(self, migration_id: int, **kwargs: Any) -> None:
        pass

    def get_migration_details(self, migration_id: int) -> dict[str, Any]:
        pass