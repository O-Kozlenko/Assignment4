def merge_guest_lists(*lists):
    result = []
    for a in lists:
        for i in a:
            if not i in result:
                result.append(i)
    return sorted(result)



facebook = ["Zahar","Sasha", "Denis", "Kostya"]
youtube = ["Sasha","Andrew","Egor"]
onlyfans = ["Denis", "Nazar", "Kostya"]
merge_guest_lists(facebook,youtube)
print(merge_guest_lists(facebook,youtube,onlyfans))