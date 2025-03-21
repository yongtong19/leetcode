from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        ingredients_map = dict(zip(recipes, ingredients))
        supplies = set(supplies)
        recipe_status = dict(zip(recipes, [None] * len(recipes)))

        for recipe in recipes:
            self.check_recipe(recipe, recipe_status, ingredients_map, supplies, set())

        return list([recipe for recipe in recipes if recipe_status[recipe]])

    def check_recipe(
        self,
        recipe: str,
        recipe_status: dict[str, bool | None],
        ingredients_map: dict[str, List[str]],
        supplies: set[str],
        recipe_chain: set[str],
    ) -> bool:
        if recipe_status[recipe] is not None:
            return recipe_status[recipe]

        if recipe in recipe_chain:
            return False

        recipe_chain.add(recipe)
        fulfilled = True
        for ingredient in ingredients_map[recipe]:
            if ingredient not in ingredients_map:
                fulfilled &= ingredient in supplies

            else:
                fulfilled &= self.check_recipe(
                    ingredient, recipe_status, ingredients_map, supplies, recipe_chain
                )

            if not fulfilled:
                break

        recipe_chain.remove(recipe)
        recipe_status[recipe] = fulfilled
        return recipe_status[recipe]


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
