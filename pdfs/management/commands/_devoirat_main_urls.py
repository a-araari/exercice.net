
def get_subject(url):
    try:
        url = url[len('https://www.devoirat.net/'):]
        subject = url[:url.index('/')]
        if subject[-2:] == '-1': subject = subject[:-2]

        return subject
    except Exception as e:
        return None


def get_category(url):
    try:
        categories = ['devoirs', 'cours', 'séries']
        url = url[len('https://www.devoirat.net/'):]

        for category in categories:
            if category in url:
                return category

    except Exception as e:
        pass

    return None


def get_level(url):
    try:
        levels = ['1ère', '2ème', '3ème', 'bac']
        url = url[len('https://www.devoirat.net/'):]

        for level in levels:
            if level in url:
                if level == 'bac':
                    return '4ème'
                return level

    except Exception as e:
        pass

    return None


URLS = [
    "https://www.devoirat.net/allemand/devoirs-allemand/3ème-année/",
    "https://www.devoirat.net/allemand/devoirs-allemand/4ème-année-bac/",
    "https://www.devoirat.net/allemand/séries-allemand/3ème-année/",
    "https://www.devoirat.net/allemand/séries-allemand/4ème-année-bac/",
    "https://www.devoirat.net/anglais/cours-anglais/2ème-année/",
    "https://www.devoirat.net/anglais/cours-anglais/4ème-année-bac/",
    "https://www.devoirat.net/anglais/devoirs-anglais/1ère-année/",
    "https://www.devoirat.net/anglais/devoirs-anglais/2ème-année/",
    "https://www.devoirat.net/anglais/devoirs-anglais/3ème-année/",
    "https://www.devoirat.net/anglais/devoirs-anglais/4ème-année-bac/",
    "https://www.devoirat.net/anglais/séries-anglais/1ère-année/",
    "https://www.devoirat.net/arabe/cours-arabe/1ère-année/",
    "https://www.devoirat.net/arabe/cours-arabe/4ème-année-bac/",
    "https://www.devoirat.net/arabe/devoirs-arabe/1ère-année/",
    "https://www.devoirat.net/arabe/devoirs-arabe/2ème-année/",
    "https://www.devoirat.net/arabe/devoirs-arabe/3ème-année/",
    "https://www.devoirat.net/arabe/devoirs-arabe/4ème-année-bac/",
    "https://www.devoirat.net/espagnol/devoirs-espagnol/3ème-lettre/",
    "https://www.devoirat.net/français/cours-français/2ème-année-bac/",
    "https://www.devoirat.net/français/devoirs-français/1ère-année/",
    "https://www.devoirat.net/français/devoirs-français/2ème-année/",
    "https://www.devoirat.net/français/devoirs-français/3ème-année/",
    "https://www.devoirat.net/français/devoirs-français/4ème-année-bac/",
    "https://www.devoirat.net/français/séries-français/1ère-année/",
    "https://www.devoirat.net/français/séries-français/2ème-année/",
    "https://www.devoirat.net/français/séries-français/4ème-année-bac/",
    "https://www.devoirat.net/histoire-géographie/cours-histoire-géo/",
    "https://www.devoirat.net/histoire-géographie/devoirs-histoire-géo/1ère-année/",
    "https://www.devoirat.net/histoire-géographie/devoirs-histoire-géo/2ème-année/",
    "https://www.devoirat.net/histoire-géographie/devoirs-histoire-géo/3ème-année/",
    "https://www.devoirat.net/histoire-géographie/devoirs-histoire-géo/4ème-année-bac/",
    "https://www.devoirat.net/informatique/cours-informatique/3ème-année/",
    "https://www.devoirat.net/informatique/cours-informatique/bac-eco-gest/",
    "https://www.devoirat.net/informatique/cours-informatique/bac-info/",
    "https://www.devoirat.net/informatique/devoirs-informatique/algorithmique/",
    "https://www.devoirat.net/informatique/devoirs-informatique/bac-economie-gest/",
    "https://www.devoirat.net/informatique/devoirs-informatique/bac-lettres/",
    "https://www.devoirat.net/informatique/devoirs-informatique/bac-math/",
    "https://www.devoirat.net/informatique/devoirs-informatique/bac-sciences-exp/",
    "https://www.devoirat.net/informatique/devoirs-informatique/bac-sport/",
    "https://www.devoirat.net/informatique/devoirs-informatique/bac-technique/",
    "https://www.devoirat.net/informatique/devoirs-informatique/base-de-donnees/",
    "https://www.devoirat.net/informatique/devoirs-informatique/eco-services/",
    "https://www.devoirat.net/informatique/devoirs-informatique/economie-gestion/",
    "https://www.devoirat.net/informatique/devoirs-informatique/informatique-1/",
    "https://www.devoirat.net/informatique/devoirs-informatique/informatique/",
    "https://www.devoirat.net/informatique/devoirs-informatique/lettres/",
    "https://www.devoirat.net/informatique/devoirs-informatique/mathématiques/",
    "https://www.devoirat.net/informatique/devoirs-informatique/sciences-exp/",
    "https://www.devoirat.net/informatique/devoirs-informatique/technique/",
    "https://www.devoirat.net/informatique/devoirs-informatique/tic/",
    "https://www.devoirat.net/informatique/séries-informatique/3ème-si/",
    "https://www.devoirat.net/informatique/séries-informatique/bac-info/",
    "https://www.devoirat.net/informatique/séries-informatique/bac-sc-exp/",
    "https://www.devoirat.net/italien/devoirs-italien/3ème-année/",
    "https://www.devoirat.net/italien/devoirs-italien/4ème-année-bac-1/",
    "https://www.devoirat.net/maths/cours-maths/1ère-année/",
    "https://www.devoirat.net/maths/cours-maths/bac-economie/",
    "https://www.devoirat.net/maths/cours-maths/bac-info/",
    "https://www.devoirat.net/maths/cours-maths/bac-maths/",
    "https://www.devoirat.net/maths/cours-maths/bac-sciences/",
    "https://www.devoirat.net/maths/cours-maths/bac-technique/",
    "https://www.devoirat.net/maths/cours-maths/eco-service/",
    "https://www.devoirat.net/maths/cours-maths/maths/",
    "https://www.devoirat.net/maths/cours-maths/science/",
    "https://www.devoirat.net/maths/cours-maths/sciences/",
    "https://www.devoirat.net/maths/devoirs-maths/1ère-année/",
    "https://www.devoirat.net/maths/devoirs-maths/2ème-trimestre-1/",
    "https://www.devoirat.net/maths/devoirs-maths/2ème-trimestre-2/",
    "https://www.devoirat.net/maths/devoirs-maths/2ème-trimestre-3/",
    "https://www.devoirat.net/maths/devoirs-maths/2ème-trimestre/",
    "https://www.devoirat.net/maths/devoirs-maths/3ème-trimestre-1/",
    "https://www.devoirat.net/maths/devoirs-maths/3ème-trimestre-2/",
    "https://www.devoirat.net/maths/devoirs-maths/3ème-trimestre-3/",
    "https://www.devoirat.net/maths/devoirs-maths/3ème-trimestre/",
    "https://www.devoirat.net/maths/devoirs-maths/bac-economie-gestion/",
    "https://www.devoirat.net/maths/devoirs-maths/bac-info/",
    "https://www.devoirat.net/maths/devoirs-maths/bac-math/",
    "https://www.devoirat.net/maths/devoirs-maths/bac-sciences-exp/",
    "https://www.devoirat.net/maths/devoirs-maths/bac-sport/",
    "https://www.devoirat.net/maths/devoirs-maths/bac-technique/",
    "https://www.devoirat.net/maths/devoirs-maths/economie-gestion-1/",
    "https://www.devoirat.net/maths/devoirs-maths/economie-gestion/",
    "https://www.devoirat.net/maths/devoirs-maths/info/",
    "https://www.devoirat.net/maths/devoirs-maths/lettres/",
    "https://www.devoirat.net/maths/devoirs-maths/maths/",
    "https://www.devoirat.net/maths/devoirs-maths/revision-bac/",
    "https://www.devoirat.net/maths/devoirs-maths/sciences-1/",
    "https://www.devoirat.net/maths/devoirs-maths/sciences/",
    "https://www.devoirat.net/maths/devoirs-maths/technique/",
    "https://www.devoirat.net/maths/devoirs-maths/technologies-info/",
    "https://www.devoirat.net/maths/séries-maths/1ère-année/",
    "https://www.devoirat.net/maths/séries-maths/2013-2014-2015/",
    "https://www.devoirat.net/maths/séries-maths/2015-2016/",
    "https://www.devoirat.net/maths/séries-maths/2016-2017-2018-1/",
    "https://www.devoirat.net/maths/séries-maths/2016-2017-2018/",
    "https://www.devoirat.net/maths/séries-maths/2018-2019-2020-1/",
    "https://www.devoirat.net/maths/séries-maths/2018-2019-2020-2/",
    "https://www.devoirat.net/maths/séries-maths/2018-2019-2020/",
    "https://www.devoirat.net/maths/séries-maths/bac-eco-gest/",
    "https://www.devoirat.net/maths/séries-maths/bac-info/",
    "https://www.devoirat.net/maths/séries-maths/bac-math/",
    "https://www.devoirat.net/maths/séries-maths/bac-science/",
    "https://www.devoirat.net/maths/séries-maths/bac-technique/",
    "https://www.devoirat.net/maths/séries-maths/eco-gest/",
    "https://www.devoirat.net/maths/séries-maths/eco-services/",
    "https://www.devoirat.net/maths/séries-maths/info-ti/",
    "https://www.devoirat.net/maths/séries-maths/info/",
    "https://www.devoirat.net/maths/séries-maths/maths/",
    "https://www.devoirat.net/maths/séries-maths/sc-exp/",
    "https://www.devoirat.net/maths/séries-maths/sciences/",
    "https://www.devoirat.net/maths/séries-maths/technique/",
    "https://www.devoirat.net/pensée-islamique/cours-pensée-islamique/4ème-année-bac/",
    "https://www.devoirat.net/pensée-islamique/devoirs-pensée-islamique/1ère-année/",
    "https://www.devoirat.net/pensée-islamique/devoirs-pensée-islamique/2ème-année/",
    "https://www.devoirat.net/pensée-islamique/devoirs-pensée-islamique/3ème-année/",
    "https://www.devoirat.net/pensée-islamique/devoirs-pensée-islamique/4ème-année-bac/",
    "https://www.devoirat.net/philosophie/cours-philosophie/",
    "https://www.devoirat.net/philosophie/devoirs-philosophie/4ème-année-bac/",
    "https://www.devoirat.net/physique/cours-physique-chimie/1ère-année/",
    "https://www.devoirat.net/physique/cours-physique-chimie/2ème-année/",
    "https://www.devoirat.net/physique/cours-physique-chimie/3ème-année/",
    "https://www.devoirat.net/physique/cours-physique-chimie/4ème-année-bac/",
    "https://www.devoirat.net/physique/devoirs-physique/1ère-année/",
    "https://www.devoirat.net/physique/devoirs-physique/2ème-trimestre-1/",
    "https://www.devoirat.net/physique/devoirs-physique/2ème-trimestre/",
    "https://www.devoirat.net/physique/devoirs-physique/3ème-trimestre-1/",
    "https://www.devoirat.net/physique/devoirs-physique/3ème-trimestre/",
    "https://www.devoirat.net/physique/devoirs-physique/bac-info/",
    "https://www.devoirat.net/physique/devoirs-physique/bac-maths/",
    "https://www.devoirat.net/physique/devoirs-physique/bac-sciences/",
    "https://www.devoirat.net/physique/devoirs-physique/bac-sport/",
    "https://www.devoirat.net/physique/devoirs-physique/bac-technique/",
    "https://www.devoirat.net/physique/devoirs-physique/info/",
    "https://www.devoirat.net/physique/devoirs-physique/maths/",
    "https://www.devoirat.net/physique/devoirs-physique/sciences-exp/",
    "https://www.devoirat.net/physique/devoirs-physique/sciences/",
    "https://www.devoirat.net/physique/devoirs-physique/technique/",
    "https://www.devoirat.net/physique/devoirs-physique/technologies-info/",
    "https://www.devoirat.net/physique/séries-physique-chimie/1ère-année/",
    "https://www.devoirat.net/physique/séries-physique-chimie/2ème-année/",
    "https://www.devoirat.net/physique/séries-physique-chimie/3ème-année/",
    "https://www.devoirat.net/physique/séries-physique-chimie/4ème-année-bac/",
    "https://www.devoirat.net/physique/séries-physique-chimie/2014-2015/",
    "https://www.devoirat.net/physique/séries-physique-chimie/2015-2016/",
    "https://www.devoirat.net/physique/séries-physique-chimie/2016-2017-2018/",
    "https://www.devoirat.net/physique/séries-physique-chimie/2016-2017/",
    "https://www.devoirat.net/physique/séries-physique-chimie/2017-2018/",
    "https://www.devoirat.net/physique/séries-physique-chimie/2018-2019-2020/",
    "https://www.devoirat.net/sciences-svt/cours-sciences-svt/1ère-année/",
    "https://www.devoirat.net/sciences-svt/cours-sciences-svt/2ème-année/",
    "https://www.devoirat.net/sciences-svt/cours-sciences-svt/3ème-année/",
    "https://www.devoirat.net/sciences-svt/cours-sciences-svt/4ème-année-bac/",
    "https://www.devoirat.net/sciences-svt/devoirs-sciences-svt/1ère-année/",
    "https://www.devoirat.net/sciences-svt/devoirs-sciences-svt/2ème-année/",
    "https://www.devoirat.net/sciences-svt/devoirs-sciences-svt/3ème-année/",
    "https://www.devoirat.net/sciences-svt/devoirs-sciences-svt/4ème-année-bac/",
    "https://www.devoirat.net/sciences-svt/séries-sciences-svt/1ère-année/",
    "https://www.devoirat.net/sciences-svt/séries-sciences-svt/2ème-année/",
    "https://www.devoirat.net/sciences-svt/séries-sciences-svt/4ème-année-bac/",
    "https://www.devoirat.net/technologie/cours-technologie/1ère-année/",
    "https://www.devoirat.net/technologie/cours-technologie/2ème-année/",
    "https://www.devoirat.net/technologie/cours-technologie/3ème-année/",
    "https://www.devoirat.net/technologie/cours-technologie/4ème-année-bac/",
    "https://www.devoirat.net/technologie/devoirs-technologie/1ère-année/",
    "https://www.devoirat.net/technologie/devoirs-technologie/2ème-année/",
    "https://www.devoirat.net/technologie/devoirs-technologie/3ème-année/",
    "https://www.devoirat.net/technologie/devoirs-technologie/4ème-année-bac/",
    "https://www.devoirat.net/technologie/séries-technologie/1ère-année/",
    "https://www.devoirat.net/technologie/séries-technologie/3ème-année/",
    "https://www.devoirat.net/technologie/séries-technologie/4ème-année-bac/",
    "https://www.devoirat.net/économie-gestion-1/cours-economie-gestion/",
    "https://www.devoirat.net/économie-gestion-1/devoirs-economie-gestion/2ème-année/",
    "https://www.devoirat.net/économie-gestion-1/devoirs-economie-gestion/3ème-année/",
    "https://www.devoirat.net/économie-gestion-1/devoirs-economie-gestion/4ème-année-bac/",
    "https://www.devoirat.net/économie-gestion-1/séries-economie-gestion-1/2ème-economie-gestion/",
    "https://www.devoirat.net/économie-gestion-1/séries-economie-gestion-1/bac-economie-gestion/",
]
