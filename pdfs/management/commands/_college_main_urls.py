
def get_subject(url):
    try:
        url = url[len('https://www.tunisiecollege.net/'):]
        subject = url[:url.index('/')]
        if subject[-2:] == '-1': subject = subject[:-2]

        return subject
    except Exception as e:
        return None


def get_category(url):
    try:
        categories = [
            ['devoirs', 'tp', 'فــــروض', 'sujets-bac', 'epreuves-corrigées', 'مواضيع', 'تقييمات', 'travaux-pratiques', 'tps/'],
            ['cours', 'résumés', 'education', 'دروس', 'وثائق', 'دروس', 'الكتب-المدرسية', 'مطالعة'],
            ['séries', 'تمارين', 'série', 'series', 'serie', 'ﺗﻤﺎﺭﻳﻦ', 'exercices', 'révision', 'تمارين'],
        ]
        url = url[len('https://www.devoir.tn/'):]

        for category in categories:
            if 1 in [1 if l in url.lower() else 0 for l in category]:
                return category[0]

        # Search for arabic categories but return the convenient english category
        for i in range(len(categories_ar)):
            if categories_ar[i] in url.lower():
                return categories[i]

    except Exception as e:
        pass

    return None



def get_level(url):
    try:
        levels = [
            ['7ème', '7éme', '7-ème', '7eme', 'السابعة-7-أساسي', 'السـابعة-أســاسي'],
            ['8ème', '8éme', '8-ème', '8eme', 'الثامنة-8-أساسي', 'الثـــامنة-أســاسي'],
            ['9ème', '9éme', '9-ème', '9eme', 'التاسعة-9-أساسي', 'التـــاسعة-أســاسي'],
        ]
        url = url[len('https://www.devoir.tn/'):]

        for level in levels:
            if 1 in [1 if l in url.lower() else 0 for l in level]:
                # For bac and 4eme
                if level[0] == levels[-1][0]: return levels[-2][0]
                return level[0]

    except Exception as e:
        pass

    return None


