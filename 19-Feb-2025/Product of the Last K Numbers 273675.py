# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:
    def __init__(self):
        self.suffix_product = [1]
    def add(self, num: int) -> None:
        if num ==0:
            self.suffix_product = [1]
        else:
            self.suffix_product.append(num * self.suffix_product[-1])
    def getProduct(self, k: int) -> int:
        if k >= len(self.suffix_product):
            return 0
        return (self.suffix_product[-1] // self.suffix_product[-k-1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)