from unittest.mock import patch

from patterns.creational.abstract_factory import Dog, PetShop


class TestPetShop:
    def test_dog_pet_shop_shall_show_dog_instance(self):
        dog_pet_shop = PetShop(Dog)
        with patch.object(Dog, "speak") as mock_Dog_speak:
            pet = dog_pet_shop.buy_pet("")
            pet.speak()
            assert mock_Dog_speak.call_count == 1
