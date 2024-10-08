class BrowserHistory:

    def __init__(self, homepage: str):
        self.nums: list(str) = [homepage]
        self.index: int = 0

    def visit(self, url: str) -> None:
        if self.index == len(self.nums)-1:
            self.nums.append(url)
            self.index += 1
        else:
            self.index += 1
            self.nums[self.index] = url
            self.nums = self.nums[:self.index+1]

    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index < 0:
            self.index = 0
        return self.nums[self.index]

    def forward(self, steps: int) -> str:
        n: int = len(self.nums)-1
        self.index += steps
        if self.index > n:
            self.index = n
        return self.nums[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)