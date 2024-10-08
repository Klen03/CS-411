from typing import Any, Optional

class Animal:
    def _init_(self,
               animal_id: int,
               species: str,
               age: Optional[int] = None,
               health_status: Optional[str] = None,
               habitat_id: Optional[int] = None) -> None:
        
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status
        self.habitat_id = habitat_id

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass

    def get_animal_details(self) -> dict[str, Any]:
        pass