URLS = [
    "https://www.tunisiecollege.net/anglais/devoirs-anglais/7-ème/",
    "https://www.tunisiecollege.net/anglais/devoirs-anglais/8-ème/",
    "https://www.tunisiecollege.net/anglais/devoirs-anglais/9-ème/",
    "https://www.tunisiecollege.net/anglais/séries-anglais/",
    "https://www.tunisiecollege.net/arabe/دروس-العربية/التاسعة-9-أساسي/",
    "https://www.tunisiecollege.net/arabe/دروس-العربية/الثامنة-8-أساسي/",
    "https://www.tunisiecollege.net/arabe/دروس-العربية/السابعة-7-أساسي/",
    "https://www.tunisiecollege.net/arabe/فــــروض-الـعــــربـيــة/التاسعة-9-أساسي/",
    "https://www.tunisiecollege.net/arabe/فــــروض-الـعــــربـيــة/الثامنة-8-أساسي/",
    "https://www.tunisiecollege.net/arabe/فــــروض-الـعــــربـيــة/السابعة-7-أساسي/",
    "https://www.tunisiecollege.net/education-civique/فــــروض-الـتــــربـيـة-الـمــــدنـيـة/",
    "https://www.tunisiecollege.net/education-islamique/فــــروض-الـتــــربـيـة-الإســـلامـيـة/التـــاسعة-أســاسي/",
    "https://www.tunisiecollege.net/education-islamique/فــــروض-الـتــــربـيـة-الإســـلامـيـة/الثـــامنة-أســاسي/",
    "https://www.tunisiecollege.net/education-islamique/فــــروض-الـتــــربـيـة-الإســـلامـيـة/السـابعة-أســاسي/",
    "https://www.tunisiecollege.net/education-musicale/دروس-الـتــــربـيـة-المــوسـيـقـيـة/السـابعة-أســاسي/",
    "https://www.tunisiecollege.net/education-musicale/فــــروض-الـتــــربـيـة-المــوسـيـقـيـة/التاسعة-أساسي/",
    "https://www.tunisiecollege.net/education-musicale/فــــروض-الـتــــربـيـة-المــوسـيـقـيـة/الثـــامنة-أســاسي/",
    "https://www.tunisiecollege.net/education-musicale/فــــروض-الـتــــربـيـة-المــوسـيـقـيـة/السـابعة-أســاسي-1/",
    "https://www.tunisiecollege.net/education-théâtrale/فروض-التربية-المسرحية/",
    "https://www.tunisiecollege.net/education-théâtrale/فروض-التربية-المسرحية/السـابعة-أســاسي/",
    "https://www.tunisiecollege.net/français/cours-français/",
    "https://www.tunisiecollege.net/français/devoirs-français/7-ème/",
    "https://www.tunisiecollege.net/français/devoirs-français/8-ème/",
    "https://www.tunisiecollege.net/français/devoirs-français/9-ème/",
    "https://www.tunisiecollege.net/français/séries-français/",
    "https://www.tunisiecollege.net/histoire-géographie/دروس-التــاريخ/",
    "https://www.tunisiecollege.net/histoire-géographie/فــــروض-الـتــاريــخ-و-الـجـغـرافــيـــــا/التاسعة-9-أساسي/",
    "https://www.tunisiecollege.net/histoire-géographie/فــــروض-الـتــاريــخ-و-الـجـغـرافــيـــــا/الثامنة-8-أساسي/",
    "https://www.tunisiecollege.net/histoire-géographie/فــــروض-الـتــاريــخ-و-الـجـغـرافــيـــــا/السابعة-7-أساسي/",
    "https://www.tunisiecollege.net/informatique/cours-informatique/",
    "https://www.tunisiecollege.net/informatique/cours-informatique/cours-architecture-et-système/",
    "https://www.tunisiecollege.net/informatique/cours-informatique/cours-internet-e-mail/",
    "https://www.tunisiecollege.net/informatique/cours-informatique/cours-présentation/",
    "https://www.tunisiecollege.net/informatique/devoirs-informatique/7ème/",
    "https://www.tunisiecollege.net/informatique/devoirs-informatique/8ème/",
    "https://www.tunisiecollege.net/informatique/devoirs-informatique/9ème/",
    "https://www.tunisiecollege.net/informatique/séries-informatique/7ème/",
    "https://www.tunisiecollege.net/informatique/séries-informatique/8ème/",
    "https://www.tunisiecollege.net/informatique/séries-informatique/9ème/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/7ème/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/8ème/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/9ème/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/tp-audacity/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/tp-excel-2003/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/tp-powerpoint-2003/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/tp-réseau-local/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/tp-système-d-exploitation/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/tp-traitement-d-images/",
    "https://www.tunisiecollege.net/informatique/tp-informatique/tp-word-2003/",
    "https://www.tunisiecollege.net/maths/cours-maths/7ème-de-base/",
    "https://www.tunisiecollege.net/maths/cours-maths/8ème-de-base/",
    "https://www.tunisiecollege.net/maths/cours-maths/9ème-de-base/",
    "https://www.tunisiecollege.net/maths/devoirs-math/2ème-trimestre-1/",
    "https://www.tunisiecollege.net/maths/devoirs-math/2ème-trimestre-2/",
    "https://www.tunisiecollege.net/maths/devoirs-math/2ème-trimestre/",
    "https://www.tunisiecollege.net/maths/devoirs-math/3ème-trimestre-1/",
    "https://www.tunisiecollege.net/maths/devoirs-math/3ème-trimestre-2/",
    "https://www.tunisiecollege.net/maths/devoirs-math/3ème-trimestre/",
    "https://www.tunisiecollege.net/maths/devoirs-math/7ème/",
    "https://www.tunisiecollege.net/maths/devoirs-math/8ème/",
    "https://www.tunisiecollege.net/maths/devoirs-math/9-ème/",
    "https://www.tunisiecollege.net/maths/séries-d-exercices-math/2017-2018-2019/",
    "https://www.tunisiecollege.net/maths/séries-d-exercices-math/séries-math-7ème/",
    "https://www.tunisiecollege.net/maths/séries-d-exercices-math/séries-math-8ème/",
    "https://www.tunisiecollege.net/maths/séries-d-exercices-math/séries-math-9ème/",
    "https://www.tunisiecollege.net/physique/cours-physique/",
    "https://www.tunisiecollege.net/physique/devoirs-physique/7-ème/",
    "https://www.tunisiecollege.net/physique/devoirs-physique/8-ème/",
    "https://www.tunisiecollege.net/physique/devoirs-physique/9-ème/",
    "https://www.tunisiecollege.net/physique/séries-physique/7ème/",
    "https://www.tunisiecollege.net/physique/séries-physique/8ème/",
    "https://www.tunisiecollege.net/physique/séries-physique/9ème/",
    "https://www.tunisiecollege.net/sciences-svt/cours-sciences-svt/8eme/",
    "https://www.tunisiecollege.net/sciences-svt/cours-sciences-svt/9eme/",
    "https://www.tunisiecollege.net/sciences-svt/devoirs-sciences/7-ème/",
    "https://www.tunisiecollege.net/sciences-svt/devoirs-sciences/8-ème/",
    "https://www.tunisiecollege.net/sciences-svt/devoirs-sciences/9-ème/",
    "https://www.tunisiecollege.net/technologie/cours-technologie/7ème/",
    "https://www.tunisiecollege.net/technologie/cours-technologie/8ème/",
    "https://www.tunisiecollege.net/technologie/cours-technologie/9éme/",
    "https://www.tunisiecollege.net/technologie/devoirs-technologie/7-ème/",
    "https://www.tunisiecollege.net/technologie/devoirs-technologie/8-ème/",
    "https://www.tunisiecollege.net/technologie/devoirs-technologie/9-ème/",
    "https://www.tunisiecollege.net/technologie/séries-technologie/8ème/",
]


for url in URLS:
    if not get_category(url): print(url)
