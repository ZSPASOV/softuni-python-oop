# def add_photo(self, label: str) -> str:
#     for idx, page in enumerate(self.photos):
#         if len(page) < 4:
#             page.append(label)
#             return f'{label} photo added successfully on page {idx + 1} slot {len(page)}'
#
#     return 'No more free spots'

photos = [[] for _ in range(4)]
for idx, page in enumerate(photos):
    if len(page) < 4:
        page.append('yo')


print(photos)

for idx, page in enumerate(photos):
    if len(page) < 4:
        page.append('yo')

print(photos)