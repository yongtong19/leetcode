from typing import List
from math import factorial


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0

        words = ["".join(sorted(set(word))) for word in words]
        words.sort()

        i = 0
        while i < len(words):
            j = i + 1
            while j < len(words) and words[j] == words[i]:
                j += 1

            if j - i > 1:
                ans += self.comb(j - i, 2)

            i = j

        return ans

    def comb(self, a, b):
        return factorial(a) // (factorial(b) * factorial(a - b))


if __name__ == "__main__":
    s = Solution()
    assert (
        s.similarPairs(
            [
                "ofwqemdbhrcckcnqvovyjwnbqxckhfohlripwumugcirazdtwo",
                "hsrmuokwhksqkkjblkomibcifqilkwobwcpwwkjlzohffsajrt",
                "uzvsxxbdwfohaujijxmeijbwyydgjiifcqvxfzmkqgwnkpxlpp",
                "ksdoiwhffhymsxebloadgyigkveizbahnbmvmxsuuxaaegxmpe",
                "fcsjnezuizcnfsuaxpmxpdivamaijvvyyqlsjsqlkifahjuanb",
                "odfwurhxumkpwndsppoflaualeghyscdqqwpntxokxviqmjhyq",
                "jbahicbweamnlfbljwyloparlmgqlwiootzoeqovytpapzjezn",
                "vsjxngyknxpkjfexdvmoikjaiccplcwtxcfrljqavatpcoeaqe",
                "lxiztvpppvsjmnnuunvdxalvzuvxlxbdnipexklmgsssyzlesb",
                "kbmiambdsahiptndziqysctinvdekysrsslssusqwhshpwehco",
                "wuwkvgrrshrmbtpyozgzzwiyflpiuklsepljvthmxnppaspuqt",
                "lkajvmdzpsxoaqzrgrhuhhmwlgwfnruxsrjolnielwcyjvvhaa",
                "imvgnslsxyqfshgmgecdrignarewusftipgjpteocnlqsfkdcy",
            ]
        )
        == 1
    )
    assert (
        s.similarPairs(
            [
                "ddeebaedceeceeebbaea",
                "aebababacddbbdedaebd",
                "ddcedbcdbedbccbaadaa",
                "cbcadaacbdceceddaedb",
                "cdadedaaaddecdadddbd",
                "dbceaaceaeebcbcadcec",
                "eceabdbabcdcbdbcdabb",
                "eabcdaedbdbccccccbcc",
                "ebdaabbeebeaabddabda",
                "debdadababbbaabaeddd",
                "aacebccdeaecccbcdaac",
            ]
        )
        == 37
    )
    assert s.similarPairs(words=["aba", "aabb", "abcd", "bac", "aabc"]) == 2
    assert s.similarPairs(words=["aabb", "ab", "ba"]) == 3
    assert s.similarPairs(words=["nba", "cba", "dba"]) == 0
