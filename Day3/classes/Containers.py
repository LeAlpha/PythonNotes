# Udover at kunne bruge diverse datastrukere, såsom lists, og dics, vi kan lave vores egen i en klasse:
# En customContainer


class TagCloud:
    def __init__(self):
        self.tags = {}

    # Styr hvordan add skal ske:
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # definer get:
    def __getitem__(self, key):
        return self.tags.get(key.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # antal af occurences:
    def __len__(self):
        return len(self.tags)

    # Definer en iteration metode:
    def __itter__(self):
        return iter(self.tags)


cloud = TagCloud()

cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud.tags)
print(cloud.__getitem__("python"))
print(cloud.__len__())

print(cloud.__itter__().)
