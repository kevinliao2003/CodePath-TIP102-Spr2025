from collections import defaultdict

# Advanced Problem Set Version 1 - Problem 1: Brand Filter
def filter_sustainable_brands(brands, criterion):
    """
    U - Understand
    - the names are strings
    - the critera is a list of strings
    - is the input always valid
    - brands is a dictionary
    - criteria is never empty

    M - Match
    - dictionary

    P - Plan
    variables:
    - res (sustainable brands to return)

    loop through the dictionary
        if the criterion is in the critera
            add the name to res

    return res

    I - Implement
    - see code below

    R - Review
    - see test cases below

    E - Evaluate
    - TC: O(n * m) where n is the size of brand and m the largest size of "criteria"
    - SC: O(1)
    """

    res = []
    for brand in brands:
        name = brand["name"]
        criteria = brand["criteria"]
        # print("name", name)
        # print("criteria", criteria)
        if criterion in criteria:
            res.append(name)
    return res

brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]
res = filter_sustainable_brands(brands, "eco-friendly")
assert res == ['EcoWear', 'GreenThreads']
res = filter_sustainable_brands(brands_2, "ethical labor")
assert res == ['Earthly']
res = filter_sustainable_brands(brands_3, "carbon-neutral")
assert res == ['GreenLife']

# Advanced Problem Set Version 1 - Problem 3: Fashion Trends
def find_trending_materials(brands):
    """
    U - Understand
    - something is "trending" if it has a frequency > 1

    M - Match
    - dictionary

    P - Plan
    variables:
    - res (list of trending brands to return)

    loop through the list
        set a Counter for materials
        loop through Counter
            if val > 1
                add the name to res

    return res

    I - Implement
    - review code below

    R - Review
    - review test cases below

    E - Evaluate
    TC: O(n * m) for the dictionary, where n = size of brands and m = largest size of materials
    SC: O(n * m)
    """

    res = []
    dic = defaultdict(int)
    for brand in brands:
        materials = brand["materials"]
        for material in materials:
            dic[material] += 1

    for material, freq in dic.items():
        if freq > 1:
            res.append(material)

    return res

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]
res = find_trending_materials(brands)
assert res == ['organic cotton', 'recycled polyester', 'bamboo']
res = find_trending_materials(brands_2)
assert res == ['hemp', 'linen']
res = find_trending_materials(brands_3)
assert res == ['recycled polyester']