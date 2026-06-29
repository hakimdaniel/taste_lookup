data = [
    ("apple", "manis"),
    ("apple", "manis"),
    ("apple", "manis"),
    ("apple", "masam"),

    ("banana", "manis"),
    ("banana", "manis"),
    ("banana", "manis"),

    ("orange", "masam"),
    ("orange", "masam"),
    ("orange", "manis"),

    ("grape", "manis"),
    ("grape", "manis"),
    ("grape", "manis"),
    ("grape", "masam"),

    ("mango", "manis"),
    ("mango", "manis"),
    ("mango", "manis"),

    ("pineapple", "masam"),
    ("pineapple", "manis"),
    ("pineapple", "masam"),

    ("watermelon", "manis"),
    ("watermelon", "manis"),
    ("watermelon", "manis"),

    ("papaya", "manis"),
    ("papaya", "manis"),
    ("papaya", "manis"),

    ("strawberry", "manis"),
    ("strawberry", "masam"),
    ("strawberry", "manis"),

    ("blueberry", "manis"),
    ("blueberry", "manis"),

    ("lemon", "masam"),
    ("lemon", "masam"),
    ("lemon", "masam"),

    ("lime", "masam"),
    ("lime", "masam"),
    ("lime", "masam"),

    ("cherry", "manis"),
    ("cherry", "manis"),
    ("cherry", "manis"),

    ("peach", "manis"),
    ("peach", "manis"),
    ("peach", "manis"),

    ("pear", "manis"),
    ("pear", "manis"),
    ("pear", "manis"),

    ("plum", "manis"),
    ("plum", "masam"),
    ("plum", "manis"),

    ("kiwi", "masam"),
    ("kiwi", "manis"),
    ("kiwi", "masam"),

    ("pomegranate", "masam"),
    ("pomegranate", "manis"),
    ("pomegranate", "masam"),

    ("durian", "manis"),
    ("durian", "manis"),
    ("durian", "manis"),

    ("jackfruit", "manis"),
    ("jackfruit", "manis"),

    ("dragonfruit", "manis"),
    ("dragonfruit", "manis"),

    ("lychee", "manis"),
    ("lychee", "manis"),
    ("lychee", "manis"),

    ("longan", "manis"),
    ("longan", "manis"),

    ("rambutan", "manis"),
    ("rambutan", "manis"),
    ("rambutan", "manis"),

    ("guava", "manis"),
    ("guava", "masam"),
    ("guava", "manis"),

    ("fig", "manis"),
    ("fig", "manis"),

    ("apricot", "manis"),
    ("apricot", "masam"),
    ("apricot", "manis"),

    ("avocado", "tawar"),
    ("avocado", "tawar"),
]

model = {}

#learn and create model
for fruit, taste in data:
    if fruit not in model:
        model[fruit] = {}

    if taste not in model[fruit]:
        model[fruit][taste] = 0

    model[fruit][taste] += 1

#use model and start predict
def predict(fruit):
    tastes = model.get(fruit, {})
    return max(tastes, key=tastes.get)

print(predict("durian"))
