from typing import List


class MoneyTransfer:
    def __init__(self, money: List[int], threshold: int) -> None:
        self.money = money
        self.threshold = threshold
        self.sorted_indices = sorted(range(len(money)), key=lambda i: money[i])  # Track original indices

    def transfer(self) -> List[int]:
        money = self.money[:]  # Work on a copy of the original money array
        sorted_indices = self.sorted_indices
        transfers = []

        left = 0
        right = len(money) - 1

        while left < right and money[sorted_indices[left]] < self.threshold:
            deficit = self.threshold - money[sorted_indices[left]]

            # Find a suitable donor
            while right > left and (money[sorted_indices[right]] - self.threshold < deficit):
                right -= 1

            if right <= left:
                print("Transfer not possible.")
                return []  # Redistribution not possible

            # Perform the transfer
            donor_idx = sorted_indices[right]
            receiver_idx = sorted_indices[left]
            money[donor_idx] -= deficit
            money[receiver_idx] += deficit
            transfers.append(f"Transferring {deficit} from index {donor_idx} to index {receiver_idx}.")
            left += 1

        print("\n".join(transfers))
        return money if all(m >= self.threshold for m in money) else []


if __name__ == "__main__":
    inputs = [
        {"money": [3, 5, 11, 28], "threshold": 10},  # Possible
        {"money": [3, 5, 11, 1], "threshold": 10},  # Not possible
        {"money": [3, 5, 22], "threshold": 10},     # Possible
        {"money": [3, 5, 21], "threshold": 10},     # Possible
    ]
    for inp in inputs:
        mt = MoneyTransfer(money=inp["money"], threshold=inp["threshold"])
        print(mt.transfer())
        print()
