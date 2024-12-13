from entities.state import State
from entities.instrument import Instrument
from entities.city import City

from entities.tracked_entity import TrackedEntity

from service.pendency_system import PendencySystem

class Demo:

    @staticmethod
    def run() -> None:
        print("Pendency System initialized...\n")
        pendency_system = PendencySystem.get_instance()

        upi = Instrument(1, "UPI")
        wallet = Instrument(2, "Wallet")

        karnataka = State(2, "Karnataka")
        jaipur = State(3, "Jaipur")

        bangalore = City(4, "Bangalore")
        mysore = City(5, "Mysore")
        rajasthan = City(6, "Rajasthan")

        tracked_entity_1112 =  TrackedEntity(1112)
        tracked_entity_1112.add_to_hierarchy(upi)
        tracked_entity_1112.add_to_hierarchy(karnataka)
        tracked_entity_1112.add_to_hierarchy(bangalore)

        tracked_entity_2451 = TrackedEntity(2451)
        tracked_entity_2451.add_to_hierarchy(upi)
        tracked_entity_2451.add_to_hierarchy(karnataka)
        tracked_entity_2451.add_to_hierarchy(mysore)

        tracked_entity_3421 = TrackedEntity(3421)
        tracked_entity_3421.add_to_hierarchy(upi)
        tracked_entity_3421.add_to_hierarchy(rajasthan)
        tracked_entity_3421.add_to_hierarchy(jaipur)

        tracked_entity_1221 = TrackedEntity(1221)
        tracked_entity_1221.add_to_hierarchy(wallet)
        tracked_entity_1221.add_to_hierarchy(karnataka)
        tracked_entity_1221.add_to_hierarchy(bangalore)

        tracked_entity_4221 = TrackedEntity(4221)
        tracked_entity_4221.add_to_hierarchy(wallet)
        tracked_entity_4221.add_to_hierarchy(karnataka)
        tracked_entity_4221.add_to_hierarchy(bangalore)

        pendency_system.start_tracking(tracked_entity_1112)
        pendency_system.start_tracking(tracked_entity_2451)
        pendency_system.start_tracking(tracked_entity_3421)
        pendency_system.start_tracking(tracked_entity_1221)

        # Case 1:
        print("\nCase I:\n")
        print(f"Output: {pendency_system.get_counts(["UPI"])}")
        print(f"Output: {pendency_system.get_counts(["UPI", "Karnataka"])}")
        print(f"Output: {pendency_system.get_counts(["UPI", "Karnataka", "Bangalore"])}")
        print(f"Output: {pendency_system.get_counts(["Bangalore"])}")

        print()
        pendency_system.start_tracking(tracked_entity_4221)
        pendency_system.stop_tracking(1112)
        pendency_system.stop_tracking(2451)

        # Case 2:
        print("\nCase II:\n")
        print(f"Output: {pendency_system.get_counts(["UPI"])}")
        print(f"Output: {pendency_system.get_counts(["Wallet"])}")
        print(f"Output: {pendency_system.get_counts(["UPI", "Karnataka", "Bangalore"])}")


if __name__ == "__main__":
    Demo.run()