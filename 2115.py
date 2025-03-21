from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        ingredients_map = dict(zip(recipes, ingredients))
        supplies = set(supplies)
        ok_recipes = set()

        for recipe in recipes:
            if self.h(recipe, ok_recipes, ingredients_map, supplies, set()):
                ok_recipes.add(recipe)

        return list(ok_recipes)

    def h(
        self,
        item: str,
        fulfilled: set[str],
        ingredients_map: dict[str, List[str]],
        supplies: set[str],
        chain: set[str],
    ) -> bool:
        if item in chain:
            return False

        if item in fulfilled or item in supplies:
            return True

        if item not in ingredients_map:
            return False

        chain.add(item)
        if all(
            self.h(ingredient, fulfilled, ingredients_map, supplies, chain)
            for ingredient in ingredients_map[item]
        ):
            chain.remove(item)
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(
        s.findAllRecipes(
            ["burger", "bread", "sandwich"],
            [["sandwich", "meat", "bread"], ["yeast", "flour"], ["bread", "meat"]],
            ["yeast", "flour", "meat"],
        )
    )
    print(
        s.findAllRecipes(
            recipes=["a", "b", "c"], ingredients=[["b"], ["c"], ["a"]], supplies=[]
        )
    )
    print(
        s.findAllRecipes(
            recipes=[
                "xevvq",
                "izcad",
                "p",
                "we",
                "bxgnm",
                "vpio",
                "i",
                "hjvu",
                "igi",
                "anp",
                "tokfq",
                "z",
                "kwdmb",
                "g",
                "qb",
                "q",
                "b",
                "hthy",
            ],
            ingredients=[
                ["wbjr"],
                ["otr", "fzr", "g"],
                ["fzr", "wi", "otr", "xgp", "wbjr", "igi", "b"],
                [
                    "fzr",
                    "xgp",
                    "wi",
                    "otr",
                    "tokfq",
                    "izcad",
                    "igi",
                    "xevvq",
                    "i",
                    "anp",
                ],
                ["wi", "xgp", "wbjr"],
                ["wbjr", "bxgnm", "i", "b", "hjvu", "izcad", "igi", "z", "g"],
                ["xgp", "otr", "wbjr"],
                ["wbjr", "otr"],
                ["wbjr", "otr", "fzr", "wi", "xgp", "hjvu", "tokfq", "z", "kwdmb"],
                ["xgp", "wi", "wbjr", "bxgnm", "izcad", "p", "xevvq"],
                ["bxgnm"],
                ["wi", "fzr", "otr", "wbjr"],
                ["wbjr", "wi", "fzr", "xgp", "otr", "g", "b", "p"],
                ["otr", "fzr", "xgp", "wbjr"],
                ["xgp", "wbjr", "q", "vpio", "tokfq", "we"],
                ["wbjr", "wi", "xgp", "we"],
                ["wbjr"],
                ["wi"],
            ],
            supplies=["wi", "otr", "wbjr", "fzr", "xgp"],
        )
    )
