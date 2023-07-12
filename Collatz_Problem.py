class Solution:
    @staticmethod
    def collatz_sequence(n):
        ans=[n]
        while n>1:
            if n%2==0:
                n//=2
                ans.append(n)
            else:
                n=3*n+1
                ans.append(n)
        return ans

if __name__ == '__main__':
    obj=Solution()
    print(*obj.collatz_sequence(5))
    print(*obj.collatz_sequence(1))
    print(*obj.collatz_sequence(4))
